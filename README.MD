# create a no-afk bot for valorant :)

## current features :

* [X] random key input  (w,a,s,d,space,ctrl)
* [X] write lol / afk in chat

# to run :

1) install Python
2) ```pip install pyautogui,keyboard```
3) ```python main.py```
4) test video 1 (watch my bot die XD): https://youtu.be/35IWyJW0BBk
5) anti-ban formula : try playing with a team member jo aapko report na kare 😉

# todo :

* [ ] pip install auto-py-to-exe
* [ ] and convert into exe

# future work that might not be done :_:

* [X] focus on valorant.exe : ( if running ) //done
* [ ] agent select using pyautogui
* [ ] remove keyboard module and use pyautogui only
* [ ] GUI for custom chat inputs :)
* [ ] make ML model with my mode
* [ ] make exe for noobs
* [ ] special key binding
* [ ] start with valo samall icon on somewhere
* [ ] auto afk detect :) danger zone for campers
* [ ] itni dur aa gaye ho to fork/star/kisi feature me help kr do saar :)

# End

now only trash below ..

# working with pyautogui

> list = pyautogui.getWindowsWithTitle('VALORANT')
> list
> [Win32Window(hWnd=263294)]
> valorant = list[0]
> valorant
> Win32Window(hWnd=263294)
> valorant.restore()
> : "D:\Games\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live
> pyautogui.scroll(200)
> im = pyautogui.screenshot()
> later work for gun buying etc with image and mouse :)
> im.save()

# Working with threads: 
    ```
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
    ```
### maja aa gaya bidu :)

fun fact : I'm noob in python and valo ![😅](https://static.xx.fbcdn.net/images/emoji.php/v9/tac/1.5/16/1f605.png)
