import cv2
import numpy as np

IMAGE_LENGTH = 60
def isCloseEnough(point1, point2):
    if (point2[0]-IMAGE_LENGTH < point1[0] and point2[1]-IMAGE_LENGTH < point1[1]):
        return True
    else:
        return False

def checkCloseEnoughList(point, list):
    for prevPointIndex in range(0, len(list)):
        if (isCloseEnough(list[prevPointIndex], point)):
            return False
    return True

LETTER_ARRAY = ['A', 'E', 'I', 'O', 'U']
def analyseScreenshot(image):
    modifiedBounds = img_rgb[415:675, 375:630]

    img_gray = cv2.cvtColor(modifiedBounds, cv2.COLOR_BGR2GRAY)
    for letter in LETTER_ARRAY:
        template = cv2.imread('data/tileTemplates/' + letter + '.png', 0)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.95
        loc = np.where(res >= threshold)
        prevSearches = []
        for pt in zip(*loc[::-1]):
            if checkCloseEnoughList(pt, prevSearches):
                prevSearches.append(pt)
                #print('(', pt[0], ',', pt[1], ')')

        print("I see {} instance(s) of \'{}\'".format(len(prevSearches), letter))
    cv2.imshow('image', modifiedBounds)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img_rgb = cv2.imread('data/sampleScreenshots/sampleScreenshot.png')
analyseScreenshot(img_rgb)
