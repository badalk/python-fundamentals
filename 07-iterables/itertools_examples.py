from itertools import islice, count
from filtering import is_prime

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
thousand_primes # returns islice object
list(thousand_primes) # create list of thousand prime numbers
sum(islice((x for x in count() if is_prime(x)), 1000))
