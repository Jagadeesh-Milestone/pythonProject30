#ATM use case:
#welcome message(some space)
#select language(3 options)/ if it is 4 error(select correct option)
#1---we will continue in telugu
#2---we will continue in english
#3---we will continue in hindi
#4---error
#name(input)
#hello,name,
#enter your 4 digits pin
#pin<4 digits or pin>4 digits (error)
# please select the option from below menu
#balance=50000
#1--check balance
#2--deposit amount--amount>0,balance+deposit amount
#3--withdraw amount--amount>0,withdraw amount<balance,balance-withdraw amount
import time
t=time.ctime()
print(t)
print('\t\t\t welcome to ICICI Bank ATM')
name=input('please enter your name:')
print('hi',name)
while True:
    print('please select your language:')
    print('1.telugu\n2.engilsh\n3.hindi')
    language = int(input('enter your language:'))
    if language not in range(1,4):
        print('enter valid option')
        break
    else:
        pass
        balance=50000
        pin=input('please enter your 4 digits pin:')
        if pin.isdigit() and len(pin)==4:
            print('select the following options')
            print('1.account balance\n2.deposit amount\n3.withdraw amount')
            option=int(input('enter your option:'))
            if option==1:
                print('your account balance is:',balance)
            elif option==2:
                deposit=int(input('enter the deposit amount:'))
                if deposit>0:
                    print('the amount has been deposited successfully')
                    print('updated account balance is:',deposit+balance)
                else:
                    print('enter the amount greater than 0')
                break
            elif option==3:
                 withdraw=int(input('enter the amount to withdraw:'))
                 if withdraw>0 and withdraw<balance:
                   print('your transaction of',withdraw,'has been successfull')
                   print('the updated balance is:',balance-withdraw)
                 else:
                   print('enter the amount greater than 0 or amount less than balance')
                 break
            else:
             print('enter the valid option')
             break
        else:
            print('enter valid pin')
