# In mathematics, a tuple is a finite ordered list (sequence) of elements. ... 
# An n-tuple is defined inductively using the construction of an ordered pair. 
# Mathematicians usually write tuples by listing the elements within parentheses "( )" and separated by commas; 
# for example, (2, 7, 4, 1, 7) denotes a 5-tuple

# It is Immutable seuqneces of arbitrary objects
# Once created = objects within them cannot be replaced or removed, and new elements cannot be added

# 1 - Basic examples
# respresented by parenthesis and can contain multiple type of objects
t = ("Norway", 4.953, 3)
t
t[0] # can be accessed by index
t[2]
type(t) # shows that its an object of type tuple

# 2 - Iterating through tuples
# can iterate using for loop
for item in t:
    print(item)

# 3 - Concatanation
# can concatanet tuples using + operator
t + (338186.0, 265e9)

# 4
# tuples can be repeated using multipllication operator
t * 3

# 5 - Nested Tuples
# Since tuples can contain any objects, it is possible to have nested tuples
a = ((220, 284), (153, 34), (1043, 4000))
a[2]
# we can use repeated application of indexing opearator to get to the inside elements  
a[2][1]

# 6 - single element tuple, 
# you cannot use single element tuple as python interprets as precedence opeator with integer
h = (391)
h 
type(h) #shows its a type of int and not tuple
k = (391,) # **** use trailing commas in tuple, lists and dictionaries to create single element tuple
k
type (k)

#7 - Empty tuple
# create emtpy tuple with empty parenthesis
e = ()
e
type (e)

# 8 - Literal tuples
# Parenthesis of literal tuples can be omitted in many cases
p = 1, 1, 1, 4, 6, 19
p
type (p)
# this feature is often used to return multiple values from a function
def minmax(items):
    return min(items), max(items) #here it will return tuple even though there is no parenthesis being used

minmax([83,55,23,9,67,43,35])

# 9 - Tuple unbacking - 
#   Returning multiple values from a function is often used with a wonderful feature of python called tuple unpacking
#   It is a destructuring opearation which allows us to unpack data structures into named references as shown below 
lower, upper = minmax([83,55,23,9,67,43,35])
lower
upper
# It also works with arbitrarily nested tuples as shown below, although not with other data structures
(a, (b, (c, d))) = (4, (3, (2, 1)))
a
b
c
d
# This in turn leads into a beautiful python idiom for swapping two or more variables
a = 'jelly'
b = 'bean'
a, b = b, a #swapping
a
b

# 10 - Creating tuple with constructor
# Conver existing object / iterable object into a tuple, you can use tuple constructor
tuple([561,345,567,346])
tuple("Converting this string into a tuple")

# 11 - Containment
# As with most collections, you can check the containment using the "in" operator
5 in (3, 5, 7, 9, 35)
# or non membership with "not in" operator
5 not in (4,6,8,0)



