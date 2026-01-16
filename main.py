import pyautogui
import time
import json

import tkinter as tk
from tkinter import ttk  # Using ttk for modern appearance
from tkinter import messagebox

from pynput.keyboard import Key, Listener

savedSpots = []

def keyPress(key):
    try:
        print(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')
        if str(key) == "Key.ctrl_l":
            print(f"Mouse position: {pyautogui.position()}")
            savedSpots.append(pyautogui.position())

def keyRelease(key):
    print(f'Key released: {key}')
    if key == Key.esc:
        # Stop listener
        return False

def trackingButtonClick():
    """Function to be called when the button is clicked."""
    print("Mouse tracking started")
    savedSpots.clear()
    # Collect events until released
    with Listener(on_press=keyPress, on_release=keyRelease) as listener:
        listener.join()
    print("Done tracking")
    # TODO: Figure out why need double messagebox to pop up
    #  If I click out of the window and click back during a mouse track, both will pop up
    messagebox.showinfo("Saved spots: ", savedSpots)
    messagebox.showinfo("Saved spots: ", savedSpots)

def trackingButtonInfoClick():
    messagebox.showinfo("Mouse tracking help", "Once started, press LEFT CONTROL to save current pointer position. Press ESCAPE to stop tracking.")

def saveButtonClick():
    with open('preset.json', 'w') as json_file:
        json.dump(savedSpots, json_file, indent=4)

# 1. Create the main window
root = tk.Tk()
root.title("Mouse clicker")
root.geometry("300x200") # width x height

widgetFrame = tk.Frame(root)
widgetFrame.pack(fill="both", expand=True)

# 2. Create the button
# The 'command' option binds the button click event to the function
trackingButton = ttk.Button(root, text="Start tracking mouse position", command=trackingButtonClick)
trackingButtonInfo = ttk.Button(root, text="Help", command=trackingButtonInfoClick)
saveButton = ttk.Button(root, text="Save preset", command=saveButtonClick)

# 3. Place the button in the window
trackingButton.pack(side="left", fill="both", expand=True) # Use a geometry manager like pack(), grid(), or place()
trackingButtonInfo.pack(side="left", fill="both", expand=True) # Use a geometry manager like pack(), grid(), or place()
saveButton.pack(fill="both", expand=True) # Use a geometry manager like pack(), grid(), or place()

# 4. Start the main event loop
root.mainloop()

# print("Please enter number of count: ")
# count = int(input())

# contactItemCoordsDict = {
#     "1920x1080": [800, 850],
#     "1920x1440": [800, 1250]
# }
# contactExchangeButtonCoordsDict = {
#     "1920x1080": [1500, 950],
#     "1920x1440": [1500, 1150]
# }

# contactCoords = None
# exchangeCoords = None

# if pyautogui.size().width == 1920:
#     match pyautogui.size().height:
#         case 1080:
#             print("Res: 1920x1080")
#             contactCoords = contactItemCoordsDict["1920x1080"]
#             exchangeCoords = contactExchangeButtonCoordsDict["1920x1080"]
#         case 1440:
#             print("Res: 1920x1440")
#             contactCoords = contactItemCoordsDict["1920x1440"]
#             exchangeCoords = contactExchangeButtonCoordsDict["1920x1440"]

# for i in range(count):
#     print("Cycle ", i, " /", count)
#     # Contact button 800, 850
#     pyautogui.moveTo(contactCoords[0], contactCoords[1])
#     pyautogui.click()
#     time.sleep(1)
#     # Exchange button 1500, 950
#     pyautogui.moveTo(exchangeCoords[0], exchangeCoords[1])
#     pyautogui.click()
#     time.sleep(1)
