#dict comprehensions:
states=['karnataka','kerala','tamilnadu']
capitals=['bangalore','thiruvananthapuram','chennai']
x={}
for (key,value) in zip(states,capitals):
    x[key]=value
print(x)
#using comprehension:
y={key:value for (key,value) in zip(states,capitals)}
print(y)