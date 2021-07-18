import keyboard
from time import sleep
from sys import exit
import pyautogui
# import win32gui
#todo : focus on valo in try block except exit with statement
# if screen pr sc match of some element

# 10 sec loop
def main():
    print()
    checkValo() #get hWnd=263294 something like that
    


    print('\n#Done#')
    
def checkValo():
    list = pyautogui.getWindowsWithTitle('VALORANT')
    if len(list) == 0 :
        print('Valorant is Not active')
        print('Exiting in 5 sec .....')
        sleep(5)
        exit(0)
    else:
        valorant = list[0]
        if valorant.isMinimized == True:
            valorant.restore()
            chat()



    
def chat():
    sleep(3.5)
    keyboard.press_and_release('enter')
    sleep(2)
    pyautogui.typewrite('Breach_Bot in the Chat :)')
    sleep(1)
    keyboard.press_and_release('enter')

    pyautogui.scroll(200)
    # im = pyautogui.screenshot()
    # later work for gun buying etc with image and mouse :)
    # im.save()

    keyboard.press_and_release('enter')
    sleep(1)
    keyboard.press_and_release('R')
    keyboard.press_and_release('a')
    keyboard.press_and_release('m')
    sleep(1)
    keyboard.press_and_release('enter')

def function():
    while True:
        keyboard.press_and_release('enter')
        sleep(2)
        keyboard.press_and_release('R')
        keyboard.press_and_release('a')
        keyboard.press_and_release('m')
        sleep(2)
        keyboard.press_and_release('enter')
        keyboard.press('w')
        for i in range (5):
            sleep(1)
            if keyboard.is_pressed('q'):
                print('\nfun khatm  :(\n')
                return

    
# "D:\Games\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live
main()      
# maja aa gaya bidu :)        
