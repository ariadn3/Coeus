import webScraper as ws
import screenSearch as ss
import cv2


img_rgb = cv2.imread('data/sampleScreenshots/ss4.png')
output = ss.analyseScreenshot(img_rgb)
print('{} = {}'.format(output[0], output[1]))

# print(ws.getHighestScoringWord('burqa'))