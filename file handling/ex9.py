#pickling:
import pickle
print('pickling the list of elements')
l=['hello','python','learners']
f=open('welcome.dat','wb')
pickle.dump(l,f)
f.close()
