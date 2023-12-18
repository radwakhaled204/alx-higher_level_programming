#!/usr/bin/node
// Defines a function that prints the number of arguments already printed and the new argument value

// Export the function
exports.logMe = function (item) {
  // Initialize a counter variable in the function scope
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  }
  // Print the counter and the item using the format <number arguments already printed>: <current argument value>
  console.log(exports.logMe.count + ': ' + item);
  // Increment the counter
  exports.logMe.count++;
};
