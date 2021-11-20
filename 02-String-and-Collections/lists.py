#mutable sequences of objects
#elements within them can be replaced or removed, new elements can be inserted or appeneded
#list can contain heterogenous items e.g. string and int etc
# Method	    Description
# =========     =====================================
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

a = ["apple", "orange", "banana"]
print (a[1])
a[1] = 7
print (a)

#you can create an empty list
b = []
b.append(1.414)
b.append(2.43534)
print (b)

#list constructor
chars = list("characters")
print (chars)

#long literal collections with improved readability
animals = ["bear", 
            "tiger",
            "elephant",
            "rabbit"]

print (animals)