#!/usr/bin/node
// Defines a function that returns the reversed version of a list

// Export the function
exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  const reversed = [];
  // Loop through the list from the end to the beginning
  for (let i = list.length - 1; i >= 0; i--) {
    // Push the current element to the reversed array
    reversed.push(list[i]);
  }
  // Return the reversed array
  return reversed;
};
