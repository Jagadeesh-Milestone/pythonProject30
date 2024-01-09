#dictionary:
#it is the combination of key and value pairs.
#dictionary allows duplicate values but not duplicate keys.
#it is mutable.
#it is taken in {}.
#it is having ordered elements.
#empty dict.
d={}
print(d)
print(type(d))

#dictionary:
a={'username':'jagadeesh','address':'bangalore','contact':9878877987}
print(a)
print(type(a))
print(a.keys())
print(a.values())
print(a.items())

#add new item:
a['course']='python'
print(a)

#update:
a['username']='hari'
print(a)

#pop:
a.pop('address')
print(a)

#popitem:
a.popitem()
print(a)

#duplicate keys are not allowed:
b={'user1':'hari','user2':'manoj','user1':'suresh'}
print(b)

#duplicate values are allowed:
c={'user1':'hari','user2':'suresh','user3':'hari'}
print(c)

#delete a key:
del c['user2']
print(c)

#delete dictionary:
del c
print(c)