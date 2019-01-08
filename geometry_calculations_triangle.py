import math


def area_triangle(base,height):
    ''' (number, number) -> float
    Return the area of a triangle with dimensions
    base and height.
    >>> area_triangle(10, 5)
    25.0
    >>> area_triangle(2.5, 3)
    3.75
    >>> area_triangle(11.1, 5.1)
    28.3
    '''
    
    return base*height/2




def perimeter_triangle(side1, side2, side3):
    ''' (number, number, number) -> float
    Return the perimeter of triangle with sides
    of length side1, side2 and side3.

    >>> perimeter_triangle(3, 4, 5)
    12
    >>> perimeter_triangle(10.5, 6, 9.3)
    25.8
    >>> perimeter_triangle(1.1, 3.3, 2.8)
    7.2
    '''

    return side1 + side2 + side3




def semiperimeter_triangle(side1, side2, side3):
    ''' (number, number, number) -> float
    Return the semiperimeter of a triangle
    with side1, side2 and side3.
    >>> semiperimeter_triangle(3, 4, 5)
    6.0
    >>> semiperimeter_triangle(10.5, 6, 9.3)
    12.9
    >>> semiperimeter_triangle(1.1, 3.3, 2.8)
    3.6
    '''

    return perimeter_triangle(side1, side2, side3)/2




def area_hero(side1, side2, side3):
    ''' (number, number, number) -> float
    Return the area of triangle with sides of length
    side1, side2 and side3, by Heron's formula.
    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5, 6, 9.3)
    27.731
    >>> area_hero(1.1, 3.3, 2.8)
    1.469
    '''

    semi = semiperimeter_triangle(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area
    
    
