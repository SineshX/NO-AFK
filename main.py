from time import sleep
import sys
import keyboard 
import random
import pyautogui 
import threading


def main():

    print('\nTo end the program : press Q for 3 sec')
    print(' Starting bot in 5 sec ')
    print()
    sleep(4) # lol

    # check if valorant is active than run
    try:
        focusOnValorant()
        # came here means valo is active and chat_afk() function executed
        global bot_flag 
        bot_flag = True # will be used to terminate the bot / thread
        # creating thread || yes u can pass function XD
        t1 = threading.Thread(target = no_afk ) 
        # starting thread || calling no_afk in parallel
        t1.start()
        while bot_flag == True:
            sleep(3)
            if keyboard.is_pressed('q'):
                bot_flag = False
                return
        # end of try block        
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
        sys.exit()
    else: 
        valorant = list[0]
        if valorant.isMinimized == True:
            valorant.restore() #run
            chat_afk()
# end of focus function 

def chat_afk():
    sleep(0.5)
    keyboard.press_and_release('enter')
    sleep(1)
    pyautogui.typewrite('Im going AFK , myBot oNN :)')
    sleep(0.5)
    keyboard.press_and_release('enter')
# end of chat function

def no_afk():
    # print('hello world')
    sleep(0.5)
    while bot_flag == True:
        choice = random.randint(1,10) # 1 to 10
        sleeptime = random.randint(1,15)
        #sed lyf no switch case :(
        # W
        if choice == 1:
            keyboard.press('w')
            sleep(sleeptime)
            keyboard.release('w')
        # A
        elif choice == 2:
            keyboard.press('a')
            sleep(sleeptime)
            keyboard.release('a')
        # S
        elif choice == 3:
            keyboard.press('s')
            sleep(sleeptime)
            keyboard.release('s')
        # D
        elif choice == 4:
            keyboard.press('d')
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
            # sleep(sleeptime)
        # afk 
        elif choice == 8: 
            keyboard.press_and_release('enter')
            sleep(2)
            pyautogui.typewrite('Sorry boiz Im AFK')
            sleep(1)
            keyboard.press_and_release('enter')
            sleep(sleeptime)
        # 9) buy gun
        # 10) do something    
    #end of while loop
# end of afk function 

# ******** Main Function ********** # 
# calling main function
if __name__ == "__main__":
    main()
