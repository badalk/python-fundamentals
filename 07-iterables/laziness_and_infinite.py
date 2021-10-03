# IMPORTANT Laziness and the infinite
# Just-in-time computation - Generators are lazy. Computation happens only when next result is requested
# This property can enable uses cases such as 
# Infinite (large) sequences - Generators can be used to produce never ending / large sequences such as 
# Sensor readings
# Mathmatical squences - such as primes / factorials
# Massive multi terrabyte files

###5
def lucas(numberofitemstoreturn): # 2, 1, 3, 4, 7 and 11 (prints Locas series)
    yield 2
    a = 2
    b = 1
    x = 2
    while x <= numberofitemstoreturn:
        yield b
        a, b = b, a + b
        x += 1

for x in lucas(20):
    print(x)