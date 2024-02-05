#regular expressions:
import re
string='hello python learners'
pattern='l'
x=re.findall(pattern,string)
print(x)

#^ symbol is used to check whether the string is starts with the
#specified characters or not.
string2='Welcome to python course'
pattern2='^Welcome'
y=re.findall(pattern2,string2)
print(y)

#$ symbol is used to check whether the string is ending with the
#specified characters or not.
string3='hello bangalore'
pattern3='bangalore$'
z=re.findall(pattern3,string3)
print(z)

#[a-n]
#this method prints the alphabets from a-n in a given string
string4='hello python learners'
pattern4='[a-n]'
a=re.findall(pattern4,string4)
print(a)

#[0-9]
#this method prints the numbers from 0-9 in a given string
string5='my number is 9879889 my user id is 789789'
pattern5='[0-9]'
b=re.findall(pattern5,string5)
print(b)

#+
#this method returns if a string contans any special characters
string6='hello % # @ good evening!+'
pattern6='[+,@,%,#,!,$]'
c=re.findall(pattern6,string6)
print(c)

#search
string7='hello python learners'
d=re.search('\s',string7)
print('the first whitespace character is located at',d.start())

#split:
string8='hello milestone technologies'
e=re.split('\s',string8)
print(e)

#sub:
string9='hello python learners'
d=re.sub('\s','jagadeesh',string9)
print(d)