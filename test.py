import keyboard
import time


# 10 sec loop

def function():
    while True:
        keyboard.press('w')
        for i in range (10):
            time.sleep(1)
            if keyboard.is_pressed('q'):
                print('\nfun khatm  :(\n')
                return


if __name__ == '__main__':
    time.sleep(5)
    keyboard.press_and_release('R')
    keyboard.press_and_release('a')
    keyboard.press_and_release('m')

    function()
        
# maja aa gaya bidu :)        
        
        
print('\nnot success   :(\n')
