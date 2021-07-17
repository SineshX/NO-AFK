from itertools import dropwhile
import time
import keyboard 
import random

#sed lyf cant prototype function in python :(

def no_afk():
    print('hello world')
    time.sleep(2)

    while True:
        choice = random.randint(1,7) # 1 to 10
        sleeptime = random.randint(1,100)
        #sed lyf no switch case :(
        if choice == 1:
            keyboard.press('w')
            time.sleep(sleeptime)
            keyboard.release('w')

        elif choice == 2:
            keyboard.press('a')
            time.sleep(sleeptime)
            keyboard.release('a')

        elif choice == 3:
            keyboard.press('s')
            time.sleep(sleeptime)
            keyboard.release('s')

        elif choice == 4:
            keyboard.press('d')
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
            keyboard.press_and_release('l','o','l','space')
            keyboard.press_and_release('enter')
            time.sleep(sleeptime)

        elif choice == 8: # afk
            keyboard.press_and_release('enter')
            keyboard.press_and_release('a','f','k','space')
            keyboard.press_and_release('enter')
            time.sleep(sleeptime)
        
        if keyboard.is_pressed('q'):
            print('\nfun khatm  :(\n')
            break
    #end of while loop
# end of afk function 

# ******** Main Function ********** # 

if __name__ == "__main__":
    no_afk()


