#str is immutable sequences of Unicode codepoints / characters
#Literal strings are delimited by quotes (single / double)
'This is a string'
"This is also a string"
"It's a good string"
'"He said so"'

#Moment of Zen: Practicality beats purity

"first" "second" #concatanates to firstsecond

#Multi-line strings (for strings containing new line)
"""This is a 
multiline 
string"""

'''This is 
also a 
multiline string'''

#Escape sequences
m = 'This string\nspans multiple\nlines' #embed newline characters yourself
m
print (m)

"This is a \" in a string"
'This is a \' in a string'
'This is a \" and a \' in a string' #use print to see the output
k = 'A \\ in a string.'
print (k)


## RAW strings => What you see is what you get"
path = r'C:\Users\Merlin\Document\Spells'
print (path)

#convert other types into strings using strinc constructor
str(400)
str(30.5)

#Operations to querying sequences
s = 'parrot'
s[4]
type(s[4])

#get help on str and explore various operations
help(str)


c = 'oslo'
print(c.capitalize())