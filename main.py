import pyautogui
import time

# Docs say move top left to abort prog
pyautogui.FAILSAFE = True

print("Please enter number of count: ")
count = int(input())

contactItemCoordsDict = {
    "1920x1080": [800, 850],
    "1920x1440": [800, 1050]
}
contactExchangeButtonCoordsDict = {
    "1920x1080": [1500, 950],
    "1920x1440": [1500, 1150]
}

contactCoords = None
exchangeCoords = None

if pyautogui.size().width == 1920:
    match pyautogui.size().height:
        case 1080:
            print("Res: 1920x1080")
            contactCoords = contactItemCoordsDict["1920x1080"]
            exchangeCoords = contactExchangeButtonCoordsDict["1920x1080"]
        case 1440:
            print("Res: 1920x1440")
            contactCoords = contactItemCoordsDict["1920x1440"]
            exchangeCoords = contactExchangeButtonCoordsDict["1920x1440"]

for i in range(count):
    print("Cycle", i+1, "/", count)
    # Contact button 800, 850
    pyautogui.moveTo(contactCoords[0], contactCoords[1])
    pyautogui.click()
    time.sleep(1)
    # Exchange button 1500, 950
    pyautogui.moveTo(exchangeCoords[0], exchangeCoords[1])
    pyautogui.click()
    time.sleep(1)
