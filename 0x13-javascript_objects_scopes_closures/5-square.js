#!/usr/bin/node
// Defines a class Square that inherits from Rectangle

// Import the Rectangle class from 4-rectangle.js
const Rectangle = require('./4-rectangle');

// Define the class Square using the class notation and extends
class Square extends Rectangle {
  // Constructor that takes 1 argument: size
  constructor (size) {
    // Call the constructor of Rectangle using super() with size as both arguments
    super(size, size);
  }
}

// Export the class
module.exports = Square;
