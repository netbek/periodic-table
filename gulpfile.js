var _ = require('lodash');
var autoprefixer = require('autoprefixer');
var cheerio = require('cheerio');
var cheerioTableparser = require('cheerio-tableparser');
var cssmin = require('gulp-cssmin');
var csvtojson = require('csvtojson');
var Decimal = require('decimal.js');
var del = require('del');
var fs = require('fs-extra');
var gulp = require('gulp');
var livereload = require('livereload');
var nunjucks = require('nunjucks');
var open = require('open');
var os = require('os');
var postcss = require('gulp-postcss');
var postcssColorRgbaFallback = require('postcss-color-rgba-fallback');
var postcssOpacity = require('postcss-opacity');
var Promise = require('bluebird');
var rename = require('gulp-rename');
var runSequence = require('run-sequence');
var sass = require('gulp-sass');
var webserver = require('gulp-webserver');
var yaml = require('js-yaml');

Promise.promisifyAll(fs);

/*******************************************************************************
 * Config
 ******************************************************************************/

var config = require('./gulp-config.js');

var livereloadOpen = (config.webserver.https ? 'https' : 'http') + '://' + config.webserver.host + ':' + config.webserver.port + (config.webserver.open ? config.webserver.open : '/');

/*******************************************************************************
 * Misc
 ******************************************************************************/

var flags = {
  livereloadInit: false // Whether `livereload-init` task has been run
};
var server;

// Choose browser for node-open.
var browser = config.webserver.browsers.default;
var platform = os.platform();
if (_.has(config.webserver.browsers, platform)) {
  browser = config.webserver.browsers[platform];
}

/*******************************************************************************
 * Functions
 ******************************************************************************/

/**
 *
 * @param  {String} src
 * @param  {String} dist
 * @return {Stream}
 */
function buildCss(src, dist) {
  return gulp
    .src(src)
    .pipe(sass(config.css.params).on('error', sass.logError))
    .pipe(postcss([
      autoprefixer(config.autoprefixer),
      postcssColorRgbaFallback,
      postcssOpacity
    ]))
    .pipe(gulp.dest(dist))
    .pipe(cssmin({
      advanced: false
    }))
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(dist));
}

/**
 * Start a watcher.
 *
 * @param {Array} files
 * @param {Array} tasks
 * @param {Boolean} livereload Set to TRUE to force livereload to refresh the page.
 */
function startWatch(files, tasks, livereload) {
  if (livereload) {
    tasks.push('livereload-reload');
  }

  gulp.watch(files, function () {
    runSequence.apply(null, tasks);
  });
}

/*******************************************************************************
 * Livereload tasks
 ******************************************************************************/

// Start webserver.
gulp.task('webserver-init', function (cb) {
  var conf = _.clone(config.webserver);
  conf.open = false;

  gulp.src('./')
    .pipe(webserver(conf))
    .on('end', cb);
});

// Start livereload server
gulp.task('livereload-init', function (cb) {
  if (!flags.livereloadInit) {
    flags.livereloadInit = true;
    server = livereload.createServer();
    open(livereloadOpen, browser);
  }

  cb();
});

// Refresh page
gulp.task('livereload-reload', function (cb) {
  server.refresh(livereloadOpen);
  cb();
});

/*******************************************************************************
 * Tasks
 ******************************************************************************/

