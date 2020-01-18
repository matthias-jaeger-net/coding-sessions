# Example 1
 
def setup():
    # Set to the same size as the source image
    # https://unsplash.com/photos/mGy1Jjr2e6M
    size(900, 600)
    background(255)
    # Load the image pixels
    img = loadImage("file.jpg")
    img.loadPixels()
    loadPixels()
    # Draw the image pixels
    for x in range(width):
        for y in range(height):
            index = x + y * width
            current = img.get(x, y)
            #if (red(current) > blue(current)):
            #    pixels[index] = current
            if (brightness(current) < 100):
                pixels[index] = current
    updatePixels()
