#!/usr/bin/node
// statusCode output from request

const request = require('request');

request(process.argv[2], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', data && data.statusCode);
  }
});
