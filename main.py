from time import sleep
from sys import exit
import keyboard 
import random
import pyautogui 

def main():

    print('\nTo end the program : press Q for 3 sec')
    # print('\nTo end the program : press Q while bot is moving !!hopefully')
    print(' Starting bot in 5 sec ',end='')
    for i in range(4): #lol
        sleep(1)
        print('. ',end='')
    # check if valorant is active than run
    try:
        focusOnValorant()
        no_afk()
    except:
        print()
        # thinking...

    print('\n       THATS DONE!!    ')

# end of main function

def focusOnValorant():
    # get list of active windows with name = VALORANT
    list = pyautogui.getWindowsWithTitle('VALORANT')
    # check 
    if len(list) == 0 :
        print('\n   Valorant is Not active')
        print('Exiting in 5 sec ',end='')
        for i in range(4): #lol
            sleep(1)
            print('. ',end='')
        exit(0)
    else: 
        valorant = list[0]
        if valorant.isMinimized == True:
            valorant.restore() #run
            chat()
# end of focus function 

def chat():
    sleep(3)
    keyboard.press_and_release('enter')
    sleep(2)
    pyautogui.typewrite('Im going AFK , myBot oNN :)')
    sleep(1)
    keyboard.press_and_release('enter')
# end of chat function

def no_afk():
    # print('hello world')
    sleep(0.5)
    while True:
        choice = random.randint(1,10) # 1 to 10
        sleeptime = random.randint(1,5)
        #sed lyf no switch case :(
        # W
        if choice == 1:
            keyboard.press('w')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                    return
            sleep(sleeptime)
            keyboard.release('w')
        # A
        elif choice == 2:
            keyboard.press('a')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                    return
            sleep(sleeptime)
            keyboard.release('a')
        # S
        elif choice == 3:
            keyboard.press('s')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                    return
            sleep(sleeptime)
            keyboard.release('s')
        # D
        elif choice == 4:
            keyboard.press('d')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                    return
            sleep(sleeptime)
            keyboard.release('d')
        # jump
        elif choice == 5:
            keyboard.press('space')
            sleep(sleeptime)
            keyboard.release('space')
        # crouch
        elif choice == 6:
            keyboard.press('control')
            sleep(sleeptime)
            keyboard.release('control')

        # lets have some fun 
        # lOL    
        elif choice == 7: #lol
            keyboard.press_and_release('enter')
            sleep(1)
            pyautogui.typewrite(' LOL :)')
            sleep(2)
            keyboard.press_and_release('enter')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                    return
            sleep(sleeptime)
        # afk 
        elif choice == 8: 
            keyboard.press_and_release('enter')
            sleep(2)
            pyautogui.typewrite('Sorry boiz Im AFK')
            sleep(1)
            keyboard.press_and_release('enter')
            for i in range (5):
                sleep(1)
                if keyboard.is_pressed('q'):
                     return
            sleep(sleeptime)
        # 9) buy gun
        # 10) do something    
    #end of while loop
# end of afk function 

# ******** Main Function ********** # 
# calling main function
if __name__ == "__main__":
    main()