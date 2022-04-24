import math


def area(radius):
    """ returns area of a circle """
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return round((math.pi * (radius**2)),2)


def cicumference(radius):
    """ returns circumference of a circle """
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return round((2 * math.pi * radius), 2)
