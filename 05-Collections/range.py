# Range is a collection and is type of sequence representing arithmetic progression of integers

# ###1 - Basic Example
# range(5) # stop value of 5. You will have integers from 0 to 4 (5 is not included)

# ###2 - Loop Counters
# Range is sometimes used as consecutive integers to be used as loop counters
for i in range(5):
    print(i)

# ###3 - Range with different starting points and creating list of values from a range
# you can supply a starting value if you wish
range (5, 10) # values from 5 to 9
list (range(5,10))
list (range(10,15))

# ###4 - Step Argument
# step argument to indicate the interval between numbers
# in order to use step argument all arguments are required
# range(start, stop, step)
# range also does not support keyword argument
list (range(0,10,2)) # will produce 0, 2, 4, 6, 8


# ###5 - Using range as index iterator for list of items
# BADPRACTICE
# Poorly styled python code - unpythonic
s = [0, 1, 4, 6, 13]
for i in range(len(s)): #although this works, this is unpythonic
    print (s[i])

# instead use items in the list directly
for v in s:
    print (v)

# ###6 - Using tuple unpacking if you have to use the index 
# if for some reason you need a counter you can use the built-in enumerate function
# It returns iterable series of pairs, each pair being the tuple 
# first element is the index of the item, and the second element is the tuple itself
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t):
    print (p)

# we can improve this by using tuple unpacking and avoiding having directly to deal with tuple
for i, v in enumerate(t):
    print("i = {}, v = {}".format(i,v))


