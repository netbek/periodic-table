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
