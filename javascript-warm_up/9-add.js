#!/usr/bin/node
const argv = require('process').argv;
const av = argv.slice(2);
const num1 = av[0];
const num2 = av[1];

if (num1 === undefined || num2 === undefined) {

} else {
  console.log(add(parseInt(av[0], 10), parseInt(av[1], 10)));
}

function add(a, b) {
  return a + b;
}
