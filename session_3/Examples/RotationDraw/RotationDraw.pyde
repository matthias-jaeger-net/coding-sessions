# RotationDraw.pyde
#
# Generates a colorful visual by rotating a masked
# source image attached to the mouse position.
# 
# This example is a part of my coding session materials: 
# https://github.com/matthias-jaeger-net/coding-sessions
#
# Matthias Jäger | MIT, 2020


# GLOBAL VARIABLES

# PGraphics objects, assigned in setup()
sourceBuffer = None
maskBuffer = None

# Angle of rotation starts at 0
angle = 0.0

# Speed of rotation is slow
speed = 0.01


# CUSTOM FUNCTIONS

# – The source image 
#
def createSourceBuffer(w, h, path):

    # Load source image 
    img = loadImage(path)
    
    # Skew it to fit (brutal)
    img.resize(w, h)

    # Create the source buffer width the image
    buffer = createGraphics(w, h)
    buffer.beginDraw()
    buffer.image(img, 0, 0)
    buffer.endDraw()
   
    # Done, return the buffer 
    return buffer


# - The masked image
#
def createMaskBuffer(w, h, n, r):
    
    # Create a PGraphicsbuffer 
    buffer = createGraphics(w, h)
    
    # Wrapping all drawing inside beginDraw/endDraw
    buffer.beginDraw()
    
    # Mask alpha settings 
    # Black (0, 0, 0) –> tansparent
    # White (255, 255, 255) -> opaque
    buffer.background(0)
    buffer.fill(255)
    
    # Randomly positioned ellipses
    for t in range(n):
        x = random(w)
        y = random(h)
        buffer.ellipse(x, y, random(r), random(r))
    
    # End drawing to the buffer
    buffer.endDraw()
    
    # Done, return the buffer
    return buffer


# PROCESSING FUNCTIONS

# – setup() gets called once at program start
#
def setup():

    # Import globals variables
    global sourceBuffer

    # Create a square canvas
    size(800, 800)

    # Set the origin of images to the center (default CORNER)
    imageMode(CENTER)

    # Clear the background with white
    background(255)
    
    # Create a PGraphics buffer w x h, filled with a streched image 
    sourceBuffer = createSourceBuffer(width, height, "image.jpg")

    # Create a PGraphics buffer with 200 shapes and 20x20 maximum size
    maskBuffer = createMaskBuffer(width, height, 200, 20)

    # Apply the mask to the source buffer
    sourceBuffer.mask(maskBuffer)
    
    
# – draw() is looping until the program is ended
#
def draw():

    # Import the global variables
    global angle

    # Relocate the origin (0, 0) to the mouse 
    translate(mouseX, mouseY)
    
    # Rotate by the angle (gets increased later)
    rotate(angle)
    
    # Render the finished source buffer in an image
    image(sourceBuffer, 0, 0)
    
    # Increase the angle contiously
    angle += speed


# – keyPressed() used to save images, any key works
#
def keyPressed():
    
    # HACK to get different names
    hack = str(random(1)) 
    
    # Saves a jpg in the out folder
    save("out/"+hack+"RotationDraw.jpg")
