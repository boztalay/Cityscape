from Tkinter import *

import random
from window import Window
from basics import Size, Point, AspectRatio, modulateValue, removeAllChildren

class WindowData():
    def __init__(self, window, origin):
        self.window = window
        self.origin = origin

class Building():
    @staticmethod
    def requestedAspectRatio():
        return AspectRatio(2.0)

    @staticmethod
    def approxNumberOfFloors():
        return 6

    def __init__(self, size):
	self.size = size

        self.generateWindows()

    def generateWindows(self):
        self.windowDatas = []

        numberOfWindowRows = int(round(modulateValue(self.approxNumberOfFloors(), 0.13)))
        windowHeight = float(self.size.height) / numberOfWindowRows

        windowWidth = Window.requestedAspectRatio.widthForHeight(windowHeight)
        numberOfWindowColumns = int(self.size.width / windowWidth)
        windowWidth += (self.size.width - (numberOfWindowColumns * windowWidth)) / numberOfWindowColumns

        windowVerticalPadding = windowHeight * Window.requestedVerticalPadding
        windowHeight -= (windowVerticalPadding * (numberOfWindowRows + 1)) / numberOfWindowRows

        windowHorizontalPadding = windowWidth * Window.requestedHorizontalPadding
        windowWidth -= (windowHorizontalPadding * (numberOfWindowColumns + 1)) / numberOfWindowColumns

        for i in range(0, numberOfWindowColumns):
            for j in range(0, numberOfWindowRows):
                windowSize = Size(windowWidth, windowHeight)
                window = Window(windowSize)

                windowX = ((i + 1) * windowHorizontalPadding + i * windowWidth)
                windowY = ((j + 1) * windowVerticalPadding + j * windowHeight)
                windowOrigin = Point(windowX, windowY)
                
                windowData = WindowData(window, windowOrigin)
                self.windowDatas.append(windowData)

    def draw(self, canvas):
        removeAllChildren(canvas)
        canvas.delete("all")
        canvas.create_rectangle(0, 0, self.size.width, self.size.height, fill="white")

        for windowData in self.windowDatas:
            window = windowData.window
            windowCanvas = Canvas(canvas, width=window.size.width, height=window.size.height, highlightthickness=0)
            windowCanvas.pack()
            windowCanvas.place(x=windowData.origin.x, y=windowData.origin.y)

            window.draw(windowCanvas)

class TallBuilding(Building):
    @staticmethod
    def requestedAspectRatio():
        return AspectRatio(3.5)

    @staticmethod
    def approxNumberOfFloors():
        return 12

class ShortBuilding(Building):
    @staticmethod
    def requestedAspectRatio():
        return AspectRatio(0.75)

    @staticmethod
    def approxNumberOfFloors():
        return 3
