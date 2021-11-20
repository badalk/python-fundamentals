class Flight:
    # initializer and not a constructor
    # object already exists by the time __init__ is being called
    # self is similar to "this" in Java and C++
    # used to configure the object
    # actual constructor is provided by the python runtime system and one of the thing it does is to call the check for the existance of the initializer and call if it is present

    def __init__(self, number): 
        # we dont need to define the object attributes before we create them
        self._number = number

    def number(self):
        return self._number

from airtravel import Flight    
f = Flight("SN060")
f.number()
Flight.number(f)
