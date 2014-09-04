from Tkinter import *

import random     

class Point():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class Size():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AspectRatio():
    def __init__(self, ratio):
        self.ratio = ratio

    def widthForHeight(self, height):
        return (height / self.ratio)

    def heightForWidth(self, width):
        return (width * self.ratio)

def modulateValue(value, delta):
    randomDelta = (random.random() * 2.0 * delta) - delta
    return (1.0 + randomDelta) * value

def removeAllChildren(widget):  
    for child in widget.winfo_children():
        child.destroy()
