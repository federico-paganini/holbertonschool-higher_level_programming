#!/usr/bin/node
import { argv } from 'node:process';

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
