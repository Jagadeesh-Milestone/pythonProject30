#datetime
#this module is used to display the date and time in python
#programming.
import datetime
import time
#current date and time
#a=time.ctime()
#print(a)

#local time
b=time.localtime()
print(b)

#shortform of day name
c=time.strftime('%a',b)
print(c)

#full form of day
d=time.strftime('%A',b)
print(d)

#shortform of month name
e=time.strftime('%b',b)
print(e)

#full form of month name
f=time.strftime('%B',b)
print(f)

#century
g=time.strftime('%C',b)
print(g)

#month of the year
h=time.strftime('%m',b)
print(h)

#time hours possible values are 00-23
i=time.strftime('%H',b)
print(i)

#seconds possible values are 0-59
j=time.strftime('%S',b)
print(j)

#minutes possible values are 0-59
k=time.strftime('%M',b)
print(k)

#week day possible values are 1-7
l=time.strftime('%w',b)
print(l)

#shortform of the year
m=time.strftime('%y',b)
print(m)

#full form of the year
n=time.strftime('%Y',b)
print(n)

#hours possible values are 0-12
o=time.strftime('%I',b)
print(o)

#AM/PM
p=time.strftime('%p',b)
print(p)

#time zone
q=time.strftime('%z',b)
print(q)

#day of the year possible values are 001-366
r=time.strftime('%j',b)
print(r)

#day of the month
s=time.strftime('%d',b)
print(s)

#week of the year possible values are 1-52
t=time.strftime('%W',b)
print(t)

#full date format
u=time.strftime('%x',b)
print(u)

#full time format
v=time.strftime('%X',b)
print(v)
