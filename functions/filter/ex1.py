#filter:
#this method filters the given sequence with the help of a function
#that is checked with the each element of a sequence.
l=['a','b','c','d','e','f','g','h','i']
for i in l:
    if i in ['a','e','i','o','u']:
        print(i,'is an vowels')
    else:
        print(i,'is not an vowels')

vowels=['a','e','i','o','u']
#using filter:
def d1(n):
    if n in owels:
        return True
    else:
        return False
f=filter(d1,l)
print(list(f))

