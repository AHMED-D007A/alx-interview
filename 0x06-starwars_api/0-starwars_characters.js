#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const characterNames = [];
    let count = 0;
    characters.forEach((character, index) => {
      request(character, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          characterNames[index] = JSON.parse(body).name;
          count++;
          if (count === characters.length) {
            characterNames.forEach(name => console.log(name));
          }
        }
      });
    });
  }
});
