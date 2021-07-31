import pyautogui
import time
import keyboard
import random

isFightScene = False

def randomSpecialMove():
    number = random.randint(3, 9)
    if isFightScene:
        if number > 6:
            pyautogui.press('r')
            print('Used Special Move')
            time.sleep(3)
            pyautogui.press('r')



try:
    cur_mouse = pyautogui.position()


    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond)
        if imageLocation is not None:
            print('Click Image "' + lable + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()

            if lable == 'Fight Auto':
                global isFightScene
                isFightScene = True

            if lable == 'SKip Friends':
                isFightScene = False

            # if lable == 'Room Closed':
            #     searchAgain()

        elif lable == 'Select Room':
            searchAgain()


    def searchAgain():
        findAndClick('search-again.png', 0.8, 'Search Again')
        time.sleep(3)

    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('q'):
            print('Stop and Exit')
            break

        # Resolution Windows 1024x576
        findAndClick('main-btn.png', 0.7, 'Jidanbo Raid')
        findAndClick('hard-mode.png', 0.7, 'Select Hard')
        findAndClick('join.png', 0.8, 'Join Rooms')
        findAndClick('okable.png', 0.7, 'Select Room')
        findAndClick('ready.png', 0.7, 'Ready')
        findAndClick('fight-auto.png', 0.9, 'Fight Auto')
        findAndClick('friends.png', 0.75, 'SKip Friends')
        findAndClick('retry.png', 0.8, 'Retry')
        findAndClick('room-closed.png', 0.8, 'Room Closed')
        findAndClick('revive.png', 0.8, 'Revive')

        randomSpecialMove()

        time.sleep(0.1)
except KeyboardInterrupt:
    print('\n')
