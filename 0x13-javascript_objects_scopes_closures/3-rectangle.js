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

  // Instance method called print() that prints the rectangle using the character
  print () {
    // loop through the height
    for (let i = 0; i < this.height; i++) {
      // print a row of x characters with the length of the w
      console.log('X'.repeat(this.width));
    }
  }
}

// Export the class
module.exports = Rectangle;
