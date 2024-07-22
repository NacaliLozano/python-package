import math
from . import basic

def area_of_rectangle(LENGTH, BREADTH):
    return LENGTH * BREADTH

def area_of_circle(RADIUS):
    return math.pi * basic.square(RADIUS)
