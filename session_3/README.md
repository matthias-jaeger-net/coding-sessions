# Basic operations with images in Processing

### Loading and displaying an image
```python
def setup():
  image(loadImage("file.jpg"), 0, 0)
```
### Resize, store and use the image
```python
myImage = None

def setup():
  global myImage
  myImage = loadImage("file.jpg")

def draw():
  image(myImage, mouseX, mouseY)
```



#### Type any number, get the same number back
```
>>> 10
10
```

#### Type a floating point number
```
>>> 10
10
```


– Strings
– Variables
– Lists
– Functions
– Conditionals
