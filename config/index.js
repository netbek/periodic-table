export const config = {
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
  }
};
