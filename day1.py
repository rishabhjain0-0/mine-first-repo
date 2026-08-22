'''      #1
salary=50.5
print(salary)
print(type(salary)
'''
#2 
'''
a=2e2
b=2E2
c=2e3
print(a)
print(b)
print(c)
print(type(a))
'''
#3
'''a=3+5j
b=2-5.5j
c=3+10.5j
print(a)
print(b)
print(c)
print(a+b)'''
#4
'''a=True     #true is one and b is zero
b=False
print(a)
print(b)
print(a+a)
print(a+b)'''
#5
"""s1='hari'
s2="hari"
s3='''hari
is
great'''
print(s1)
print(s2)
print(s3)
print(s4) """
#6 creating a bytes datatype
'''x=[10,20,30,100,200]
y=bytes(x)
print(type(y))
print(y[0])
print(y[1])'''
#7 printing the byte data type values using for loop
'''x=[12,56,69,18,45]
y=bytes(x)
for r in y :
    print(r)'''
# some error statement which represents that the values that are assnged cannt be changed
'''x=[10,20,30,76]
y=bytes(x)
y[0]=30  '''# here im trying to change the value of 10 to 30 but now that it has been converted in bytes it cannot be changed
#7 creating a range of values using range 
'''a=range(5)
print(a)
for x in a :
    print(x)'''
#8
'''a=12
print(int("23")+a)
print("23"+str(a))

print(bool(23)+4) #any numberis true except 0 or none 
print(bool("")+4)''' #string is true except empty string
#8
'''a=5            #Type Conversion
print(float(a))
b=6.9
print(int(b))
print(str(a))'''
#9   nesting
'''a=10
b=20
c=-8
d=-7
e=((a if a<d else d) if a<c else (c if c<d else d))if a<b else ((b if b<d else d) if b<c else (c if c<d else d))
print (e)'''
# special operators
'''a=6
b=4
print(a**b)  # a to the power of b
print(a//b)  # divides and gives only the integer value
print(a%b)'''   # divides and gives the remainder 
# and function
'''print(0 and 4)
print(4 and 7)
print(21 and 0)
print(15 and 8)'''
# some more operators (also works for-,*,%,/)
'''a=12
a+=5
print(a)'''