gulp.task('build-data', function (cb) {
  var blocksData;
  var wikidata;
  var categoryColorMap = {};

  var Converter = csvtojson.Converter;
  var converter = new Converter({
    headers: [
      'string#!atomicNumber',
      'string#!symbol',
      'string#!name',
      'string#!atomicMass',
      'string#!cpkHexColor',
      'string#!electronConfiguration',
      'string#!electronegativity',
      'string#!atomicRadius',
      'string#!ionRadius',
      'string#!vanDelWaalsRadius',
      'string#!ionizationEnergy',
      'string#!electronAffinity',
      'string#!oxidationStates',
      'string#!standardState',
      'string#!bondingType',
      'string#!meltingPoint',
      'string#!boilingPoint',
      'string#!density',
      'string#!groupBlock',
      'string#!yearDiscovered'
    ],
    noheader: true
  });

  converter.on('end_parsed', function (rows) {
    rows = _.map(rows, function (row) {
      row = _.pick(row, [
        'atomicNumber',
        'symbol',
        'name',
        'atomicMass',
        'electronegativity'
      ]);

      if (!isNaN(row.atomicNumber)) {
        row.atomicNumber = Number(row.atomicNumber);
      }

      row.atomicMass = row.atomicMass.replace(/^([0-9\.]+).*$/, '$1');
      row.atomicMass = row.atomicMass.replace(/\[/, '(').replace(/\]/, ')');

      if (!isNaN(row.atomicMass)) {
        row.atomicMass = Number(row.atomicMass);
        row.atomicMass = (new Decimal(row.atomicMass)).toDecimalPlaces(2).valueOf();
      }

      if (!isNaN(row.electronegativity)) {
        row.electronegativity = Number(row.electronegativity);
      }

      row.block = _.find(blocksData, {
        atomicNumber: row.atomicNumber
      }).block;
      row.group = '';
      row.period = '';
      row.category = '';

      var wikidataIndex = wikidata[0].indexOf(row.atomicNumber.toString());

      if (wikidataIndex > -1) {
        row.symbol = wikidata[1][wikidataIndex];
        row.name = wikidata[2][wikidataIndex];
        row.group = wikidata[4][wikidataIndex] ? Number(wikidata[4][wikidataIndex]) : '';
        row.period = wikidata[5][wikidataIndex] ? Number(wikidata[5][wikidataIndex]) : '';
        row.category = wikidata[13][wikidataIndex] ? wikidata[13][wikidataIndex] : '';
      }

      return row;
    });

    var str = yaml.safeDump(rows);

    fs.writeFileAsync('data/elements.yml', str, 'utf8')
      .then(function () {
        cb();
      });
  });

  fs.readFileAsync('data/src/blocks.yml', 'utf8')
    .then(function (str) {
      blocksData = yaml.safeLoad(str);

      return fs.readFileAsync('data/categories.yml', 'utf8');
    })
    .then(function (str) {
      var values = yaml.safeLoad(str);

      _.forEach(values, function (value) {
        categoryColorMap[value.id] = value.color;
      });

      return fs.readFileAsync('data/src/list-of-chemical-elements.html', 'utf8');
    })
    .then(function (str) {
      var $ = cheerio.load(str);

      var categories = [];

      $('table.wikitable > tr > td:nth-child(2)').each(function (i, elm) {
        var $elm = $(this);
        var color = $elm.css('background').trim().toLowerCase();
        var category = _.findKey(categoryColorMap, function (value) {
          return value == color;
        });
        categories.push(category);
      });

      cheerioTableparser($);
      var data = $('table.wikitable').first().parsetable(false, false, true);

      data = _.map(data, function (value) {
        return value.slice(2);
      });

      data.push(categories);

      return data;
    })
    .then(function (data) {
      wikidata = data;

      fs.createReadStream('data/src/pt-data1.csv')
        .pipe(converter);
    })
});

gulp.task('build-css', function (cb) {
  buildCss('src/css/**/*.scss', 'css/')
    .on('end', cb);
});

gulp.task('build-demo-page', function (cb) {
  var categories;
  var elements;

  fs.readFileAsync('data/categories.yml', 'utf8')
    .then(function (str) {
      categories = yaml.safeLoad(str);

      return fs.readFileAsync('data/elements.yml', 'utf8');
    })
    .then(function (str) {
      elements = yaml.safeLoad(str);

      return fs.mkdirpAsync('demo/');
    })
    .then(function () {
      var res = nunjucks.render('src/demo/index.njk', {
        categories: categories,
        elements: elements
      }, function (err, res) {
        if (err) {
          console.log(err);
          cb();
        }
        else {
          fs.writeFileAsync('demo/index.html', res, 'utf8')
            .then(function () {
              cb();
            });
        }
      });
    });
});

gulp.task('build-demo-css', function (cb) {
  buildCss('src/demo/css/**/*.scss', 'demo/css/')
    .on('end', cb);
});

gulp.task('build', function (cb) {
  runSequence(
    'build-data',
    'build-css',
    'build-demo-page',
    'build-demo-css',
    cb
  );
});

gulp.task('livereload', function () {
  runSequence(
    'build',
    'webserver-init',
    'livereload-init',
    'watch:livereload'
  );
});

/*******************************************************************************
 * Watch tasks
 ******************************************************************************/

// Watch with livereload that doesn't rebuild docs
gulp.task('watch:livereload', function (cb) {
  var livereloadTask = 'livereload-reload';

  _.forEach(config.watchTasks, function (watchConfig) {
    var tasks = _.clone(watchConfig.tasks);
    tasks.push(livereloadTask);
    startWatch(watchConfig.files, tasks);
  });
});

/*******************************************************************************
 * Default task
 ******************************************************************************/

gulp.task('default', ['build']);
