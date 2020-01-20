# RotationDraw.pyde

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generates a colorful visual by rotating a masked source image attached to the mouse position. This example is a part of my coding session materials: https://github.com/matthias-jaeger-net/coding-sessions. It's written in the python mode of Processing.

# Core idea of the program
The program loads the pixels of a given image into a graphics buffer, then applies an alpha mask with a large number of randomly placed white shapes on a black background, leaving only parts of the original image visible. Not calling ``background(255)`` inside of the draw loop traces a colorful path around the mouse position.

# Output images
![session](out/0.118021726608RotationDraw.jpg)


## Learning goals
- Learn to load, resize and display images in Processing 
- Learn to create graphics buffers and apply alpha masks 
- Learn to animate the masked image in draw
- Learn save the images you draw 
