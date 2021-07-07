import cv2 as cv
from matplotlib.colors import hsv_to_rgb
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("park", img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("Lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# HSV to BGR
hsv_to_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSB --> BGR", hsv_to_bgr)

# L*a*b to BGR
lab_to_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("Lab --> BGR", lab_to_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
