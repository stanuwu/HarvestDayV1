from python_imagesearch.imagesearch import imagesearch
import pyautogui
import time


### center ###
centerX = 500
centerY = 800

moveX = 1478
moveY = 199

oPos = None


def findSilo():
    return imagesearch("./sample/silo.png")


def relocate(x, y):
    diffX = moveX - x
    diffY = moveY - y
    nointstat()
    moveTo(centerX, centerY)
    pyautogui.drag(diffX, diffY, 1)
    nointstop()


def nointstat():
    oPos = pyautogui.position()


def nointstop():
    if oPos != None:
        moveTo(oPos.x, oPos.y)


def moveTo(x, y):
    pos = pyautogui.position()
    diffX = x - pos.x
    diffY = y - pos.y
    pyautogui.move(diffX, diffY, 1)


def tryCenter():
    loc = findSilo()
    if loc[0] != -1 and (loc[0] != moveX or loc[1] != moveY):
        relocate(loc[0], loc[1])


### farm ###
wheatDF = 25


def collect():
    pos = imagesearch("./sample/sicle.png")
    if pos[0] != -1:
        moveTo(pos[0], pos[1])
        pyautogui.mouseDown()

        loc = [centerX, centerY]
        while loc[0] != -1:
            loc = findNext(0.2)
            if loc[0] != -1:
                moveTo(loc[0], loc[1])
                pyautogui.move(0, wheatDF, 0.2)
                pyautogui.move(0, -100, 0.2)
                pyautogui.move(0, 200, 0.2)
                pyautogui.move(0, -100, 0.2)
                pyautogui.move(100, 0, 0.2)
                pyautogui.move(-200, 0, 0.2)

        pyautogui.mouseUp()


def findNext(x):
    for i in range(round(x*100)):
        loc = imagesearch("./sample/wheat.png", 0.4)
        time.sleep(x/100)
        if loc[0] != -1:
            return loc
    return [-1, -1]


def farmWheat():
    pos = [centerX, centerY]
    while True:
        pos = imagesearch("./sample/wheat.png", 0.7)
        if pos[0] != -1:
            break
    moveTo(pos[0], pos[1]+wheatDF)
    pyautogui.click()
    collect()
    print(pos)


### loop ###
print("started...")
while True:
    farmWheat()
    time.sleep(5)
