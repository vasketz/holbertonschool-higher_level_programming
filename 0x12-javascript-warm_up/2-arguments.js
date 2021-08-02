#!/usr/bin/node
// this script prints if arguments are passed
const argvProcess = process.argv.slice(2).length;
if (argvProcess === 0) {
  console.log('No argument');
} else if (argvProcess === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
