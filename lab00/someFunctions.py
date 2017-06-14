# someFunctions.py    Define a few sample functions in Python
# P. Conrad for CS8, 08/06/2009

# CtoF: number -> number
#   consumes: a temperature in Celsius
#   produces: a temperature in Fahrenheit

import math;

def CtoF(cTemp):
    return (cTemp / 5.0) * 9 + 32


# squared: number -> number
#  consumes: a number x
#  returns: the square of that number

def square(x):
    return x * x;


def distance(x1,y1,x2,y2):
    return math.sqrt( square(x2-x1) + square(y2-y1) )
