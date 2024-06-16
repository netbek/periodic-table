const _ = require('lodash');
const autoprefixer = require('autoprefixer');
const cheerio = require('cheerio');
const cheerioTableparser = require('cheerio-tableparser');
const cssmin = require('gulp-cssmin');
const csvtojson = require('csvtojson');
const Decimal = require('decimal.js');
const fs = require('fs-extra');
const ghPages = require('gulp-gh-pages');
const gulp = require('gulp');
const livereload = require('livereload');
const nunjucks = require('nunjucks');
const open = require('open');
const os = require('os');
const periodicTable = require('.');
const pixrem = require('pixrem');
const postcss = require('gulp-postcss');
const postcssColorRgbaFallback = require('postcss-color-rgba-fallback');
const postcssOpacity = require('postcss-opacity');
const Promise = require('bluebird');
const rename = require('gulp-rename');
const sass = require('gulp-sass')(require('node-sass'));
const webserver = require('gulp-webserver');
const yaml = require('js-yaml');

Promise.promisifyAll(fs);

/* -----------------------------------------------------------------------------
 * Config
 ---------------------------------------------------------------------------- */

const config = require('./gulp-config.js');

const livereloadOpen =
  (config.webserver.https ? 'https' : 'http') +
  '://' +
  config.webserver.host +
  ':' +
  config.webserver.port +
  (config.webserver.open ? config.webserver.open : '/');

/* -----------------------------------------------------------------------------
 * Misc
 ---------------------------------------------------------------------------- */

const flags = {
  livereloadInit: false // Whether `livereload-init` task has been run
};
let server;

// Choose browser for node-open.
let browser = config.webserver.browsers.default;
const platform = os.platform();
if (_.has(config.webserver.browsers, platform)) {
  browser = config.webserver.browsers[platform];
}

/* -----------------------------------------------------------------------------
 * Functions
 ---------------------------------------------------------------------------- */

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
    .pipe(
      postcss([
        autoprefixer(config.autoprefixer),
        pixrem,
        postcssColorRgbaFallback,
        postcssOpacity
      ])
    )
    .pipe(gulp.dest(dist))
    .pipe(
      cssmin({
        advanced: false
      })
    )
    .pipe(
      rename({
        suffix: '.min'
      })
    )
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

  return gulp.watch(files, gulp.series(...tasks));
}

/* -----------------------------------------------------------------------------
 * Livereload tasks
 ---------------------------------------------------------------------------- */

// Start webserver.
gulp.task('webserver-init', function (cb) {
  const conf = _.clone(config.webserver);
  conf.open = false;

  gulp.src('./').pipe(webserver(conf)).on('end', cb);
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

// Watch with livereload that doesn't rebuild docs
gulp.task('watch:livereload', function () {
  const livereloadTask = 'livereload-reload';

  _.forEach(config.watchTasks, function (watchConfig) {
    const tasks = _.clone(watchConfig.tasks);
    tasks.push(livereloadTask);
    startWatch(watchConfig.files, tasks);
  });
});

/* -----------------------------------------------------------------------------
 * Tasks
 ---------------------------------------------------------------------------- */

gulp.task('build-data', () => {
  let blocksData;
  let wikidata;
  const categoryColorMap = {};

  return fs
    .readFile('data/src/blocks.yml', 'utf-8')
    .then(function (str) {
      blocksData = yaml.load(str);

      return fs.readFile('data/categories.yml', 'utf-8');
    })
    .then(function (str) {
      const values = yaml.load(str);

      _.forEach(values, function (value) {
        categoryColorMap[value.id] = value.color;
      });

      return fs.readFile('data/src/list-of-chemical-elements.html', 'utf-8');
    })
    .then(function (str) {
      const $ = cheerio.load(str);

      const categories = [];

      $('table.wikitable > tr > td:nth-child(2)').each(function () {
        const $elm = $(this);
        const color = $elm.css('background').trim().toLowerCase();
        const category = _.findKey(categoryColorMap, function (value) {
          return value == color;
        });
        categories.push(category);
      });

      cheerioTableparser($);
      let data = $('table.wikitable').first().parsetable(false, false, true);

      data = _.map(data, function (value) {
        return value.slice(2);
      });

      data.push(categories);

      return data;
    })
    .then((data) => {
      wikidata = data;

      const parserParams = {
        headers: [
          'atomicNumber',
          'symbol',
          'name',
          'atomicMass',
          'cpkHexColor',
          'electronConfiguration',
          'electronegativity',
          'atomicRadius',
          'ionRadius',
          'vanDelWaalsRadius',
          'ionizationEnergy',
          'electronAffinity',
          'oxidationStates',
          'standardState',
          'bondingType',
          'meltingPoint',
          'boilingPoint',
          'density',
          'groupBlock',
          'yearDiscovered'
        ],
        noheader: true
      };

      return csvtojson(parserParams).fromFile('data/src/pt-data1.csv');
    })
    .then((jsonArray) => {
      const rows = _.map(jsonArray, function (row) {
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

        row.atomicMass = row.atomicMass.replace(/^([0-9.]+).*$/, '$1');
        row.atomicMass = row.atomicMass.replace(/\[/, '(').replace(/\]/, ')');

        if (!isNaN(row.atomicMass)) {
          row.atomicMass = Number(row.atomicMass);
          row.atomicMass = new Decimal(row.atomicMass)
            .toDecimalPlaces(2)
            .valueOf();
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

        const wikidataIndex = wikidata[0].indexOf(row.atomicNumber.toString());

        if (wikidataIndex > -1) {
          row.symbol = wikidata[1][wikidataIndex];
          row.name = wikidata[2][wikidataIndex];
          row.group = wikidata[4][wikidataIndex]
            ? Number(wikidata[4][wikidataIndex])
            : '';
          row.period = wikidata[5][wikidataIndex]
            ? Number(wikidata[5][wikidataIndex])
            : '';
          row.category = wikidata[13][wikidataIndex]
            ? wikidata[13][wikidataIndex]
            : '';
        }

        return row;
      });

      const str = yaml.dump(rows);

      return fs.writeFile('data/elements.yml', str, 'utf-8');
    });
});

gulp.task('build-demo-css', function (cb) {
  buildCss(['src/css/**/*.scss', 'src/demo/css/**/*.scss'], 'demo/css/').on(
    'end',
    cb
  );
});

gulp.task('build-demo-page', function (cb) {
  fs.mkdirpAsync('demo/')
    .then(function () {
      return Promise.props({
        categories: periodicTable.loadCategories(),
        elements: periodicTable.loadElements(),
        groups: periodicTable.loadGroups()
      });
    })
    .then(function (data) {
      nunjucks.render('src/demo/index.njk', data, function (err, res) {
        if (err) {
          console.log(err);
          cb();
        } else {
          fs.writeFileAsync('demo/index.html', res, 'utf-8').then(function () {
            cb();
          });
        }
      });
    });
});

gulp.task('build-demo-vendor', function () {
  return gulp
    .src(['node_modules/normalize-css/**/*.css'])
    .pipe(gulp.dest('demo/css/'));
});

gulp.task(
  'build',
  gulp.series(
    'build-data',
    'build-demo-css',
    'build-demo-page',
    'build-demo-vendor'
  )
);

gulp.task('deploy', function () {
  return gulp.src('demo/**/*').pipe(ghPages());
});

gulp.task(
  'livereload',
  gulp.series('build', 'webserver-init', 'livereload-init', 'watch:livereload')
);

/* -----------------------------------------------------------------------------
 * Default task
 ---------------------------------------------------------------------------- */

gulp.task('default', gulp.series('build'));
