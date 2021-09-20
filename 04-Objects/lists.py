r = [4,7,11]
s = r
s[1] = 12

r == s # returns true
r is s
id (r) == id (s) #returns true as both r and s refers to the same object

# Example 2: Value Equality and Object Identity
# Value equality: refers to equivalent contents and could be managed programatically especially if you create your own objects
# 
r = [7,8,9]
s = [7,8,9]
r == s # value equality, which is not same as object identity equality
r is s # should return false as both objects are different
r is r

