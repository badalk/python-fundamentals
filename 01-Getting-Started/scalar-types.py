# int - integers are arbitrary precition integers
# float - 64 bit floating point numbers
# bool - boolean logical values
# None - the null object

# integers
print(10)
print (0b10) #binary
print (0o10) #octal
print (0x10) #hexadecimal

#convert float to int
int (-3.5) #converts towards 0
int ("400") #converts string to int
int ("10000", 3) #convert 10000 to base 3 => outputs 81

#Floats
3.125
3e8
1.616e-35
float (7)
float ("1.686")

3.0+1 #result of any calculation involving int and float is promoted to float

#/None represets that value does not exists
None #does not print anything
a=None
a is None

#Boolean
True
False
bool(0) #only 0 is considered as true
bool(100)
bool(-5)
bool(0.0) #true
bool(0.05) #false
bool([]) #empty list is false
bool([1,3,5]) #since this is not empty, this is true
bool("") #empty string is false
bool("something here") # this is true
bool("False") #and hence interestingly this returns true and not false **
bool("True") #also returns true


