#!/usr/bin/node
// Defines class Rectangle

class Rectangle {
  // Constructor that takes 2 arguments w and h
  constructor (w, h) {
    // check if w and h are positive int
    if (w > 0 && h > 0) {
      // Initialize the instance attribute width with the value of w
      this.width = w;
      // Initialize the instance attribute height with the value of h
      this.height = h;
    }
  }
}

// Export the class
module.exports = Rectangle;
