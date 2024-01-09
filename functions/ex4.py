# * args:
#it is used to pass multiple values to a single argument.
#if you dont know how many values you are passing then put a *
#before the argument name.
def d1(*a):
    print(a)
d1(10,20,30,40,50)

def d2(*students):
    print(students)
    print('the tallest student is:',students[0])
d2('hari','manoj','suresh','naresh')

#** kwargs:
#it is used to pass the values as keyword and value.
def d3(**users):
    print(users)
    print('the shortest student is:',users['user1'])
d3(user1='suresh',user2='jagadeesh',user3='arshad')
