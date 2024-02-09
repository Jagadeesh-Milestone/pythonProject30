#Series:
import  pandas as p

x=p.Series([10,20,30,40,50])
print(x)
print(x[0])

#labels:
y=p.Series([100,200,300,400],index=['a','b','c','d'])
print(y)
print(y['b'])