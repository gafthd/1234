import pyautogui as p
from time import sleep
import re
import pytesseract as t

def snap(a, b, c, d):
    # p.screenshot(region = (a*2, b*2, (c - a)*2, (d - b)*2)).save('meow2.png')
    return p.screenshot(region = (a*2, b*2, (c - a)*2, (d - b)*2))

def bookmark(text):
    if re.search(text, string) is not None:
        x = re.search(text,string).span()
        p.hotkey('command', 'd')
        sleep(.5)
        p.write(string[x[0]:x[1]])
        sleep(.5)
        p.press('enter')
        p.click(x = 580, y = 45)
        sleep(0.5)

while True:
    import pytesseract as t
    p.click(x=1000, y=399)
    string = t.image_to_string(snap(519, 135, 1386, 252)).strip()
    try:
        bookmark('Solutions.\w+.Set.\w+')
        bookmark('Problems+.*Set.\w+')
        p.press('right')
        continue
    except Exception:
        print('match not found')
        p.press('right')
        continue


# string = t.image_to_string(snap(519, 135, 1386, 252)).strip()
# print(s('Solutions.to.Set.[0-9][0-9]'))
# string = 'Solutions to Set 1'
# if re.search('Solutions.to.Set.[1-9]?\d|100',string) is not None:
#     x = re.search('Solutions.to.Set.[1-9]?\d|100',text)
#     print(x)