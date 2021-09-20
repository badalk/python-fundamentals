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
# ###4 - Copying Lists
full_slice = s[:] # Since start and stop indices are both optional. This is copying the list
full_slice
full_slice is s # as ids are different
full_slice == s # the elements within it are references to the same object 

u = s.copy() # more readable way of copying the list
v = list(s) # using the list constructor
# all of the above methods uses shallow copyies and its a matter of preference. list constructor above takes any iterable element as a parameter


# ###5 - SHALLOW COPIES
# Copies are shallow
a = [[1, 2], [3, 4]]
b = a[:] # b elements refers to the same element list as referred by a. These inner two lists refers to the same element references as in a
a is b #lists are distinct objects
a == b #but inner objects referes to the same objects
a[0]
b[0]
a[0] is b[0] # they refer to the same inner object
a[0] == b[0] # values are same
# Let us replace the element at a[0] with new list
a[0] = [8,9]
a[0] # points to the new list
b[0] # unmodified
# Append an additional item in list referred by a[1]
a[1].append(5)
a[1]
b[1]

# ###6 - List repetition
# Lists support repetition using mulitpleication operator
c = [21, 37]
d = c * 4
[0] * 9 # good approach to initialize the list of elements when the size is known
# IMPORTANT - 
# The repetition causes multiple references to one instance of the constant in the produced list. 
# Repetition using this kind of mulitiplcation will repeat the reference without copying the value

# ###7 - Repetition is shallow
s = [[-1, 1]] * 5 # [0,1,2,3,4] elements of the outerlist are all references to the same object, which is an inner list containing -1, 1 elements
s # [[-1, 1], [-1, 1], [-1, 1], [-1, 1], [-1, 1]]
# To prove this let us append additional integer in any one of the inner list
s[3].append(7) # appending 7 to the 4th inner list. This will create a new integer object and a new element on the inner list containing the inner reference to that integer object
s # [[-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7], [-1, 1, 7]] as you can see all of the elements of the outer list are modified because they all refer to the same inner list

# ###8 - Finding Elements in the list
w = "the quick brown fox jumps over the lazy dog".split()
w
i = w.index("fox")
i
w[i]
# finding element that does not exist throws a ValueError
w.index("unicorn")

# count number of occurences
w.count("the")
# Find the memberships or non-memberships
37 in [1, 78, 37]
25 not in [1, 78, 37]

# ###9 - Removing the elements from the lists
u = "jackdaws love my big sphinx of qaurtz".split()
u
del u[3]
u
# removing elements by value than by position
u.remove('jackdaws')
u
# Attempting to remove an element that does not exist gives a ValueError
u.remove('pyramid')

# ###10 - Inserting items in the list
a = "I accidently the whole universe".split()
a
a.insert(2, "destroyed") # takes the index at which you want to insert the element and the value of the element as parameters
a
' '.join(a) #reconstruct the string with space as a separator

# ###11 - Growing Lists / Working with multiple lists
# Concataneting two lists using the + operator creates a new list without modifying the existing operads
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n
k
# Augumented assignee operator modifies the operator in place
k += [18, 29, 47]
k
# you can also use extend method of the list
k.extend([76,129, 199])
k
# IMPORTANT
# All of this works with any iterable series not just lists

# ###12 - Reversing and Sorting Lists
g = [1, 11, 21, 1211, 112111]
# operations to re-arrange the elements in place
g
g.reverse() # reversing in-place
g
d = [5, 17, 23, 13, 67, 54, 96, 111, 75, 3456]
d
d.sort() # sorting in-place
d
# sort method also accepts two more parameters, reverse (true / false) and a key on which to sort
d.sort(reverse = True)
d
# key parameter in the sort method takes any callable object which is then used to extract a key from each item
# the items then be sorted according to the relative ordering of these keys
# There are several types of callable objects in Python
# For ex: built-in len function is a callable object (that is used to determine the lenght of a collection)
h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
h
h.sort(key=len) #sort h list based on the key as a lenght of an item
h
' '.join(h)

# sorted and reversed built-in functions. These will work on any finite length iterable source object
x = [4, 9, 2, 1]
y = sorted(x) #original list x is un-modified
y
p = [9, 3, 1, 0]
q = reversed(p)
q # returns list_reverseiterator object
list(q) # use list constructor to list the items of the list_reverseiterator object
