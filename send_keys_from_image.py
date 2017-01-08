
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
        return False

    # Save cropped image
    cropped_image = image[ref_points['topleft'][1]:ref_points['bottomright'][1],
                          ref_points['topleft'][0]:ref_points['bottomright'][0]]
    cv2.imwrite(screenshot_path, cropped_image)

    # Convert image to text
    text_ouput_path = './text_from_image'
    call(["tesseract", screenshot_path, text_ouput_path])

    return True


def send_keys():
    with open('./text_from_image.txt') as f:
        first_time = True
        for line in f:
            cleaned_line = line.strip()
            if first_time:
                first_time = False
            else:
                cleaned_line = ' ' + cleaned_line
            print(cleaned_line)
            keyboard.write(cleaned_line)
