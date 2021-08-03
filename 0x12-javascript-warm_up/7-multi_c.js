#!/usr/bin/node
// script that prints x times C is fun
const args = process.argv.slice(2);
const lang = 'C is fun';
let i = 0;
if (isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  while (i < args) {
    console.log(lang);
    i++;
  }
}
