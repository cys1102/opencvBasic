import cv2 as cv

# img = cv.imread("../Resources/Photos/cat_large.jpg")
# cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    # Images, Viedoes, and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)


resized_img = rescaleFrame(img)
cv.imshow("Resized_cat", resized_img)

# Reading Videos
capture = cv.VideoCapture("../Resources/Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video_resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):  # if 'd' is put
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
