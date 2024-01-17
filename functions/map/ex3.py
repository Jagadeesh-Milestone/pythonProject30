#map:
x=['bangalore','mumbai','chennai','hyderabad']
print(len(x))
print(len(x[0]),len(x[1]),len(x[2]),len(x[3]))

for i in x:
    print(len(i))

#using map:
def d1(n):
    return len(n)
z=map(d1,x)
print(list(z))

#using map in lambda
y=map(lambda a:len(a),x)
print(tuple(y))