#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, parse the body as JSON
    const data = JSON.parse(body);
    // Initialize an empty object to store the results
    const results = {};
    // Loop through the data array
    for (const task of data) {
      // Get the user id and the completed status of each task
      const userId = task.userId;
      const completed = task.completed;
      // If the task is completed
      if (completed) {
        // If the user id is already in the results object, increment the count
        if (results[userId]) {
          results[userId]++;
        } else {
          // Otherwise, initialize the count to 1
          results[userId] = 1;
        }
      }
    }
    // Print the results object
    console.log(results);
  }
});
