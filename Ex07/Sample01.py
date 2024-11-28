import math


def circumference(radius:float) -> float:
    '''
    calculate the circumference with the given radius.
    return the result with two decial places.
    you may want to have a helper function to make it work
    
    Tip: use the round up function, round(), and math.pi 
    '''
    pi = math.pi
    return round(float(pi * radius * 2),2)
 

