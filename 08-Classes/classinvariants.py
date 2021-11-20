class Flight:
    # initializer and not a constructor
    # object already exists by the time __init__ is being called
    # self is similar to "this" in Java and C++
    # used to configure the object
    # actual constructor is provided by the python runtime system and one of the thing it does is to call the check for the existance of the initializer and call if it is present

    def __init__(self, number): 
        # Class invariants:
        #   Truths about an object that endure for its lifetime
        # In python we establish class invariants in __init method and raise exceptions if it cannot be attained
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))
        # we dont need to define the object attributes before we create them
        self._number = number

    def number(self):
        return self._number

    def airlinecode(self):
        return self._number[:2]


from classinvariants import Flight    
f = Flight("SN060")
f.number()
Flight.number(f)