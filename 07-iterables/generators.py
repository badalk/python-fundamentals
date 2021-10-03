# One of the most powerful and ellegant feature of Python
# DEFINE Generators: 
# It provides the means of describing iterable series with code and functions. All generators are iterators
# Generators are evaluated lazily - the next value in the sequence is computed on demand
# This allows to model infinite squences, such as data streams with no definite end such as data from sensors, or active log files
# Using this, we can make generic stream processing elements, which can be composed into sophisticated pipelines

# Generators are defined by any python function that uses yield keyword at least once in its definition.
# They may also contain the return keyword with no arguments
# and just like any other functions there is an implicit return at the end of the definition
# Generator functions return generator object

def gen123():
    yield 1
    yield 2
    yield 3

g = gen123() # returns a generator object, which are in fact iterators and you can use std iterator functions to retrieve items
g #generator object which is also iterator
next(g)
next(g)
next(g)
next(g) # raises StopIteration exception

for v in gen123(): 
    print(v)

# Be aware that each call to the generator function creates a new generator object
h = gen123() # 0x7f91c8099f20
i = gen123() # 0x7f91a801c0b0
h # shows a different generator object
i # again a new generator object
h is i # Both are different and can be iterated separately
next(h) # 1
next(h) # 2
next(i) # 1

###2 How and when the code in generators gets executed
def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246() # no code is executed yet
next(g)
next(g) # Resumes execution
next(g) 
next(g)

