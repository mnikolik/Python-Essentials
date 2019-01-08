import math


def circumference_circle(radius):
    ''' (number) -> float
    Return the circumference of a circle with given radius,
    following equation L = 2*r*Pi.
    >>> circumference_circle(2)
    12.566
    >>> circumference_circle(5.5)
    34.557
    >>> circumference_circle(1234e15)
    7.75345e+18
    '''
    
    return 2 * radius * math.pi




def area_circle(radius):
    ''' (number) -> float
    Return the area of a circle with given radius,
    following equation P = r^2 * Pi.
    >>> area_circle(2)
    12.566
    >>> area_circle(5.5)
    95.033
    >>> area_circle(1234e15)
    4.784e+36
    '''

    return radius**2 * math.pi




def volume_sphere(radius):
    ''' (number) -> float
    Return the volume of a sphere with given radius,
    following the equation V = (4/3)*(r^3)*Pi.
    >>> volume_sphere(2)
    33.510
    >>> volume_sphere(5.5)
    696.91
    >>> volume_sphere(1234e15)
    7.871e+54
    '''

    return (4/3) * (radius**3) * math.pi
    
