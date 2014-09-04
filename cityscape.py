from Tkinter import *

import random
from city import City
from basics import Size, removeAllChildren

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

master = Tk()
master.resizable(width=False, height=False)

random.seed()

def generateCity(event):
    removeAllChildren(master)

    citySize = Size(WINDOW_WIDTH, WINDOW_HEIGHT)
    city = City(citySize)

    cityCanvas = Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0)
    cityCanvas.pack()

    cityCanvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="black")
    city.draw(cityCanvas)

def quit(event):
    master.quit()

generateCity(None)

master.bind("r", generateCity)
master.bind("q", quit)
mainloop()
