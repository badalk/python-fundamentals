# heterogeneous mutable sequence
# ###1 - Basic
s = "show how to index into sequences".split()
s

# ###2 - Indexes (front and back)
s[4] # access the 5th element
# Ability to index from the end - Very convinient feature of lists and other python sequences, and applies to tuples too
s[-5] #5th element from end
s[-1] #last index
# there is no difference between 0 and -0 index and hence indexing from the end starts from -1

# ###3 - Slicing 
# It is the form of extended indexing which allows to refer to the portions of the lists
s[1:4] #slice 3 words from the lists with start index of 1 and stop at 4
s[1:-1] #take all the elements except first and last
s[3:] #start and stop arguments are optional. To extrract the portions of the list from a starting index till the end
s[:3] #slicing fromt he begining till the index, excluding the stop index item
# s[:x] + s[x:] == s this slicing together forms the whole list
# ###4 Copying Lists
full_slice = s[:] # Since start and stop indices are both optional. This is copying the list
full_slice
full_slice is s # as ids are different
full_slice == s # the elements within it are references to the same object 

u = s.copy() # more readable way of copying the list
v = list(s) # using the list constructor
# all of the above methods uses shallow copyies and its a matter of preference. list constructor above takes any iterable element as a parameter


# SHALLOW COPIES
# Copies are shallow
a = [[1, 2], [3, 4]]
b = a[:]
