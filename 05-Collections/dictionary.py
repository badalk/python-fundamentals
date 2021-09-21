# Dictionary is heart of many python programs
# Delimited by { and }
# key-value pairs comma separated
# corresponding keys and values joined by colon
# keys must be unique within the dictionary
# values can be accessed via keys and can be duplicate so long they are associated with different keys
# IMPORTANT
# Dictionary maintains the references to the key objects and value objects
# Key objects must be immutable * and hence strings, numbers and tuples are fine but lists are not
# The value objects can be mutable and in practice often are
# You should never rely on the order of items in the dicitionary i.e. it can have Arbitrary order
# Its essentially random and ay even vary between different runs of the same program
# Items in the dictionary are not stored in any particular order either
# Keys must be legitimate python identifiers

# ###1 - Basic and constructor
# As with other collections, dictionary has a constructor
# dict() constructor accepts iterable series of key-value 2-tuples
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
d = dict(names_and_ages)
d
# So long as the keys are valid python identifiers, you can create a dictionary directly from keyword arguments passed to the dict
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
phonetic # {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot'}

# ###2 - Copying dictionary
# IMPORTANT
# As with lists, dictionary copying is shallow by default. Copying only the references to the key and value object and not the objects themselves
# 2 methods to copy dictionaries
# 1 - copy method
d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
d
e = d.copy()
e
# 2 - Most common method of copying is by passing existing dictionary object to the constructor
f = dict(e)
f

# ###3 - Extending current dictionary
# if you need to extend the dictionary with definitions from another dictionary, you can use the update method
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimpson=0xDC143C)
f.update(g)
f
# if the keys match in source and target dictionaries, update replaces the values correspoding to duplicate keys from the source to the target dictionary onw hich the update is being called
stocks = {'GOOG': 891, 'AAPL':416, 'IBM': 194}
stocks.update({'GOOG': 894, 'YHOO': 25, 'AAPL':416})
stocks

# ###4 - Looping through dictionaries
colors = dict(aquamarine='#7FFFD4', burlywood='#DEB887',
              chartreuse='#7FFF00', cornflower='#6495ED',
              firebrick='#B22222', honeydew='#F0FFF0',
              maroon='#B03060', sienna='#A0522D')
for key in colors:
    print ("{key} ==> {value}".format(key=key, value = colors[key]))

# if you want to iterate only through values, we can use the values dictionary method
for value in colors.values():
    print (value)
# there is also keys method but not often used
for key in colors.keys():
    print (key)

# ideally you will iterate through key and values in tandem and for that you can also use items method on the dictionary
for key, value in colors.items():
    print ("{key} ==> {value}".format(key=key, value=value))

# ###5 - Membership functions to check if the item is in the dictionary or not
# It works only on keys
symbols = dict(usd='\u0024', gbp='\u00a3', nzd='\u0024',
               krw='\u20a9', eur='\u20ac', jpy='\u00a5', 
               nok='kr', ils='\u20aa', hhg='Pu')

symbols
'nzd' in symbols
'mkd' not in symbols

# ###6 - Delete an element from a dictionary
z = {'H': 1, 'Tc': 43, 'Xe': 54, 'Un': 137, 'Rf': 104, 'Fm': 100}
z
del z['Un'] # remove by key
z

# ###7 - Dictionary Mutability
# Keys are immutable, values may be mutable
m = {'H': [1, 2, 3],
     'He': [3, 4] ,
     'Li': [6, 7],
     'Be': [7, 9, 10],
     'B': [10, 11],
     'C': [11, 12, 13, 14]}
m
m['H'] += [4, 5, 6, 7] # dictionary is not being modified here but dictionary is extended
m
# IMPORTANT
#Dictionary itself is mutable
m['N'] = [13, 14, 15]
m

# ###8 - Pretty Printing
# Python standard library print module (arguably its a poor design to use the name module containing the function of the same name)
from pprint import pprint as pp 
pp(m)

