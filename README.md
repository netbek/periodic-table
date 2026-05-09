# Periodic table

Periodic table with responsive layout.

## Demo

[netbek.github.io/periodic-table](https://netbek.github.io/periodic-table)

## Integration

Install the package:

```shell
npm install @netbek/periodic-table
```

Create a Sass file:

```scss
@import 'node_modules/@netbek/periodic-table/src/css/mixins';

// Define vars that should override defaults
$nb-periodic-table-cell-bg:                       #eee;
$nb-periodic-table-cell-border:                   #ccc;

// Load default vars
@import 'node_modules/@netbek/periodic-table/src/css/variables';

// Mobile-first layout
@include nb-periodic-table-base;
@include nb-periodic-table-color;
@include nb-periodic-table-size;

// Wide breakpoint layout
@media (min-width: 82em) {
  @include nb-periodic-table-color('category');
  @include nb-periodic-table-size('wide');
}
```

Create a Nunjucks template:

```html
{%- from "path/to/node_modules/@netbek/periodic-table/nunjucks/macros/nb_pt_legend.njk" import nb_pt_legend %}
{%- from "path/to/node_modules/@netbek/periodic-table/nunjucks/macros/nb_pt_table_18.njk" import nb_pt_table_18 %}
<html>
  <body>
    {% set element_columns = {
        atomic_number: 'Atomic number',
        symbol: 'Symbol',
        name: 'Name',
        atomic_mass: 'Atomic mass',
        electronegativity: 'Electronegativity'
    } %}
    {{ nb_pt_legend(elements, categories, element_columns) }}
    {{ nb_pt_table_18(elements, groups) }}
  </body>
</html>
```

Render the Nunjucks template:

```js
import nunjucks from 'nunjucks';
import periodicTable from '@netbek/periodic-table';

async function render() {
  const categories = await periodicTable.loadCategories();
  const elements = await periodicTable.loadElements();
  const groups = await periodicTable.loadGroups();

  const data = {
    categories,
    elements,
    groups
  };

  return nunjucks.render('path/to/template.njk', data);
}

render();
```

## Development: Installation

1. Install Nix:

    ```shell
    sh <(curl -L https://nixos.org/nix/install) --daemon
    ```

2. Configure Nix. Edit `/etc/nix/nix.conf` (for a multi-user installation) or `~/.config/nix/nix.conf` (for a single-user installation) to include the following lines:

    ```shell
    experimental-features = nix-command flakes
    trusted-users = root <USER>
    ```

    Replace `<USER>` with your username on your computer.

3. Install direnv:

    ```shell
    sudo apt install direnv
    ```

4. Enable direnv in your shell by adding a line to your shell configuration file.

    For Bash, edit `~/.bashrc`:

    ```shell
    eval "$(direnv hook bash)"
    ```

5. Allow `.envrc`:

    ```shell
    direnv allow
    ```

6. Enter a [PyPI API token](https://pypi.org/manage/account/#api-tokens) as the password in `.pypirc`.

## Development: Usage

Automatically build and refresh browser during development:

```shell
gulp livereload
```

Build and publish the JavaScript and Python distribution packages:

```shell
make bump-version [major|minor|patch]
git push
make build-and-commit
git push
make create-release
make publish
```

## Feature ideas

* Group and period axes
* Color by group or block; different palettes ([mendeleevapp](https://github.com/lmmentel/mendeleevapp))

## Credit

Data from [mendeleev](https://mendeleev.readthedocs.io/en/stable/bibliography.html) (MIT License)

## License

Copyright (c) 2016 Hein Bekker. Licensed under the GNU Affero General Public License, version 3.
