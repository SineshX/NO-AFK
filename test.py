import keyboard
import time
import pyautogui
import win32gui
#todo : focus on valo in try block except exit with statement


# 10 sec loop

def function():
    while True:
        keyboard.press_and_release('enter')
        time.sleep(2)
        keyboard.press_and_release('R')
        keyboard.press_and_release('a')
        keyboard.press_and_release('m')
        time.sleep(2)
        keyboard.press_and_release('enter')
        keyboard.press('w')
        for i in range (5):
            time.sleep(1)
            if keyboard.is_pressed('q'):
                print('\nfun khatm  :(\n')
                return


if __name__ == '__main__':
    
    time.sleep(5)
    keyboard.press_and_release('enter')
    time.sleep(2)
    pyautogui.typewrite('Breach_Bot in the Chat :)')
    time.sleep(1)
    keyboard.press_and_release('R')
    keyboard.press_and_release('a')
    keyboard.press_and_release('m')
    time.sleep(2)
    keyboard.press_and_release('enter')

    # function()

       
# maja aa gaya bidu :)        
