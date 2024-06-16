const fs = require('fs-extra');
const path = require('path');
const Promise = require('bluebird');
const yaml = require('js-yaml');

Promise.promisifyAll(fs);

module.exports = {
  /**
   *
   * @returns {Promise}
   */
  loadCategories: function () {
    return fs
      .readFile(path.resolve(__dirname, 'data/categories.yml'), 'utf8')
      .then(function (data) {
        return Promise.resolve(yaml.load(data));
      });
  },
  /**
   *
   * @returns {Promise}
   */
  loadElements: function () {
    return fs
      .readFile(path.resolve(__dirname, 'data/elements.yml'), 'utf8')
      .then(function (data) {
        return Promise.resolve(yaml.load(data));
      });
  },
  /**
   *
   * @returns {Promise}
   */
  loadGroups: function () {
    return fs
      .readFile(path.resolve(__dirname, 'data/groups.yml'), 'utf8')
      .then(function (data) {
        return Promise.resolve(yaml.load(data));
      });
  }
};
