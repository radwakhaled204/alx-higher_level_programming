#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.

// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Define the character ID of Wedge Antilles
const wedgeId = 18;

// Make a GET request to the API URL
request.get(apiUrl, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, parse the body as JSON
    const data = JSON.parse(body);
    // Initialize a counter for the number of movies
    let count = 0;
    // Loop through the results array
    for (const movie of data.results) {
      // Loop through the characters array of each movie
      for (const character of movie.characters) {
        // If the character URL contains the wedgeId, increment the count
        if (character.includes(wedgeId)) {
          count++;
        }
      }
    }
    // Print the count of movies
    console.log(count);
  }
});
