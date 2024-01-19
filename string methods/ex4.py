#string formatting.
string1='my name is {} my address is {}'
x=string1.format('jagadeesh','bangalore')
print(x)

string2='my name is {0} my address is {1}'
y=string2.format('hari','chennai')
print(y)

string3='my name is {name} my address is {address}'
z=string3.format(name='manoj',address='hyderabad')
print(z)