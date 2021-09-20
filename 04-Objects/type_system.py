# #Dynamic Types
# # Strong Type System: cannot implicity convert objects types
# # Object references have no type

# def add (a, b):
#     return a + b;


# add (5, 7)
# add (2.5, 3.5)
# add ([3,5],[7,9])
# add ('Badal', ' Kotecha')

# #This produces the type error : TypeError: can only concatenate str (not "int") to str
# add ('Badal', 42)

#Scopes: Scopes are contexts in which named references can be looked up
#   4 scopes from narrowest to broadest are LEGB
#   Local: Inside the current function
#   Enclosing: Any and all enclosing the function
#   Global: top level of module. Each module brings in new global scope
#   Built-in: Build into the python language in special builtins module

count = 0

def show_count():
    print ("count = ", count)

# #In below function c is in Local Scope and although it sets and replaces the reference to count to point to c, when it goes out of that function scope, count is again set to 0
# # here we created new variables with shadows (count)
# def set_count(c):
#     count = c

# to refer to the global variable inside a function use global keyword as shown below
def set_count(c):
    global count
    count = c