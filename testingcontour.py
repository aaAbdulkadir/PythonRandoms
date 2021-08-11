# import the Python Image processing Library
from PIL import Image
from pylab import *

# Create an Image object from an Image
imageObject = Image.open("image.jpg")

# Crop image to get rid of background interruptions
cropped = imageObject.crop((500,0,750,500))

# read image to array
im = array(cropped.convert('L'))

# create a new figure
figure()

# show contours with origin upper left corner
contour(im, levels=[90], colors='black', origin='image')
axis('equal')

show()