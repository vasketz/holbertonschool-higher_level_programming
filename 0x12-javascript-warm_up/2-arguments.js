#!/usr/bin/node
// this script prints if arguments are passed
const argv_process = process.argv.slice(2).length;
if (argv_process === 0) {
    console.log("No argument");
}
else {
    console.log("Argument found")
}
