# Example 2

# Globally stored image
myImage = None

def setup():
    
    # Import the image
    global myImage
    
    # Define the sketch format
    size(900, 600)
    
    # Set the origin of the image to it's center
    imageMode(CENTER)
    
    # Load the source image
    # https://unsplash.com/photos/mGy1Jjr2e6M
    myImage = loadImage("file.jpg")

    # Skew the image to a small square
    myImage.resize(100, 100)
    
    # Clear screen with white 
    background(255)

def draw():

    # Attach the square to the mouse position
    image(myImage, mouseX, mouseY)
