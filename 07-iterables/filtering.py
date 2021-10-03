from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1): # loop  through 2 and half of the numbers
        if x % i == 0: 
            return False
        return True

# ###1 Predicate syntax
# [expr(item) for item in iterable if predicate(item)]
[x for x in range(101) if is_prime(x)] # predicate at the end determines which items at the source are evaluated by the expression

# you can combine the filtering predicate to the transforming expression
prime_square_divisors = {x*x:(1, x, x*x) for x in range(101)
                         if is_prime(x)} # numbers with only 3 divisors mapped to those divisors

# BESTPRACTICE Your comprehensions should have no side-effects. 
# Long complex comprehensions may be less readable than the equivalent for loop
# If you need to create side effects such as printing to the console during iteration, use construct such as for loop instead


