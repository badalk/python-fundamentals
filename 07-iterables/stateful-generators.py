###3 Maintaining State in local variables
# DEFINE Stateful Generators:
# Generators resume execution
# Can maintain state in local variables
# Allows for Complesx control flow
# Lazy evaluation

# following function / generator takes specified number of elements from the front of the sequence 
def take(count, iterable):
    '''Take items from the front of an iterable
    
    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series
    
    Yields:
        At most 'count' items from 'iterable'
    '''
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

# Since generators are lazy and only produce values only on request, we will drive execution through a for loop in below function
def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take (3, items): # this will take values from generator until it terminates
        print (item)

if __name__ == '__main__':
    run_take()

