#!/usr/bin/node
// Defines a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

// Import the dict from the file 101-data.js
const dict = require('./101-data').dict;

// Initialize an empty object to store the new dictionary
const newDict = {};

// Loop through the keys and values of the dict
for (const [key, value] of Object.entries(dict)) {
  // If the value is not a key in the new dictionary, create a new array with the key as an element
  if (newDict[value] === undefined) {
    newDict[value] = [key];
  } else {
    // Else, push the key to the existing array
    newDict[value].push(key);
  }
}

// Print the new dictionary at the end
console.log(newDict);
