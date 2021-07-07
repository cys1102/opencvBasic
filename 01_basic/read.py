import cv2 as cv

# Read images
# img = cv.imread("../Resources/Photos/cat_large.jpg")

# cv.imshow("Cat", img)
# cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture("../Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):  # if 'd' is put
        break

capture.release()
cv.destroyAllWindows()
