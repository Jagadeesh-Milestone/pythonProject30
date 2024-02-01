#unpickling:
#it is the process of converting byte stream code to python object.
#we use load method in unpickling:
import pickle
f=open('welcome.dat','rb')
x=pickle.load(f)
print(x)
f.close()