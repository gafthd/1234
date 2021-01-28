import re
import pytesseract as t
import pyautogui as p

def snap(a, b, c, d):
    return p.screenshot(region = (a*2, b*2, (c - a)*2, (d - b)*2))

# string = t.image_to_string(snap(519, 135, 1386, 252)).strip()
# print(string)
# # string = 'Problems  Set 100'
# # print(re.search(r'Problems+.*\w+.\w+',string).group())

text = 'analysis\n uses Kirchhoff\xe2\x80\x99s'
# text = '<p>1. Yada yada<p>2.'
# print(re.search('<p>\d.*>\d.',text).group())
print(re.sub(r'"\"\w','',str(text)))