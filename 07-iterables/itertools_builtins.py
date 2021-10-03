any([False, False, True]) # returns True as any returns true only when any of the series its passed is True
all([False, False, True]) # returns False as all returns true only when all of the series its passed are True

# Using generator expression to find out if there are any prime numbers in a given range with inclusive
from filtering import is_prime
any(is_prime(x) for x in range(1328, 1361)) # returns False

# Check if all of the city names are proper nouns with first letter as capital
all(name == name.title() for name in ['London', 'New York', 'Sydney']) 

# Zip - Gives us the way to synchronize iterations over two iterable series
# combine pairs of temperatures from two days
sunday = [12, 14, 15, 13, 15, 17, 18, 16]
monday = [13, 14, 12, 11, 16, 17, 11, 14]
for item in zip(sunday, monday):
    print(item) # you can see that zip returns tuples when iterated

# we can use tuple unpacking in the for loop to calculate the average temperature
for sun, mon in zip (sunday, monday):
    print("average = ", (sun + mon) / 2)

# zip can accept any number of arguments
# here we can calculate minimum, maximum and average temperatures for sunday, monday and tuesday
tuesday = [14, 11, 10, 13, 9, 15, 11, 14]
for temps in zip (sunday, monday, tuesday):
    print ("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(min(temps), max(temps), sum(temps)/len(temps)))

# chain
# we may need long temperature series for monday, tuesday and wednesday
# we can lazil concataneate the tuples using itertools chain
# this is different than simply concataneating three lists into new lists
from itertools import chain
temperatures = chain(sunday, monday, tuesday)
# check if all of those temperatures are above freezing points without the memory impact of data duplication
all(temp > 0 for temp in temperatures)


## combining it all
from laziness_and_infinite import lucas
from filtering import is_prime
for x in (p for p in lucas(200) if is_prime(p)):
    print (x)