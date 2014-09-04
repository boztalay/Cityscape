from Tkinter import *

from basics import Size, AspectRatio, removeAllChildren

class Window():
    requestedAspectRatio = AspectRatio(1.5)
    requestedHorizontalPadding = 0.25
    requestedVerticalPadding = 0.3

    def __init__(self, size):
        self.size = size

    def draw(self, canvas):
        removeAllChildren(canvas)
        canvas.delete("all")
        canvas.create_rectangle(0, 0, self.size.width, self.size.height, fill="black")
