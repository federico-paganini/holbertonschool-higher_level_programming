#!/usr/bin/node
const argv = require('process').argv

const av = argv.slice(2);

if (av.length < 1) {
    return console.log('No argument');
};

if (av.length === 1) {
    return console.log('Argument found');
};

if (av.length > 1) {
    return console.log('Arguments found');
};
