import pyautogui
import time
import keyboard

try:
    cur_mouse = pyautogui.position()
    c_round = 0


    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond, grayscale=True)
        if imageLocation is not None:
            print('Click Image "' + lable + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()

            if lable == 'Result Screen':
                global c_round
                c_round = c_round + 1
                print('Cur Round ' + str(c_round))



    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('end'):
            print('Stop and Exit')
            break

        if c_round > 250:
            print('Completed Round' + c_round)
            break

        # findAndClick('ticket.png', 0.7, 'Start with Ticket')
        # findAndClick('purchase-tickets.png', 0.7, '1 Orb = 5 Tickets')
        # findAndClick('tap-screen.png', 0.8, 'Tap Screen')
        # findAndClick('result-screen.png', 0.8, 'Result Screen')
        # findAndClick('tap-screen.png', 0.8, 'Tap Screen')
        # findAndClick('close.png', 0.8, 'Close Reward')
        # findAndClick('retry.png', 0.8, 'Retry Quest')

        findAndClick('collect-all.png', 0.8, 'Collect Reward')
        time.sleep(1)
        findAndClick('ok.png', 0.9, 'OK')
        time.sleep(3)
        findAndClick('close.png', 0.8, 'Close Reward')
        time.sleep(3)

        time.sleep(1)
except KeyboardInterrupt:
    print('\n')
