from Tkinter import *

import random
from building import Building

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
STREET_LEVEL = 480

BUILDING_WIDTH_LIMITS = (100, 200)
BUILDING_HEIGHT_LIMITS = (100, 450)
BUILDING_HEIGHT_DELTA_MIN = 0.1

master = Tk()
master.resizable(width=False, height=False)
canvas = Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()
random.seed()

def generateBuildings(event):
	currentBuildingStartX = random.randint(-50, -30)
	lastBuildingHeight = random.randint(BUILDING_HEIGHT_LIMITS[0], BUILDING_HEIGHT_LIMITS[1])

	buildings = []
	while (currentBuildingStartX < WINDOW_WIDTH):
		newBuildingHeight = random.randint(BUILDING_HEIGHT_LIMITS[0], BUILDING_HEIGHT_LIMITS[1])
		while (newBuildingHeight > ((1.0 - BUILDING_HEIGHT_DELTA_MIN) * lastBuildingHeight) and
			   newBuildingHeight < ((1.0 + BUILDING_HEIGHT_DELTA_MIN) * lastBuildingHeight)):
			newBuildingHeight = random.randint(BUILDING_HEIGHT_LIMITS[0], BUILDING_HEIGHT_LIMITS[1])

		newBuilding = Building((currentBuildingStartX, STREET_LEVEL),
							   ((random.randint(BUILDING_WIDTH_LIMITS[0], BUILDING_WIDTH_LIMITS[1]), newBuildingHeight)),
							   "white")
		buildings.append(newBuilding)

		currentBuildingStartX += newBuilding.size[0]
		lastBuildingHeight = newBuilding.size[1]

	canvas.delete("all")
	canvas.create_rectangle(0, 0, WINDOW_WIDTH + 2, WINDOW_HEIGHT + 2, fill="black")

	for building in buildings:
		building.draw(canvas)

generateBuildings(None)
master.bind("r", generateBuildings)
mainloop()
