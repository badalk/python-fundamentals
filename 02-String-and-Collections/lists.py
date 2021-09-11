#mutable sequences of objects
#elements within them can be replaced or removed, new elements can be inserted or appeneded
#list can contain heterogenous items e.g. string and int etc

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