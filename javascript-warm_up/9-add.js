#!/usr/bin/node
const argv = require('process').argv;
const av = argv.slice(2)

function add(a, b) {
  return a + b;
}

console.log(add(av[0], av[1]));