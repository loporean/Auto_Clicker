# autoclicker program

import pyautogui
import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
import threading
import random

window = Tk()
window.geometry("300x200")
window.title("Autoclicker")



# go is initially true for while loop
go = True

def toggleReset():
    if B1['state'] == DISABLED:
        B1['state'] = NORMAL
    else:
        B1['state'] = DISABLED

def resetButton():
    B1['text'] = 'Reset'
    toggleReset()

def startButton():
    B1['text'] = 'Start'

def thread():
    resetButton()
    t1=threading.Thread(target=Start)
    t1.start()
    


def Start():
    # imports listeners for both the mouse and keyboard
    from pynput.mouse import Listener as Listener
    from pynput.keyboard import Listener as KeyListener, Key 

    

    def on_press(key):
        # declare go as global
        global go
        # if 'esc' key is pressed, then stop both listener
        # and key_listener and set go to False
        # after listener and key_listener are both stopped,
        # the program will exit form the event listeners and continue 
        # on to check if go is True or False
        # if go is still True, then the clicker function will run
        if key == Key.esc:
            listener.stop()
            key_listener.stop()
            go = False
            toggleReset()
            startButton()
            return


    def on_move(x, y):
        print(x, y)

    # listen for mouse clicks
    def on_click(x, y, button, pressed):
        # global variables to access coordinates outside of listener
        global X
        global Y
        X = x
        Y = y
        print(x, y, button, pressed)
        # if left click, then stop listener
        if pressed and button.name == 'left':
            listener.stop()
            key_listener.stop()

    def on_scroll(x, y, dx, dy):
        print(x, y, dx, dy)


    def likes500(n):
        # sensitivity to determine how much movement is allowed until clicker is paused
        sensitivity = 10
        count = 0
        # record position of mouse before running loop
        current_x, current_y = pyautogui.position()
        pyautogui.PAUSE=0.001
        check = None
        for i in range(n):
            """ check = pyautogui.locateOnScreen('goldCookie.png', confidence=0.6)
            if check != None:
                pyautogui.click(check)
                check = None """
            
            # monitor position of mouse in each iteration of loop
            new_x, new_y = pyautogui.position()
            # if 'esc' is pressed, then return from function and loop back to top
            if keyboard.is_pressed('Esc'):
                return
            # if initial position - current position is greater than the set sensitivity,
            # go into while loop to pause clicks until the 'q' or 'esc' key is pressed
            if abs(new_x - current_x) > sensitivity or abs(new_y - current_y) > sensitivity:
                toggleReset()
                while 1:
                    #time.sleep(0.005)
                    time.sleep(0.001)
                    # if 'q' is pressed, then return back to previous autoclicker position
                    if keyboard.is_pressed('q'):
                        toggleReset()
                        break
                    # if 'esc' is pressed, then return from function and loop back to top
                    if keyboard.is_pressed('Esc'):
                        return
                
            pyautogui.click(X, Y)
            #time.sleep(0.1)
            count += 1
            print(count)
    while go:
        with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            with KeyListener(on_press=on_press) as key_listener:
                listener.join()
                key_listener.join()
        # if go is set to False,
        # then break from while loop
        if not go:
            return

        likes500(100)

# Buttons setup
B1 = Button(window, text="Start", activebackground="green", font="Helvetica", width=10, command = thread)
#B2 = Button(window, text="Stop", activebackground="red", font="Helvetica", width=10, command = threading)
B1.pack()
#B2.pack()
B1.place(relx=0.5, rely=0.3, anchor=CENTER)
#B2.place(relx=0.5, rely=0.6, anchor=CENTER)

# looped window
window.mainloop()
