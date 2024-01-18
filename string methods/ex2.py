#string methods.
a='hellopythonlearners'
#is alpha.
#it returns true if a string contains only alphabets.
print(a.isalpha())

#is alnum:
#it returns true if a string contains alphabets,numbers or both.
b='hello'
print(a.isalnum())
c='10'
print(a.isalnum())
d='user10'
print(a.isalnum())
e='hello 10'
print(e.isalnum())

x='10'
y='10.2'
z='hello'
#is digit.
print(x.isdigit())
print(y.isdigit())
print(z.isdigit())

#is decimal.
print(x.isdecimal())
print(y.isdecimal())
print(z.isdecimal())

#is numeric:
print(x.isnumeric())
print(y.isnumeric())
print(z.isnumeric())

#replace.
#it is used to replace a character of a string with other character.
f='Hello python Hello Java'
print(f.replace('l','jagadeesh'))
print(f.replace('l','milestone',2))
