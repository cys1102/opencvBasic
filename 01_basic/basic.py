import cv2 as cv

img = cv.imread("../Resources/Photos/lady.jpg")
cv.imshow("Lady", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilate", dilated)

# Erodings
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
