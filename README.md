# Periodic table

Periodic table with responsive layout.

## Demo

[netbek.github.io/periodic-table](https://netbek.github.io/periodic-table)

## Integration

Install the packages:

```shell
npm install @netbek/periodic-table
pip install netbek-periodic-table
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

Create a Jinja template:

```jinja
{%- from "nb_pt_legend.jinja2" import nb_pt_legend %}
{%- from "nb_pt_table_18.jinja2" import nb_pt_table_18 %}
<!DOCTYPE html>
<html>
  <body>
    {{ nb_pt_legend(elements, categories, element_columns) }}
    {{ nb_pt_table_18(elements, groups) }}
  </body>
</html>
```

Render the Jinja template:

```python
from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PackageLoader

from netbek.periodic_table import data

env = Environment(
    loader=ChoiceLoader(
        [
            FileSystemLoader("path/to/templates"),
            PackageLoader("netbek.periodic_table", "jinja/macros"),
        ]
    ),
    autoescape=True,
    # Required by nb_pt_legend.jinja2
    extensions=["jinja2.ext.do"],
)

template = env.get_template("template.jinja2")
html = template.render(
    categories=data.categories,
    elements=list(data.elements.values()),
    groups=data.groups,
    element_columns=data.element_columns,
)
```

## Development: Installation

1. Clone the repo:

    ```shell
    git clone git@github.com:netbek/periodic-table.git
    ```

2. Install Mise and add activation to `~/.bashrc`, e.g.

    ```shell
    curl -fsSL https://github.com/jdx/mise/releases/download/v2026.7.13/install.sh | sh
    ```

    See [other installation methods](https://mise.en.dev/installing-mise.html).

3. Trust `mise.toml`:

    ```shell
    mise trust
    ```

4. Create a [PyPI API token](https://pypi.org/manage/account/#api-tokens), and add the token to the system keyring as the password:

    ```shell
    keyring set pypi-periodic-table __token__
    ```

## Development: Usage

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
