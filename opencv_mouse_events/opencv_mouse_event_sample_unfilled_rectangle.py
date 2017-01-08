import cv2
import numpy as np
drawing = False  # true if mouse is pressed
ix, iy = -1, -1
# mouse callback function


def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, canvas, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img = canvas.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        img = canvas.copy()
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)


canvas = np.zeros((512, 512, 3), np.uint8)
img = canvas.copy()

# Set window => fullscreen or not
# cv2.namedWindow('image')
cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.setMouseCallback('image', draw_rect)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
