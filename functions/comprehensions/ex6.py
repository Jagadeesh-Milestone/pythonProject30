#write a program for printing the second largest number
#in a list of numbers.
#write a program for check whether the entered input is palindrome
#or not.
#write a program for printing odd numbers and even numbers from
#a list of numbers.
#take a list of strings and print the strings which have 'a' in it.
x=['hello','book','car','pencil','bangalore']
for i in x:
    if 'a' not in i:
        print(i)

l=[1,2,3,4,5,3,2,4,6,8,9,4,4,6]
l.sort()
print(l[-2])
print(l[1])

text=input('please enter any text:')
x=reversed(text)
if list(text)==list(x):
    print(text,'is a palindrome')
else:
    print(text,'is not a palindrome')

m=[1,2,3,4,5,6,7,8,9,10]
n=[]
for i in m:
    if i%2==0:
        print(i,'is an even number')
    else:
        print(i,'is an odd number')