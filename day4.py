#identity oprator ---> checks the identity of an object --> id()
# integer objects are not change able
"""
a=4
b=5
print(id(a))
print(id(b))
c=9
print(id(c))
print(a is c)
print(5==5)

a=[1,3,5,7,11]
b=a
print(id(a))
print(id(b))
c=[1,3,5,7,11]
print(id(c)) 

#as we have lists (mutable collection botha and c will have difftet ids but valus are diffrent )
print(c is a)#o/p false
print(c==a)#o/p true
"""

#note important for da (bitwise)

#>>> bit bise oprators
#-->persorm bitwuse oprations over oprands

#&,|,^(xor), shiftting oprators(<<,>>)or
"""
#number will be converted into binary format
print(5&3)#both 5 and 3 to be converted binary and bitwise and oparands
print(5|3)#bitwise
print(5^3)# bitwise XOR
print(5 and 3) # here and is logical oprator checks for both existance
print(5 ^ 3)
print (5 or 3)
"""
"""
"""
""""
#left shift opators <<,right shitt >>>
print(5<1)# false comparison

print(5<<1)#left shift opration BY 1 POSITION
print(15<<2)#convert 15 binary and perform 2 times left shifting

print(15>>2)#same 2 times right shifting 

"""
#input formating -->input,int(input()),float(intput())
#single input
#group of integers -->list(int,input()),split(',')
"""
name=input("enter the names:").split(',')
print(name)

name1,name2=map(str,input("enter the friends names:").split(','))
print[name1,name2]                
"""
"""
#tokens-->numeric datatypes--.oprations
"""
#conditional statments--> if ussage
"""
Syntax:
if<condition>
  statement(s)...
   ....
"""
"""
#age=15
age=int(input("enter the age:"))
if age >=18:
    print("your age is")


#else keyword

Syntax:
if<condition>
  statement(s)...
   ....
   
if else 
  statement(s)...
   ....
"""
"""
#voter elgibility
#--->tocheck voter elgibility and give acces
age = int(input("enter the age:"))
if age>18:
    print("you have voter elgibility and age is",age)
    print("access granted")
else:
    age = 18-age
  #  print("you dont have elgibility")
  print("you need to wait more ",age,"years")
"""
"""
age = int(input("enter the age:"))
if age > 0:
    if age>18:
        print("you have voter elgibility and age is",age)
        print("access granted")
    else:
        age = 18-age
        print("you dont have elgibility")
        #print("you need to wait more ",age,"years")
else:
    print("you have entered a -ve value/zero enter only +ve")

"""
#task:student marks and grade analyzer
#90-100--->'A'
#80-89-->'B'
#70-79--'C'
#60=69-->'D'
#50-59-->'E'

marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    print("Your grade is A")
else:
    if 80 <= marks <= 89:
        print("Your grade is B")
    else:
        if 70 <= marks <= 79:
            print("Your grade is C")
        else:
            print("Fail")























