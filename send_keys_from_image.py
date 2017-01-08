
import keyboard
import pyautogui
import cv2
from get_image_region import draw_region
from subprocess import call


def main():
    # Take screenshot
    screenshot_path = './screenshot.png'
    pyautogui.screenshot(screenshot_path)

    # Draw image region
    image = cv2.imread(screenshot_path)
    ref_points = draw_region(image)
    print(ref_points)

    # Sanity check
    if not ref_points:
        print('Region not selected')
        return

    # Save cropped image
    cropped_image = image[ref_points['topleft'][1]:ref_points['bottomright'][1],
                          ref_points['topleft'][0]:ref_points['bottomright'][0]]
    cv2.imwrite(screenshot_path, cropped_image)

    # Convert image to text
    text_ouput_path = './text_from_image'
    call(["tesseract", screenshot_path, text_ouput_path])

    # Open result file
    with open(text_ouput_path + '.txt') as f:
        print(f)
        # keyboard.write(data.strip())
