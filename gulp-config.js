module.exports = {
  'autoprefixer': {
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
  },
  'css': {
    'params': {
      'includePaths': [
        'node_modules/bourbon/app/assets/stylesheets/',
        'node_modules/chrys/src/css/'
      ],
      'errLogToConsole': true
    }
  },
  // 'dist': {
  //   'css': 'css/'
  // },
  // 'src': {
  //   'css': 'src/css/'
  // },
  'watchTasks': [
    //
    {
      files: [
        'data/src/**/*',
        'src/**/*'
      ],
      tasks: [
        'build'
      ]
    }
  ],
  'webserver': {
    'host': 'localhost',
    'port': 8000,
    'path': '/',
    'livereload': false,
    'directoryListing': false,
    'open': '/demo/',
    'https': false,
    'browsers': {
      'default': 'firefox',
      'darwin': 'google chrome',
      'linux': 'google-chrome',
      'win32': 'chrome'
    }
  }
};
