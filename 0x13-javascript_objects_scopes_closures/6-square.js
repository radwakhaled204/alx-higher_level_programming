#!/usr/bin/node
// Defines a class Square that inherits from Square

// Import the Square class from 5-square.js
const Square5 = require('./5-square');

// Define the class Square using the class notation and extends
class Square extends Square5 {
  // Instance method called charPrint(c) that prints the rectangle using the character c
  charPrint (c) {
    // If c is undefined, use the character X
    if (c === undefined) {
      c = 'X';
    }
    // Loop through the height
    for (let i = 0; i < this.height; i++) {
      // Print a row of c characters with the length of the width
      console.log(c.repeat(this.width));
    }
  }
}

// Export the class
module.exports = Square;
