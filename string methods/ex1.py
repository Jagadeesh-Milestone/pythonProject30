#string methods:
a='bangalore'
print(a)
print(type(a))
print(len(a))
print(a.count('a'))
print(a.index('a'))
print(a.rindex('a'))
print(a[2])
print(a[-3])

b='Hello Python Learners'
#upper:
#it will print the string in upper case letters
print(b.upper())

#lower:
#it will print the string in lower case letters
print(b.lower())

#is upper:
#it will return true if each letter of a string is in upper case.
#otherwise it returns false.
x='HELLO WORLD'
print(x.isupper())

#is lower:
#it will return true if each letter of a string is in lower case.
#otherwise it returns false.
y='hello python'
print(y.islower())

#title:
#it will print first letter of every word in upper case
c='hello java learners'
print(c.title())

#is title:
#it returns true if the first letter of each word in a string is
#starting with a upper case and remaining letters in lower case.
d='Hello Bangalore'
print(d.istitle())
