#! python3
# Will nudge mouse cursor from time to time to look busy in messengers and won't let computer sleep.

import pyautogui
import time
import sys

pyautogui.FAILSAFE = False
prevCoordinates = pyautogui.position()

try:
    while True:
        if prevCoordinates != pyautogui.position():
            prevCoordinates = pyautogui.position()
            time.sleep(120)
            continue
        pyautogui.moveRel(20, 0)
        pyautogui.moveRel(-20, 0)
        pyautogui.click()
        time.sleep(120)
except KeyboardInterrupt:
    sys.exit()
