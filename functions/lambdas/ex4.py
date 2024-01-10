#nested lambda:
x=lambda a=10:(lambda b:((a+b),(a-b)))
y=x()
print(y(20))