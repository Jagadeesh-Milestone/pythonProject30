#raise an exception:
#we can raise our own exceptions by using raise an exception.
#x='jagadeesh'
##if type(x) is not int:
  #  raise Exception('assign only integers')
##else:
   # print(x)
   ## print('hello world')
number=int(input('please enter any number:'))
if number<=0:
    raise Exception('enter only positive numbers')
else:
    print(number)