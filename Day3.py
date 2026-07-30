#numeric data type---> int bool float complex
#input formatting--->Acceptting input from the user -->inpt>
#accepting integer input from use
  #by default input()acccepts any input--> string
#int(input())--->will accept only intergers
"""
age=int(input('enter the age:'))
print(type(age))

#float(input()) ----> integer fl0at values
age=float(input('enter the age:')
print(age)
print(type(age))          



# accept group of values
a=input().split()
print(a) #inter spaces in output
#comma seprates value
#comma seprated
a=input("enter the value :").split(',')
print(a)
"""
"""
#list of integers
marks=list(map(int,input("enter the value").split(',')))
print(marks)
"""

"""
#now we want to acces 2 valus from user
age,salary=(map(int,input("enter the value").split(',')))
print(age)
print(salary)
"""
"""
#single input --->int(input))
#two inputs -->a,b=map(int,input().spilt(','))
#any number results as lists-->a=list(map(int(),input().split(','))
 #float
age,salary=(map(float,input("enter the value").split(',')))
print(age)
print(salary) 
"""
# accepting input from user --->int float -->input formatting
#oprators--> oprators perfom operations b/w values (oprands)
#they are 7 types -->arthemetic,asssigments , comparrision,(relationship)
#membership,identify,logical,biwise
#arthemetic oprators -->arthemetic oprations
""""
print(5+3)
print(5-3)
print(5*3)
print(5/3)#float value# if we use / devide then it will show quotient
#float
print(5%3)#if we use persentage simbol it will give reminder of the sum 
print(5**3)
print(5**2)
"""
"""
#task accept integer input as lenth, breath --> find the area of rectangle
#area lenght*breath
length=int(input('enter the value'))
breadth=int(input('enter the value'))
area=length*breadth
"""
"""
#assignment operators --->assign the value
#=,+=,_+
#update the value
a=20
print(a)
a=a+5
print(a)
b=20
print(a+b)
b-=5
print(b)
## task:*=,/=,//=,%=,**= work out
"""
"""
#comparition oprators# always output comes is only boolean
#==,(eqaul to),!=not eqal to ,< less then ,>grater then
#<= lessthen or eqal to, >= greater then qual to

age=25
print(age==25)# returns to boolean
print(age!=35)
print(age<=25)
print(age>=33)

print(-22<-7)
"""
# membership oprators--->in,not in--->boolen
#it cheacks for the existance of an object in a collection
marks =[22,33,55,66,777,]
print(33 in marks)
print(25 not in marks)
print ('code in coders')

#logical oprators--> logical decission making --. and ,or,not
# and --> all condition satisfy
#or --> any one conditions can satisfy

a=(25 in [23,22,44]) and 45<56
print(a)
b=45>56 or 25<=45
print(b)
c=not(True)
print(c)

# identity oprators -->check for identity of an object -->id()
a=24
b=33
print(id(a))
print(id(b))
c=22
print(id(c))

a=[1,3,4,5]
print(id(a))




