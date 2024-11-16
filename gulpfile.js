/* eslint-disable @typescript-eslint/no-var-requires */
const _ = require('lodash');
const autoprefixer = require('autoprefixer');
const esbuild = require('esbuild');
const fs = require('fs-extra');
const ghPages = require('gulp-gh-pages');
const globby = require('globby');
const gulp = require('gulp');
const livereload = require('livereload');
const nunjucks = require('nunjucks');
const open = require('open');
const os = require('os');
const path = require('path');
const periodicTable = require('.');
const pixrem = require('pixrem');
const postcss = require('postcss');
const postcssColorRgbaFallback = require('postcss-color-rgba-fallback');
const postcssOpacity = require('postcss-opacity');
const Promise = require('bluebird');
const sass = require('sass-embedded');
const webserver = require('gulp-webserver');

/* -----------------------------------------------------------------------------
 * Config
 ---------------------------------------------------------------------------- */

const gulpConfig = require('./gulp-config.js');

const livereloadOpen =
  (gulpConfig.webserver.https ? 'https' : 'http') +
  '://' +
  gulpConfig.webserver.host +
  ':' +
  gulpConfig.webserver.port +
  (gulpConfig.webserver.open ? gulpConfig.webserver.open : '/');

/* -----------------------------------------------------------------------------
 * Misc
 ---------------------------------------------------------------------------- */

const flags = {
  livereloadInit: false // Whether `livereload-init` task has been run
};
let server;

// Choose browser for node-open.
let browser = gulpConfig.webserver.browsers.default;
const platform = os.platform();
if (_.has(gulpConfig.webserver.browsers, platform)) {
  browser = gulpConfig.webserver.browsers[platform];
}

/* -----------------------------------------------------------------------------
 * Functions
 ---------------------------------------------------------------------------- */

async function buildCss(src, destDir) {
  const files = await globby(src);

  for (const file of files) {
    let css = (await sass.compileAsync(file, gulpConfig.sass)).css;

    css = (
      await postcss([
        autoprefixer(gulpConfig.autoprefixer),
        pixrem,
        postcssColorRgbaFallback,
        postcssOpacity
      ]).process(css, {
        from: undefined,
        to: destDir
      })
    ).css;

    const cssMin = (
      await esbuild.transform(css, {
        loader: 'css',
        minify: true,
        legalComments: 'none'
      })
    ).code;

    const basename = path.basename(file);
    const destPath = path.join(destDir, basename.replace(/\.scss$/, '.css'));
    const destMinPath = path.join(
      destDir,
      basename.replace(/\.scss$/, '.min.css')
    );

    await fs.outputFile(destPath, css, 'utf-8');
    await fs.outputFile(destMinPath, cssMin, 'utf-8');
  }
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
  const conf = _.clone(gulpConfig.webserver);
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

  _.forEach(gulpConfig.watchTasks, function (watchConfig) {
    const tasks = _.clone(watchConfig.tasks);
    tasks.push(livereloadTask);
    startWatch(watchConfig.files, tasks);
  });
});

/* -----------------------------------------------------------------------------
 * Tasks
 ---------------------------------------------------------------------------- */

gulp.task('build-demo-css', async () =>
  buildCss(['src/css/**/!(_)*.scss', 'src/demo/css/**/!(_)*.scss'], 'demo/css')
);

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
  gulp.series('build-demo-css', 'build-demo-page', 'build-demo-vendor')
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
