#!/usr/bin/node
// this script prints the value pased throught argv
const args = process.argv[2];
if (!args) {
  console.log('No arguments');
} else {
  console.log(args);
}
