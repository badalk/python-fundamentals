# BESTPRACTICE Use common or existing exception types when possible
# Use exceptions that users will anticipate. Standard exceptions are often the best choice
# Use
#   IndexError - when an integer index is out of range
#   TypeError - Avoid protecting against type errors. This is against the grain of Pythons dynamic type system
#   KeyError - when a lookup in a mapping fails
#   ValueError - when the object is of the right type, but contains an inapproriate value

# BESTPRACTICE Usually its not worth to add type checking in python. Just let it fail
import sys

def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria
    
    Args:
        x: The number for which the square root is to be computed
    
    Returns:
        The square root of x.

    Raises:
        ValueError: If x is negative.

    '''

    # BESTPRACTICE Detect conditions early on and raise an exception at that point (like the one shown below), instead of bad practice highlighted below
    if x < 0:
        raise ValueError("Cannot compute square root "
                        "of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess) / 2.0
        i += 1

    # BADPRACTICE: Wasteful try-catch block - as you can always do it premptively as shown above by checking if the value is negative
    # try:
    #     while guess * guess != x and i < 20:
    #         guess = (guess + x/guess) / 2.0
    #         i += 1    
    # except ZeroDivisionError:
    #     raise ValueError()

    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is not printed due to the exception raised for above sqrt call.")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program execution continues normally here.")    

if __name__ == '__main__':
    main()
    