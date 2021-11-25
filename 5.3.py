from tkinter import *
import tkinter.font
import time
import RPi.GPIO as GPIO
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

Code = {
'A' : '.-' ,
'B' : '-...' ,
'C' : '-.-.' ,
'D' : '-..' ,
'E' : '.' ,
'F' : '..-.' ,
'G' : '--.' ,
'H' : '....' ,
'I' : '..' ,
'J' : '.---' ,
'K' : '-.-' ,
'L' : '.-..' ,
'M' : '--' ,
'N' : '-.' ,
'O' : '---' ,
'P' : '.--.' ,
'Q' : '--.-' ,
'R' : '.-.' ,
'S' : '...' ,
'T' : '-' ,
'U' : '..-' ,
'V' : '...-' ,
'W' : '.--' ,
'X' : '-..-' ,
'Y' : '-.--' ,
'Z' : '--..'
}

LED = 7
GPIO.setup(LED, GPIO.OUT)

win = Tk()
win.title("Morse Converter")
Font_style = tkinter.font.Font( family = 'Cambaria', size = 20, weight = "bold")

def Dash_func():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.13)
    
def Dot_func():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.13)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.13)

def morse_code():
    TEXT = string_input.get()
    for alphabet in TEXT:
        for dot_dash in Code[alphabet.upper()]:
            if dot_dash == '-':
                Dash_func()
            elif dot_dash == '.':
                Dot_func()
            else:
                time.sleep(0.13)
        time.sleep(1) 

string_input = Entry(win, font = Font_style, width = 20)
string_input.grid(row = 0, column = 0)

button = Button(win, text = 'MORSE-CODE-CONVERT', font = Font_style, command = morse_code, height = 2, width = 20)
button.grid( row =0, column = 3)

win.mainloop()
                


