# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    """A class for a Vehicle object. 
    #* To run doctests: $ python3 OOP_practice.py -v

    >>> c = Vehicle(40, 200000)
    >>> c.max_speed
    40
    >>> c.mileage
    200000
    
    """

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# OOP Exercise 2: Create a Vehicle class without any variables and methods

class VehicleSansMethods:
    """a class for a Vehicle object - no variables or methods.
    >>> c = VehicleSansMethods()
    >>> c.max_speed
    Traceback (most recent call last):
    AttributeError: 'VehicleSansMethods' object has no attribute 'max_speed'
    >>> c.mileage
    Traceback (most recent call last):
    AttributeError: 'VehicleSansMethods' object has no attribute 'mileage'
    """

    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()