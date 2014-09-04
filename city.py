from Tkinter import *

import random
from building import Building
from basics import Point, Size, AspectRatio, modulateValue, removeAllChildren

STREET_LEVEL_FACTOR = 0.8
BUILDING_WIDTH_FACTOR = 0.1

class BuildingData():
    def __init__(self, building, origin):
        self.building = building
	self.origin = origin

class City():
    def __init__(self, size):
        self.size = size
        self.streetLevel = int(self.size.height * STREET_LEVEL_FACTOR)
	self.approxBuildingWidth = self.size.width * BUILDING_WIDTH_FACTOR
		
	self.generateBuildings()

    def generateBuildings(self):
	self.buildingDatas = []

	currentBuildingX = int(-random.random() * self.approxBuildingWidth)

	while (currentBuildingX < self.size.width):
            buildingWidth = int(modulateValue(self.approxBuildingWidth, 0.25))
            buildingHeight = int(modulateValue(Building.requestedAspectRatio.heightForWidth(buildingWidth), 0.1))
            buildingSize = Size(buildingWidth, buildingHeight)
            building = Building(buildingSize)

            buildingOrigin = Point(currentBuildingX, self.streetLevel - buildingHeight)

            buildingData = BuildingData(building, buildingOrigin)
            self.buildingDatas.append(buildingData)

            currentBuildingX += buildingWidth

    def draw(self, canvas):
        removeAllChildren(canvas)
        canvas.delete("all")
	canvas.create_rectangle(0, 0, self.size.width, self.size.height, fill="black")

	for buildingData in self.buildingDatas:
            building = buildingData.building
            buildingCanvas = Canvas(canvas, width=building.size.width, height=building.size.height, highlightthickness=0)
            buildingCanvas.pack()
            buildingCanvas.place(x=buildingData.origin.x, y=buildingData.origin.y)

            buildingData.building.draw(buildingCanvas)
