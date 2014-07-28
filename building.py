from Tkinter import *

class Building():
	def __init__(self, origin, size, color):
		self.origin = origin
		self.size = size
		self.color = color

	def draw(self, canvas):
		canvas.create_rectangle(self.origin[0], self.origin[1],
								self.origin[0] + self.size[0],
								self.origin[1] + self.size[1],
								fill=self.color)
