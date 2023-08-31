import pyautogui
import time
import keyboard
from pystyle import Write, Colors

points = [
    (991, 877, "PRENDRE SNAP"),
    (1100, 940, "ENVOYER"),
    (978, 577, "groupe 1"),
    (979, 632, "groupe 2"),
    (972, 680, "groupe 3"),
    (1141, 943, "ENVOYER SNAP"),
]

def check_key():
    if keyboard.is_pressed("end"):
        return True
    return False

logo = """
SSSSS  N   N  A   PPPP
S      NN  N A A  P   P
SSSS   N N N AAAAA PPPP
    S  N  NN A   A P
SSSS   N   N A   A P

"""

Write.Print(logo, Colors.green_to_yellow, interval=0.02)

while True:
    if check_key():
        break
        
    for x, y, name in points:
        if check_key():
            break

        print(f"s {name}")

        pyautogui.moveTo(x, y, duration=0)

        time.sleep(0.2)

        pyautogui.click(button='left')
