# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    """A class for a Vehicle object.

    >>> c = Vehicle(40, 200000)
    >>> c.max_speed
    40
    >>> c.mileage
    200000
    
    """

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage





if __name__ == "__main__":
    import doctest
    doctest.testmod()