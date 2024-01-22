#splitlines:
#it is used to split the string at every new line.
a='hello python learners\n hello java learners\n hello bangalore'
print(a.splitlines())

#partition:
#it is used to make string into 3 parts.
b="Hello Python Learners.Good morning!"
print(b.partition('Python'))
c='hello python learners.I like python course'
print(c.rpartition('python'))

#swapcase:
#it converts upper case to lower case and lower case to upper case.
d="Hello PytHon LearNers"
print(d.swapcase())

#expandtabs:
e="h\te\tl\tl\to"
print(e.expandtabs())
print(e.expandtabs(2))
print(e.expandtabs(5))
print(e.expandtabs(10))

#is space:
#it will returns true if a string contains all the spaces.
f="      "
print(f.isspace())
g="  . "
print(g.isspace())