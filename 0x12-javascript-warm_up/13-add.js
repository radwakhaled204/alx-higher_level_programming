#!/usr/bin/node
// This script exports a function that returns the addition of 2 integers
function add (a, b) {
  // return the sum of a and b
  return a + b;
}

// Export the function as a module
module.exports = {
  // the name of the function is add
  add
};
