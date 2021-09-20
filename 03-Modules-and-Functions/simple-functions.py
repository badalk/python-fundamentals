def square(x):
    return x*x

square(10)

# function without a return value 
def launch_missiles():
    print ("Missiles Launched")

launch_missiles()

# Return from function without returning a value
def even_or_odd(n):
    if n % 2 == 0:
        print ("Even")
        return
    print ("Odd")

even_or_odd(5)
w = even_or_odd(35)
w is None