#imutable sequences of bytes
d = b'some bytes'
d.split()

#Converting between strings and bytes
#decode and encode
# str => encode => bytes
# bytes => decode => str

norsk = "Jeg begynte å fortære en sandwitch mens jeg kjørte tax i på vei til quiz."
data = norsk.encode('utf-8')
print (data)

norwegian = data.decode('utf-8')
print(norsk == norwegian)