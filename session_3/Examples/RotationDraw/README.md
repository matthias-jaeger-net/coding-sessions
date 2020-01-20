# RotationDraw.pyde

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generates a colorful visual by rotating a masked source image attached to the mouse position. This example is a part of my coding session materials: https://github.com/matthias-jaeger-net/coding-sessions. It's written in the python mode of Processing.

# Core ideas of the program
```
# Set the origin to the mouse position  
translate(mouseX, mouseY)
# Rotate by the angle
rotate(angle)
# Render the source buffer 
image(sourceBuffer, 0, 0)
# Increase the angle contiously
angle += speed

```
