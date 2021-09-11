c = 5
while c != 0:
    print (c)
    c -= 1

while c: #unpythonic in this case although expression is implicitly converted to boolean
    print (c)
    c -= 1

#breaking out of the loop
c=5
while True:
    if c == 0:
        break #breaks the innermost while loop
    print (c)
    c -= 1

while True:
    response = input() #getting input from the user
    if int(response) % 7 == 0:
        break

