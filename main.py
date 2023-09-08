import tkinter
import tkinter.font
import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random
import threading

window = tkinter.Tk()

# Get window screen size
monitor_height = window.winfo_screenheight()
monitor_width = window.winfo_screenwidth()

# Macro window size
gui_width = 330
gui_height = 200

# Macro window init position
gui_init_position = str(int(monitor_width/2 - gui_width/2)) + '+' + str(int(monitor_height/2 - gui_height/2 - 100))

# Macro status variables (running=True, stopping=False)
global macro_status
macro_status = False

# ------ Widget Function ------ #
# Update macro status label
def updateMacroStatusLabel(status):
  if status == False:
    status_text = 'STOPPING'
    status_label.config(text=status_text)
  else:
    status_text = 'RUNNING'
    status_label.config(text=status_text)
  print(status_text)
  print(macro_status)

# Click start/stop button
def clickStartButton():
  startMacro(True)
def clickStopButton():
  stopMacro(False)
# ------------------------------ #

# ------ Macro Function ------ #
# Macro start/stop function
def startMacro(status):
  macro_status = status
  updateMacroStatusLabel(status)
def stopMacro(status):
  macro_status = status
  updateMacroStatusLabel(status)

# Press keyboard's key function
def pressKey(key):
  pyd.keyDown(key)
  time.sleep(0.05)
  pyd.keyUp(key)

# Find image and click function
def imgClick(files):
  imgFile = pgi.locateCenterOnScreen(files, confidence=0.8)
  if imgFile == None:
    pass
  else:
    x, y = imgFile
    x = x - random.randint(1, 20) + random.randint(1, 20)
    y = y - random.randint(1, 20) + random.randint(1, 20)
    pgi.click(x, y)
  
  # Find image and key press function
def imgKeyPress(files, key):
  imgFile = pgi.locateCenterOnScreen(files, confidence=0.8)
  if imgFile == None:
    pass
  else:
    x, y = imgFile
    x = x - random.randint(1, 20) + random.randint(1, 20)
    y = y - random.randint(1, 20) + random.randint(1, 20)
    pgi.click(x, y)
    pressKey(key)

def macro():
  while True:
    time.sleep(1)
    if macro_status == True:
      print("TEST")
      if monitor_width == 2560:
        imgKeyPress('img/ss.png', 's')
        imgClick('img/s2.png')
        imgClick('img/s3.png')
        imgClick('img/s4.png')
        imgClick('img/s5.png')
        imgClick('img/s6.png')
        imgClick('img/s7.png')
        imgKeyPress('img/sesc.png', 'esc')
        imgKeyPress('img/sskip.png', 's')
      else:
        imgKeyPress('img/fhds.png', 's')
        imgClick('fhd2.png')
        imgClick('fhd3.png')
        imgClick('fhd4.png')
        imgClick('fhd5.png')
        imgClick('fhd6.png')
        imgClick('fhd7.png')
        imgKeyPress('img/fhdesc.png', 'esc')
        imgKeyPress('img/fhdskip.png', 's')
    
# ---------------------------- #

global macro_thread
macro_thread = threading.Thread(target=macro)

window.title("FIFA4 MACRO")
window.geometry(str(gui_width)+'x'+str(gui_height)+'+'+gui_init_position)
window.resizable(False, False)

status_text = 'STOPPING'
status_font = tkinter.font.Font(family="맑은 고딕", size=16, weight='bold')
status_color = 'red'

# Generate widget
start_button = tkinter.Button(window, text='START', width=10, height=3)
stop_button = tkinter.Button(window, text='STOP', width=10, height=3)
status_label = tkinter.Label(window, text=status_text, font=status_font, foreground=status_color)
footer = tkinter.Label(window, text='Made by covy kim (programmer97@naver.com)', anchor='e')

# Widget position
start_button.grid(row=0, column=0, padx=30, pady=30)
stop_button.grid(row=0, column=1, padx=30)
status_label.grid(row=1, column=0, columnspan=2, padx=30)
footer.grid(row=2, column=0, columnspan=2, padx=30, pady=20)

# Bind function
start_button.bind("<Button-1>", startMacro)
stop_button.bind("<Button-1>", stopMacro)

macro_thread.start()

window.mainloop()