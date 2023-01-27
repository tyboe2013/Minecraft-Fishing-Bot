import pyautogui
import cv2
from PIL import ImageGrab
import numpy as np
from time import sleep
import keyboard
import mouse


def manage_window(title):
    title.resizeTo(800, 600)
    title.moveTo(0, 0)


def initPyAutoGUI():
    # Initialized PyAutoGUI
    # When fail-safe mode is True
    # moving the mouse to the upper-left
    # corner will abort your program. This prevents
    # locking the program up.
    pyautogui.FAILSAFE = True


def take_capture(magnification):
    mx, my = pyautogui.position()  # get the mouse cursor position
    x = mx - 5  # move to the left 5 pixels
    y = my - 5  # move up 5 pixels
    capture = ImageGrab.grab(
        bbox=(x, y, x + 30, y + 30)
    )  # get the box down and to the right 25 pixels
    arr = np.array(capture)  # convert the image to numpy array
    res = cv2.cvtColor(
        cv2.resize(
            arr,
            None,
            fx=magnification,
            fy=magnification,
            interpolation=cv2.INTER_CUBIC
        ), cv2.COLOR_BGR2GRAY
    )  # magnify the screenshot and convert to grayscale
    return res


def eat_food(food_slot_number, item_slot_number):
    food_key = f"{food_slot_number}"
    item_key = f"{item_slot_number}"
    keyboard.send(food_key)
    mouse.press(button='right')
    sleep(10)
    mouse.release(button='right')
    keyboard.send(item_key)


def autofish(tick_interval, threshold, magnification):
    pyautogui.rightClick()  # cast the fishing line
    sleep(2)
    img = take_capture(magnification)  # take initial capture
    # Once there are no black pixels in the capture:
    #     np.sum(img == 0) is looking for black pixels
    #     > threshold is the number of those pixels (0)
    # exit the loop and reel in the catch (pyautogui.rightClick()).
    # Finally, wait a second and leave the auto-fish method.
    # This will cast, wait and catch one interval. See main method
    # for looping.
    while np.sum(img == 0) > threshold:
        img = take_capture(magnification)
        sleep(tick_interval)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
    pyautogui.rightClick()
    sleep(1)


def autofish_test(tick_interval, threshold, magnification):
    pyautogui.rightClick()  # cast the fishing line
    sleep(2)
    img = take_capture(magnification)  # take initial capture
    # Once there are no black pixels in the capture:
    #     np.sum(img == 0) is looking for black pixels
    #     > threshold is the number of those pixels (0)
    # exit the loop and reel in the catch (pyautogui.rightClick()).
    # Finally, wait a second and leave the auto-fish method.
    # This will cast, wait and catch one interval. See main method
    # for looping.
    while np.sum(img == 0) > threshold:
        print("ready")
        img = take_capture(magnification)

        sleep(tick_interval)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("destroy")
            cv2.destroyAllWindows()
            break
    pyautogui.rightClick()
    sleep(1)



if __name__ == "__main__":
    print("")

