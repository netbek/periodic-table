import autoprefixer from 'autoprefixer';
import browserslist from 'browserslist';
import esbuild from 'esbuild';
import {globby} from 'globby';
import {copyFile, mkdir, readFile, rm, writeFile} from 'node:fs/promises';
import nunjucks from 'nunjucks';
import path from 'node:path';
import postcss from 'postcss';
import * as sass from 'sass-embedded';
import {promisify} from 'node:util';
import {config} from '../config/index.js';
import {load} from 'js-yaml';

const packageDir = path.resolve(import.meta.dirname, '..');
const destDir = path.join(packageDir, 'dist/demo');
const cssDestDir = path.join(destDir, 'css');
const vendorSrcDir = path.resolve('node_modules/normalize.css');

const renderTemplate = promisify(nunjucks.render);

async function buildDemoCss() {
  const files = await globby([
    'src/css/**/!(_)*.scss',
    'src/demo/css/**/!(_)*.scss'
  ]);

  await mkdir(cssDestDir, {recursive: true});

  for (const file of files) {
    let css = (await sass.compileAsync(file, config.sass)).css;

    css = (
      await postcss([
        autoprefixer({
          overrideBrowserslist: browserslist(undefined, {path: packageDir})
        })
      ]).process(css, {
        from: undefined,
        to: cssDestDir
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
    const destPath = path.join(cssDestDir, basename.replace(/\.scss$/, '.css'));
    const destMinPath = path.join(
      cssDestDir,
      basename.replace(/\.scss$/, '.min.css')
    );

    await writeFile(destPath, css, 'utf-8');
    await writeFile(destMinPath, cssMin, 'utf-8');
  }
}

async function loadYaml(filename) {
  const data = await readFile(
    path.resolve(import.meta.dirname, '..', 'data', filename),
    'utf8'
  );

  return load(data);
}

async function buildDemoPage() {
  await mkdir(destDir, {recursive: true});

  const [categories, elements, groups] = await Promise.all([
    loadYaml('categories.yml'),
    loadYaml('elements.yml'),
    loadYaml('groups.yml')
  ]);

  const html = await renderTemplate('src/demo/index.njk', {
    categories,
    elements,
    groups
  });

  await writeFile(path.join(destDir, 'index.html'), html, 'utf-8');
}

async function buildDemoVendor() {
  const files = await globby('**/*.css', {cwd: vendorSrcDir});

  for (const file of files) {
    const destPath = path.join(cssDestDir, file);
    await mkdir(path.dirname(destPath), {recursive: true});
    await copyFile(path.join(vendorSrcDir, file), destPath);
  }
}

await rm(destDir, {recursive: true, force: true});
await buildDemoCss();
await buildDemoPage();
await buildDemoVendor();
