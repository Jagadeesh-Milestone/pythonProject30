#polymorphism:
#it is the property in which a single method having different properties.
#polymorphism in * operator
#* is used in multiplication
a=10
print(a*4)
#* is used in power
b=5
c=4
print(b**c)
#* used in taking multiple values to a single argument.
def d1(*students):
    print(students)
d1('hari','manoj','naresh')

#* is used to pass keyword arguments.
def d2(**users):
    print(users)
d2(user1='naresh',user2='suresh')

