import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# create a binary thresholded image
_, binary = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY_INV) # i changed up the two numbers to fix the black and white of the image

# show it
plt.imshow(binary, cmap="gray")
plt.show()
