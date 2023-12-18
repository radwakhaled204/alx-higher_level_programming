#!/usr/bin/node
// This script exports a function that increments and calls a function
function addMeMaybe (number, theFunction) { // Define a function with the prototype: function (number, theFunction)
  number++; // Increment the number by one
  theFunction(number); // Call the function passed as an argument with the incremented number
}

module.exports = { // Export the function as a module
  addMeMaybe // The name of the function is addMeMaybe
};
