#seek:
f=open('hello.txt','r')
f.seek(10)
f.tell()
print(f.read())
f.close()

