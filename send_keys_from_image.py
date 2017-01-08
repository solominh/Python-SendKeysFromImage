# import pyautogui
import keyboard
import pyautogui
import cv2
from get_image_region import draw_region

screenshot_path = './screenshot.png'
pyautogui.screenshot(screenshot_path)
image = cv2.imread(screenshot_path)
ref_points = draw_region(image)
print(ref_points)


def send_keys(data):
    keyboard.write(data.strip())
    # pyautogui.typewrite(data.strip())


def main():
    send_keys(data)
    print('Send keys successfully!')
