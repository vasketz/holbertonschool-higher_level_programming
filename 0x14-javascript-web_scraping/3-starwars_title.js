#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, id, (error, data, body) => {
  if (error) {
    return console.error(error);
  } else {
    console.log(JSON.parse(body).id);
  }
});
