#file handling:
#writing into a new file:
f=open('hello.txt','w')
name=input('please enter your name:')
f.write(name)
f.close()
