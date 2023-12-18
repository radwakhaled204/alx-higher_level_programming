#!/usr/bin/node
// Defines a class Rectangle

class Rectangle {
  // Constructor that takes 2 arguments: w and h
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      // Initialize the instance attribute width with the value of w
      this.width = w;
      // Initialize the instance attribute height with the value of h
      this.height = h;
    }
  }

  // Instance method called print() that prints the rectangle using the character X
  print () {
    // Loop through the height
    for (let i = 0; i < this.height; i++) {
      // Print a row of X characters with the length of the width
      console.log('X'.repeat(this.width));
    }
  }

  // Instance method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    // Swap the values of width and height using destructuring assignment
    [this.width, this.height] = [this.height, this.width];
  }

  // Instance method called double() that multiples the width and the height of the rectangle by 2
  double () {
    // Multiply the width and height by 2 using the *= operator
    this.width *= 2;
    this.height *= 2;
  }
}

// Export the class
module.exports = Rectangle;
