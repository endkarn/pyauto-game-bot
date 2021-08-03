import pyautogui
import time
import keyboard

try:
    while True:
        if keyboard.is_pressed('q'):
            strengthen = pyautogui.locateOnScreen('strengthen.png', 0.7)
            clickpos = pyautogui.center(strengthen)
            print(str(clickpos))
            pyautogui.click(strengthen)
            pyautogui.click(clicks=15, interval=0.02, x=(clickpos.x+612), y=(clickpos.y-80))

            time.sleep(0.5)
            pyautogui.click(x=(clickpos.x + 150), y=clickpos.y)
            # pyautogui.click(pyautogui.locateOnScreen('close.png', 0.7))
            pyautogui.click(pyautogui.locateOnScreen('evo.png', 0.7))
            time.sleep(4)
            pyautogui.click(x=(clickpos.x + 150), y=(clickpos.y+15))



        if keyboard.is_pressed('e'):
            evolve = pyautogui.locateOnScreen('evolve.png', 0.7)
            clickpos = pyautogui.center(evolve)

            pyautogui.click(clickpos)
            pyautogui.click(x=(clickpos.x+250), y=(clickpos.y-255)) #select acc
            pyautogui.click(x=clickpos.x, y=(clickpos.y+75)) #upgrade with cost

            okbtn = pyautogui.locateOnScreen('sm-ok.png', 0.8)
            okpos = pyautogui.center(okbtn)
            pyautogui.click(okbtn)
            time.sleep(1)
            pyautogui.click(x=okpos.x, y=(okpos.y+130))

            # pyautogui.click(x=(clickpos.x + 250), y=(clickpos.y - 255))
            # pyautogui.click(x=(clickpos.x + 250), y=(clickpos.y - 255))

        if keyboard.is_pressed('r'):
            evolve = pyautogui.locateOnScreen('recycle.png', 0.7)
            clickpos = pyautogui.center(evolve)
            pyautogui.click(clickpos)

            pyautogui.click(x=(clickpos.x + 260), y=(clickpos.y - 300))  # select acc
            pyautogui.click(x=clickpos.x, y=(clickpos.y + 40))  # use cost
            time.sleep(0.5)
            pyautogui.click(x=(clickpos.x + 360), y=(clickpos.y - 110)) # first ok
            time.sleep(0.5)
            pyautogui.click(x=(clickpos.x + 360), y=(clickpos.y + 10))  # secound ok


        if keyboard.is_pressed('end'):
            print('Stop and Exit')
            break



        # time.sleep(0.5)
except KeyboardInterrupt:
    print('\n')