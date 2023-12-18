#!/usr/bin/node
// This script exports a function that executes x times a function
// Define a function with the prototype: function (x, theFunction
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) { // Loop x times
    theFunction(); // Call the function passed as an argument
  }
}

module.exports = { // Export the function as a module
  callMeMoby // The name of the function is callMeMoby
};
