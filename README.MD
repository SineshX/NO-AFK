# create a no-afk bot for valorant :)

## current features :

* [X] random key input  (w,a,s,d,space,ctrl)
* [X] write lol / afk in chat

# to run :

1) install Python 
2) ``` pip install pyautogui,keyboard ```
3) ``` python main.py ```
4) test video 1 : https://youtu.be/_4jDhEqCZI4

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

### maja aa gaya bidu :)
