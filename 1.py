import pytesseract as t
import pyautogui as p
from time import sleep

def snap(a, b, c, d):
    return p.screenshot(region = (a*2, b*2, (c - a)*2, (d - b)*2))

# image = snap(1225, 789, 1273, 826)
# print(t.image_to_string(image).strip())
print(t.image_to_string('est.png'))
# p.displayMousePosition()
