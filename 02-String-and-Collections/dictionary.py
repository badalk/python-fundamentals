# mutable mappings of keys to values
# also called associative arrays
# dictionary literals {k1:v1, k2:v2}

#simple telephone directory
directory = {
    'alice': '123-234-4355',
    'jack': '513-394-2342',
    'eunice': '343-443-5345'
}
print (directory['jack'])

directory['alice'] = '444-555-6666' #update
print (directory)

directory['charles'] = '333-666-9999' #append
print (directory)

# create an empty dictionary
d = {}
