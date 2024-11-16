const {browserslist} = require('./package.json');

module.exports = {
  autoprefixer: {
    overrideBrowserslist: browserslist
  },
  css: {
    params: {
      includePaths: ['node_modules/chrys/src/css/'],
      errLogToConsole: true
    }
  },
  sass: {
    loadPaths: ['.'],
    outputStyle: 'expanded',
    silenceDeprecations: [
      'abs-percent',
      'bogus-combinators',
      'call-string',
      'color-module-compat',
      'css-function-mixin',
      'duplicate-var-flags',
      'elseif',
      'feature-exists',
      'fs-importer-cwd',
      'function-units',
      'global-builtin',
      'import',
      'mixed-decls',
      'moz-document',
      'new-global',
      'null-alpha',
      'relative-canonical',
      'slash-div',
      'strict-unary'
      // 'user-authored'
    ]
  },
  watchTasks: [
    {
      files: ['data/src/**/*', 'src/**/*'],
      tasks: ['build']
    }
  ],
  webserver: {
    host: 'localhost',
    port: 8000,
    path: '/',
    livereload: false,
    directoryListing: false,
    open: '/demo/',
    https: false,
    browsers: {
      default: 'firefox',
      darwin: 'google chrome',
      linux: 'google-chrome',
      win32: 'chrome'
    }
  }
};
