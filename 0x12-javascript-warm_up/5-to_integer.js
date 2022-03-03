#!/usr/bin/node
const { argv } = require('process');
if (parseInt(argv[2])) {
  console.log(parseInt(argv[2]));
} else {
  console.log('Not a number');
}
