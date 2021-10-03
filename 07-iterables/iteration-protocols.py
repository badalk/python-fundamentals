# Iterable object and Iterator object
# Iterable protocol and Iterator protocol

# Iterable Protocol
#   - Iterable objects can be passed to the built-in iter() function to get an iterator
#       iterator = iter(iterable)
#
# Iterator Protocol
#   - Iterator objects can be passed to the built in next() function to fetch the next item.
#       item = next(iterator)

###1 - Simple iternable next function
iterable = ["Summer", "Winter", "Autumn", "Spring"]
iterator = iter(iterable)
next(iterator) # Summer
next(iterator) # Winter
next(iterator) # Autumm
next(iterator) # Spring
next(iterator) # Python raises an exception called StopIteration as there are more objects to iterate

###2 - Example 2 with List, Set and empty set
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

first(["1st", "2nd", "3rd"])
first({"1st", "2nd", "3rd"})
first(set())

# COOL It is worth noting that the higher level constructs such as for loops and comprehensions are built on thes lower level iteration protocols
