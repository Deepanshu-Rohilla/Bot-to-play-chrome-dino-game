import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time
def press(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

if __name__ == "__main__":
    time.sleep(1)
    image = takeScreenshot()
    data=image.load()
    print(asarray(image))
    for i in range(34,45):
        for j in range(45,67):
            data[i, j] = 0
    image.show()
