import webScraper as ws
import screenSearch as ss
import cv2
import pyautogui
import time
import os

if __name__ == '__main__':
    os.system('mode con: cols=75 lines=35')
    while True:
        try:
            additionalLetters = input('> ').lower()
        except EOFError:
            break
        if additionalLetters == '~':
            break
        pt = pyautogui.locateOnScreen('data/anchors/title.png')
        if pt is None:
            print('Window not found!')
            continue
        pyautogui.click(x=pt[0]+1, y=pt[1]+1)
        im = pyautogui.screenshot('temp.png', region=(pt[0], pt[1], 1002, 783))
        img_rgb = cv2.imread('temp.png')
        output = ss.analyseScreenshot(img_rgb)
        print('{} = {}'.format(output[0] + additionalLetters, output[1] + len(additionalLetters)- additionalLetters.count('qu')))
        print(ws.getHighestScoringWord(output[0] + additionalLetters).replace(',',''))
        os.remove('temp.png')