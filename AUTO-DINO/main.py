import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time
def press(key):
    pyautogui.keyDown(key)

def danger(data):
    for i in range(250,325):
        for j in range(400,500):
            if(data[i,j]>60):
                return True
    return False


if __name__ == "__main__":
    time.sleep(3)
    press("up")
    while(True):
        image = ImageGrab.grab().convert('L')
        data=image.load()
        if danger(data):
            press("up")
    # print(asarray(image))
    # for i in range(250,325):
    #     for j in range(400,525):
    #         data[i, j] = 0
    # image.show()
