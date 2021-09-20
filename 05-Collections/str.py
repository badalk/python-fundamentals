# Str - is a homegenous squence of immutable unicode codepoints (Characters)

# ###1 - Basic
# As with any other python sequence we can determine the lenght of a sequence using len function
len("asdfljasdfas;dlkfjasdf;ljkasdf;lkj")

# ###2 - String concatanation
# Using + opeator
"New" + "found" + "land"
# BADPRACTICE 
# Below exmaple generates large number of temporaries using + or augumented += operator, with consequent costs for memory allocations and copies
s = "New"
s += "found"
s += "land"
# BESTPRACTICE - Use join method to concatanate large number of strings
# If you are joining large number of strings, "join" method should be preferred as it is substantially more efficient **
# join takes collection of strings as an argument and produces a new string by inserting a separator in between each of them
# ** spearator is the string on which the join operation is called
colors = ";".join(['$45ff23', '#2321fa', '1298a3', '#a32312'])
colors
colors.split(';') #split them again using split method
# use empty string as a separator to join multiple strings
''.join(['high', 'way', 'man'])

# ###3 - partitioning
# Partition method devides a string into three parts, prefix, separator and suffix
"unforgetable".partition('forget') # here 'forget' is the separator and string is partitioned using that separator
# BESTPRACTICE - Combining tuple unpacking with string partition
#  this is commonly used using tuple un-packing
departure, separator, arrival = "London:Edinburgh".partition(':')
departure
arrival
separator
# COOL 
# often we are not interested in capturing the separator value, for which you can use "_" variable name for unused or dummy values as shown below
origin, _, destination = "Cincinnati-to-Mumbai".partition('-to-')
origin
destination

# ###4 - Formatting Strings
# Use format() function to insert values into the strings 
"The age of {0} is {1}".format('Jim', 32)
# use field names more than one
"The age of {0} is {1}. {0}'s birthday is on {2}".format('Jim', 32, 'October 31')
# if fields names are used only once in same order as arugments, they can be omitted
"Your winning numbers are {} and {}".format(5, 42)
# if keyword arugments are passed in format, then named field can be used instead of indexes
"Current position is {latitude} {longitude}".format(latitude="60N", 
                                                    longitude="5E")

# ###5 - Using Tuples and other objects with string formatting
# COOL - Using object attributes in string formatting
pos = (65.2, 23.1, 82.2)
"Galactic Position x={pos[0]} y={pos[1]} z={pos[2]}".format(pos=pos)
# we can even access object attributes e.g. math object
import math
"Math constants: pi={m.pi}, e={m.e}".format(m=math)
# format strings also gives us lot of control over field alignment and floating point formatting as shown below to show pi value in 3 decimals
"Math constants: pi={m.pi: .3f}, e={m.e: .3f}".format(m=math)

# ###6 - Familiarize yourself with other string methods
help (str)