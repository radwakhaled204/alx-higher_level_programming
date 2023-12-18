#!/usr/bin/node
// Defines a function that returns the number of occurrences in a list

// Export the function
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter variable
  let count = 0;
  // Loop through the list
  for (let i = 0; i < list.length; i++) {
    // If the current element is equal to the searchElement, increment the counter
    if (list[i] === searchElement) {
      count++;
    }
  }
  // Return the counter
  return count;
};
