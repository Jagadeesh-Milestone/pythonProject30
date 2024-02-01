#while in file handling:
f=open('java.py','w')
name='jagadeesh'
while name=='jagadeesh':
    name=input('enter your name:')
    f.write(name)
f.close()