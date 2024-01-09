#datatypes:
#It is the type of data which we are passing into a python object.
#python supports six types of data types.
#number datatypes--int,float,complex
#sequences--list,tuple,range,string
#boolean--True and False
#mapping--dictionary
#set--set,frozen set
#binary--bytes,bytearray

#number datatypes:
#int:
#In python any real number will be treated as an integer.
a=10
print(a)
print(type(a))

#float:
#In python any decimal number will be treated as a float value.
b=10.3
print(b)
print(type(b))

#complex:
#It is the combination of a real number and an imaginary number.
c=5+6j
print(c)
print(type(c))
print(c.imag)
print(c.real)

#binary numbers:
#they starts with 0b
#base value is 2
#possible values are 0,1
a=2
print(bin(a))

b=0b1010
print(b)

#hexa decimal numbers:
#they starts with 0x
#base value is 16
#possible values are 0-9,a-f
c=16
print(hex(c))

d=0xa
print(d)

#octal numbers:
#they starts with 0o
#base value is 8
#possible values are 0-7
e=8
print(oct(e))

f=0o10
print(f)