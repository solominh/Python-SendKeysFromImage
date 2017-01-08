import cv2

drawing = False  # true if mouse is pressed
ix, iy = -1, -1
# mouse callback function


def draw_rect(event, x, y, flags, param):
    global ix, iy, drawing, original_image, cloned_image
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cloned_image = original_image.copy()
            cv2.rectangle(cloned_image, (ix, iy), (x, y), (0, 255, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cloned_image = original_image.copy()
        cv2.rectangle(cloned_image, (ix, iy), (x, y), (0, 255, 0), 1)


def draw_region(image):
    global original_image, cloned_image

    original_image = image
    cloned_image = image.copy()

    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        "image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('image', draw_rect)

    while(1):
        cv2.imshow('image', cloned_image)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
