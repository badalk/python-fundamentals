#Argument Passing
#   Arguments are passed by object reference.
#   i.e. Value of the reference is copied not the value of the object

# Example 1: values modified inside a function reflects in the reference outside the function
f = [4,7,11]

def modify(k): #value passed by ref
    print ('original f: ', k)
    k[1] = 9
    return k

print ("Returned k: ", modify(f))
print ("Value of f after function call:", f) #this also shows the changed values inside the function


# Example 2: complete object changed
print ("Example 2: Replacing the passed object to a new one, without changing the contents of the original object")
f = [3,5,7]

def replace(k):
    k = [2,4,6]
    print ("k = ", k)


replace (f)
print ("original f: ", f) #not changed

# Example 3: Replace the contents
print ("Example 3: Replace the contents of the original objhect")

r = [23,45,67]

def replace_contents(q):
    q[0] = 11
    q[1] = 22
    q[2] = 33
    return q

print ("Before: ", r)
print ("Function Returned: ", replace_contents(r))
print ("After: ", r)