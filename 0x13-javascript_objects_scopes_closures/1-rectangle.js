#!/usr/bin/node
// Defines a class Rectangle

class Rectangle {
  // Constructor that takes 2 arguments w and h
  constructor (w, h) {
    // initialize the instance attribute width with the valuew of w
    this.width = w;
    // initialize the instance attribute height with the valuew of h
    this.height = h;
  }
}

// Export the class
module.exports = Rectangle;
