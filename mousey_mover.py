import pyautogui
import random

list1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

i = 0

while(i < 5):
    x = random.choice(list1)
    y = random.choice(list2)

    pyautogui.moveTo(x, y, duration = .2)
    
    #there, no more else function. now the script is lame and weak
    
