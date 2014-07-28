from Tkinter import *

import random
from building import Building

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

master = Tk()
master.resizable(width=False, height=False)
canvas = Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()
random.seed()


def generateBuildings(event):
	numBuildings = 50
	buildings = []
	for i in range(0, numBuildings):
		newBuilding = Building((random.randint(0, WINDOW_WIDTH), random.randint(WINDOW_HEIGHT / 5, ((3 * WINDOW_HEIGHT) / 5) - 120)),
							   (random.randint(30, 70), random.randint(80, 120)),
							   "white")
		buildings.append(newBuilding)

	canvas.delete("all")
	canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="black")

	for building in buildings:
		building.draw(canvas)

master.bind("r", generateBuildings)
mainloop()
