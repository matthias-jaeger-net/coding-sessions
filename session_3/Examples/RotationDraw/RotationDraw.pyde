# 
# RotationDraw.pyde
# Generates a colorful visual by spinning a masked image
# that is attached to the mouse position 
#
# Matthias Jäger | MIT, 2020
#

# Global variables

# PGraphics objects 
sourceImage = None 
sourceBuffer = None 
maskBuffer = None 

# Angle of rotation
angle = 0.0 

# Speed of rotation
speed = 0.01 

    

# Main program functions

def setup():
    # Import globals variables
    global sourceImage, sourceBuffer, maskBuffer

    # Create a square canvas
    size(800, 800)
    
    # Clear the background with white
    background(255)
    
    # Load source image and skew it to fit
    # https://unsplash.com/photos/f5Fx_B3Qc4o
    sourceImage = loadImage("image.jpg")
    sourceImage.resize(width, height)

    # Create the source buffer
    
    sourceBuffer = createGraphics(width, height)
    sourceBuffer.beginDraw()
    sourceBuffer.image(sourceImage, 0, 0)
    sourceBuffer.endDraw()
    
    # Create the mask buffer
    maskBuffer = createGraphics(width, height)
    maskBuffer.beginDraw()

    # Mask style settings
    maskBuffer.background(0)
    maskBuffer.fill(255)
    
    # Create a number of randomly positioned shapes
    for n in range(950):
        maskBuffer.ellipse(random(width), 
                        random(height), 
                        random(20), 
                        random(20))
    maskBuffer.endDraw()
    
    # Apply the mask effect to the source buffer
    sourceBuffer.mask(maskBuffer)


def draw():
    global angle
    noStroke()
    imageMode(CENTER)
    translate(mouseX, mouseY)
    rotate(angle)
    image(sourceBuffer, 0, 0)
    angle += speed
    

def keyPressed():
    # HACK to get different names
    save("out/"+str(random(1))+"RotationDraw.jpg")
