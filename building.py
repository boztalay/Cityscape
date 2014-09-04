from Tkinter import *

import random
from window import Window

APPROX_WINDOW_WIDTH = 40.0
APPROX_WINDOW_HEIGHT = 60.0
WINDOW_BUFFER = 8.0

class Building():
	def __init__(self, origin, size, color):
		self.origin = origin
		self.size = size
		self.color = color

		self.generateWindows()

	def generateWindows(self):
		self.windows = []

		numberOfWindowRows = int(self.size[1] / APPROX_WINDOW_HEIGHT)
		numberOfWindowColumns = int(self.size[0] / APPROX_WINDOW_WIDTH)

		numberOfWindowRows += random.randint(1, 2)
		numberOfWindowColumns += random.randint(1, 2)

		windowWidth = float(self.size[0] - WINDOW_BUFFER) / numberOfWindowColumns
		windowHeight = float(self.size[1] - WINDOW_BUFFER) / numberOfWindowRows

		windowWidth -= WINDOW_BUFFER
		windowHeight -= WINDOW_BUFFER

		for i in range(0, numberOfWindowColumns):
			for j in range(0, numberOfWindowRows):
				newWindowX = ((i + 1) * WINDOW_BUFFER + i * windowWidth)
				newWindowY = ((j + 1) * WINDOW_BUFFER + j * windowHeight)
				newWindow = Window((int(self.origin[0] + newWindowX), int(self.origin[1] + newWindowY)),
								   (int(windowWidth), int(windowHeight)),
								   "black")
				self.windows.append(newWindow)

	def draw(self, canvas):
		canvas.create_rectangle(self.origin[0], self.origin[1],
								self.origin[0] + self.size[0],
								self.origin[1] + self.size[1],
								fill=self.color)

		for window in self.windows:
			window.draw(canvas)
