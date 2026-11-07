import ghpages from 'gh-pages';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const packageDir = fileURLToPath(new URL('..', import.meta.url));
const destDir = path.join(packageDir, 'dist/demo');

ghpages.publish(destDir);
