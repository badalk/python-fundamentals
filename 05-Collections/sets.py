# Set data type is unordered collection of unique, immutable objects'
# The collection is mutable, elements can be added and removed form the set, but each element in itself will be immutable
# delimted by { and }

# Protocol              Implementing Collections                                Support for 
# ## ## ## ## ## #      ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##         ## ## ## ## ## ## ## ## ## ## ## ## ##
# Container             str, list, range, tuple, bytes, set, dict               "in" and "not in"
# Sized                 str, list, range, tuple, bytes, set, dict               len(s)
# Iterable              str, list, range, tuple, bytes, set, dict               can produce an iterator with iter(s)
# Sequence              str, list, range, tuple, bytes                          items can be retrived, searched, count, and reversed with [integer index]
# Mutable Sequence      list                                                    
# Mutable Set           set
# Mutable Mapping       dict
# ## ## ## ## ## #      ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

# ###1 - Basic examples
p = {6, 28, 496, 8128, 33550336}
p
type(p)


# ###2 - Create an empty set
d = {} # creates an empty dictionary
type (d)
# IMPORTANT - Create an empty set 
# To create an empty set, you need to use the constructor
e = set()
e
# set constructor can create a set from any iterable series such as a list, and duplicates are discarded
s = set([2, 4, 16, 64, 4096])
s
# In fact, a common use of set is to remove duplicate items from a series of objects
t = [1, 4, 2, 1, 7, 9, 9]
set(t)

# order is arbitrary
for x in {1, 2, 4, 8, 16, 32}:
    print(x)

# ###3 - Membership functions in and not in
q = {2, 9, 6, 4}
3 in q
3 not in q

# ###4 - Add, Remove, Copy
k = {81, 108}
k
k.add(54)
k
k.add(12)
k
k.add(108) #adding the same element has no effect as duplicates are not allowed in a set, and neither does it produce an error
k
# multiple items can be added in one go from any iterable series
k.update([37, 128, 97])
k
# two methods are provided for removing items from a set
k.remove(98) #requires an element to exist in set otherwise a KeyError is given
k.discard(98) #is less fussy if the item being removed is not a member of the set
# as for the other built in collections set has a copy method and is a shallow copy method
j = k.copy()
j
m = set(j) #this method can also be used to copy the set
m

# ###5 - Set functions for Set Algebra
# for set unions, set differences and set intersections
# to evaluate if two sets have subset or superset or disjoint set relations
# Below are sets of people with different phenotypes
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua' }
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# Union
blue_eyes.union(blond_hair) # people who are either has blue eyes or blond hair or both
# union is a commutative operation
blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)

# Intersection
blue_eyes.intersection(blond_hair) # people who are present in both sets - blue eyes AND blond hair
# intersection is commutative operation
blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes)

# Difference 
# Identify people with blond hair who dont have blue eyes
blond_hair.difference(blue_eyes)
# Difference is non-communtative
blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair)

# Symmetric Difference 
# People who exclusively has blond hair or blue eyes (people who are either - AND - only one set but not both)
blond_hair.symmetric_difference(blue_eyes)
# Symmetric difference is commutative
blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair)

# In addition, 3 predicate methods are provided to tell us about relationship between sets
# Subsets
# Check if one set is a subset of another set
smell_hcn.issubset(blond_hair)
# Suberset
# Check if a given set is a super set of another set
taste_ptc.issuperset(smell_hcn) # to check all people who can taste hydrogen cyanide can also taste phyenylthiocarbamide can also taste hydrogen cyanide
# Disjoint sets
# To test that two sets have no members in common, use isdisjoint method
a_blood.isdisjoint(o_blood)