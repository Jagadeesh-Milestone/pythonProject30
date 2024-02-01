#writelines:
f=open('bangalore.txt','w')
l=['bangalore','mumbai','chennai','hyderabad']
f.writelines(l)
print('data is inserted')
f.close()