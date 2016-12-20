var _ = require('lodash');
var cheerio = require('cheerio');
var cheerioTableparser = require('cheerio-tableparser');
var csvtojson = require('csvtojson');
var fs = require('fs');
var mkdirp = require('mkdirp');
var Promise = require('bluebird');
var yaml = require('js-yaml');

Promise.promisifyAll(fs);

var mkdirpAsync = Promise.promisify(mkdirp);

function parse() {
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
        console.log('Done!');
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
}
