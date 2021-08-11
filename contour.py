import cv2
import numpy as np

img = cv2.imread('black_and_white_test.jpg', cv2.IMREAD_UNCHANGED)


#find contours
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#create an empty image for contours
img_contours = np.zeros(img.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (255,0,0), 3)
#save image
cv2.imwrite('contourplot.jpg',img_contours)