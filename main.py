from itertools import dropwhile
import time
import keyboard 
import random

from pyautogui import scroll

def main():
    print('press Q to end the program at any time !!hopefully')
    # todo : focus on valorant window
    time.sleep(5)
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('b')
    keyboard.press_and_release('o')
    keyboard.press_and_release('t')
    keyboard.press_and_release('space')
    keyboard.press_and_release('o')
    keyboard.press_and_release('N')
    keyboard.press_and_release('N')
    keyboard.press_and_release('enter')

    no_afk()
    print('fun khatm  :)')
# end of main function

def no_afk():
    # print('hello world')
    time.sleep(2)

    while True:
        choice = random.randint(1,9) # 1 to 10
        sleeptime = random.randint(1,5)
        #sed lyf no switch case :(
        if choice == 1:
            keyboard.press('w')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    return
            time.sleep(sleeptime)
            keyboard.release('w')

        elif choice == 2:
            keyboard.press('a')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    return
            time.sleep(sleeptime)
            keyboard.release('a')

        elif choice == 3:
            keyboard.press('s')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    return
            time.sleep(sleeptime)
            keyboard.release('s')

        elif choice == 4:
            keyboard.press('d')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    return
            time.sleep(sleeptime)
            keyboard.release('d')

        elif choice == 5:
            keyboard.press('space')
            time.sleep(sleeptime)
            keyboard.release('space')

        elif choice == 6:
            keyboard.press('control')
            time.sleep(sleeptime)
            keyboard.release('control')

        # lets have some fun     
        elif choice == 7: #lol
            keyboard.press_and_release('enter')
            time.sleep(2)
            keyboard.press_and_release('l')
            keyboard.press_and_release('o')
            keyboard.press_and_release('l')
            keyboard.press_and_release('enter')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    return
            time.sleep(sleeptime)

        elif choice == 8: # afk
            keyboard.press_and_release('enter')
            time.sleep(2)
            keyboard.press_and_release('a')
            keyboard.press_and_release('f')
            keyboard.press_and_release('k')
            keyboard.press_and_release('enter')
            for i in range (5):
                time.sleep(1)
                if keyboard.is_pressed('q'):
                     return
            time.sleep(sleeptime)
        
        

        
    #end of while loop
# end of afk function 

# ******** Main Function ********** # 
# calling main function
if __name__ == "__main__":
    main()