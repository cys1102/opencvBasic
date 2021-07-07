import cv2 as cv

img = cv.imread("../Resources/Photos/group 1.jpg")
cv.imshow("Group 1", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average", average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian", gauss)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
