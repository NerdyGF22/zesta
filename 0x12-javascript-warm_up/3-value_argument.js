#!/usr/bin/node
const { argv } = require('process');
if (argv[2]) {
  console.log(argv[3]);
} else {
  console.log('No argument');
}
