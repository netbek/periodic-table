var _ = require('lodash');
var autoprefixer = require('gulp-autoprefixer');
var cheerio = require('cheerio');
var cheerioTableparser = require('cheerio-tableparser');
var cssmin = require('gulp-cssmin');
var csvtojson = require('csvtojson');
var Decimal = require('decimal.js');
var del = require('del');
var fs = require('fs');
var gulp = require('gulp');
var mkdirp = require('mkdirp');
var nunjucks = require('nunjucks');
var Promise = require('bluebird');
var rename = require('gulp-rename');
var runSequence = require('run-sequence');
var sass = require('gulp-sass');
var yaml = require('js-yaml');

Promise.promisifyAll(fs);

var mkdirpAsync = Promise.promisify(mkdirp);

gulp.task('build-data', function (cb) {
  var wikidata;

  var Converter = csvtojson.Converter;
  var converter = new Converter({
    headers: [
      'string#!atomicNumber',
      'string#!symbol',
      'string#!name',
      'string#!atomicMass',
      'string#!cpkHexColor',
      'string#!electronicConfiguration',
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

      row.group = '';
      row.period = '';

      var wikidataIndex = wikidata[0].indexOf(row.atomicNumber.toString());

      if (wikidataIndex > -1) {
        row.symbol = wikidata[1][wikidataIndex];
        row.name = wikidata[1][wikidataIndex];
        row.group = wikidata[4][wikidataIndex] ? Number(wikidata[4][wikidataIndex]) : '';
        row.period = wikidata[5][wikidataIndex] ? Number(wikidata[5][wikidataIndex]) : '';
      }

      return row;
    });

    var str = yaml.safeDump(rows);

    fs.writeFileAsync('data/elements.yml', str, 'utf8')
      .then(function () {
        cb();
      });
  });

  fs.readFileAsync('data/src/list-of-chemical-elements.html', 'utf8')
    .then(function (str) {
      var $ = cheerio.load(str);
      cheerioTableparser($);
      var data = $('table.wikitable').first().parsetable(false, false, true);

      return _.map(data, function (value) {
        return value.slice(2);
      });
    })
    .then(function (data) {
      wikidata = data;

      fs.createReadStream('data/src/pt-data1.csv')
        .pipe(converter);
    })
});

function buildCss(src, dist) {
  return gulp
    .src(src)
    .pipe(sass({
      'includePaths': [
        'src/css/'
      ],
      'errLogToConsole': true
    }).on('error', sass.logError))
    .pipe(autoprefixer({
      'browsers': [
        'last 2 versions',
        'ie >= 8',
        'ff >= 5',
        'chrome >= 20',
        'opera >= 12',
        'safari >= 4',
        'ios >= 6',
        'android >= 2',
        'bb >= 6'
      ]
    }))
    .pipe(gulp.dest(dist))
    .pipe(cssmin({
      advanced: false
    }))
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(dist));
}

gulp.task('build-css', function (cb) {
  buildCss('src/css/**/*.scss', 'css/')
    .on('end', cb);
});

gulp.task('build-demo-page', function (cb) {
  var elements;

  fs.readFileAsync('data/elements.yml', 'utf8')
    .then(function (str) {
      elements = yaml.safeLoad(str);

      return mkdirpAsync('demo/');
    })
    .then(function () {
      var res = nunjucks.render('src/demo/index.njk', {
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

gulp.task('default', ['build']);
