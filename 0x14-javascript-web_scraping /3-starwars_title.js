#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

// Import the request module
const request = require('request');

// Get the movie ID from the first argument
const movieID = process.argv[2];

// Build the URL to request using the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the URL
request.get(url, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, parse the body as JSON
    const data = JSON.parse(body);
    // Print the title of the movie in the format: <title>
    console.log(data.title);
  }
});
