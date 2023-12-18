#!/usr/bin/node
// Defines a function that converts a number from base 10 to another base

// Export the function
exports.converter = function (base) {
  // Return a function that takes a number as an argument
  return function (number) {
    // Convert the number from base 10 to the given base using the toString() method
    return number.toString(base);
  };
};
