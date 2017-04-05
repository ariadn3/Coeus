import webScraper as ws
import screenSearch as ss
import cv2
import pyautogui
import time

if __name__ == '__main__':
    while True:
        input('Press enter to begin analysis')
        time.sleep(1)
        im = pyautogui.screenshot('temp.png', region=(0, 0, 1002, 783))
        img_rgb = cv2.imread('temp.png')
        output = ss.analyseScreenshot(img_rgb)
        print('{} = {}'.format(output[0], output[1]))
        print(ws.getHighestScoringWord(output[0]))