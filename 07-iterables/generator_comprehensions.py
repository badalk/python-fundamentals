# IMPORTANT DEFINE Generator Comprehensions
# Generator comprehensions syntax is similar to list comprehensions
# (expr(item) for item in iterable) # delimited by parenthesis
# Creates a generator object which produces specified sequence lazily
# Concise
# Provides lazy evaluation
# Useful for situations where you want lazy evaluation of generators with the declarative concisions of comprehensions

million_squares = (x*x for x in range(1000001))
million_squares # returns a generator object # at this point none of the squares are created
# We can force the evaluation of the generator object by creating a long list
# This list contains significant chunk of memory about 40 MB
list (million_squares) 
# note that generator object is just an iterator and once run exhaustively in this way will yield no more items
list (million_squares) # returns an empty list, as generators are single use objects
# each time we call a generator function it creates a new generator object

# compute the sum of first 1 million squares using the built in sum function
# below function consumes no memory but some would assume it would be about 400 MB based on previous example. and this is because of lazy loading
# the function returns quickly
sum (x*x for x in range (1000001)) # notice we dont need additional parenthesis for the generator expression

# As with comprehensions you can include an if clause at the end of the generator expression
# get the sum of the first 1000 numbers which are prime
from filtering import is_prime
sum (x for x in range(1001) if is_prime(x))
