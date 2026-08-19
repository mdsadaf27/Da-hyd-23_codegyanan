  
'''
tokens,datatypes-->control flow statements--if,elif,else,
for,while,break,continue...
procedure oriented programming
'''

#1.Functions-->a function is a block of code which performs a specific task
#it is a resusable block of code/group of statements where we define using "def keyword"
'''
Advantages of functions are-->
1.code reusability
2.code maintainbility
3.ease of debugging
4.avoiding code duplication...
5.modularity

Syntax-->
def fname(parameters):  #function definition
    """Doc String""" #description function
    statements(s).....   #function body
    ..................
    return value(s)...
fname(args)   #function call
'''

#2.To perform sum of given objects
#we prefer return-->
'''
def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,3)) #addition
print(add('Code','gnan')) #concatenation
print(add([12,5],[12,34])) #merging

c,d=map(int,input('Enter the values:').split(','))
print(c,d)
print(add(c,d))
'''
#--->same example without return keyword
'''
def add(a,b):
    """Sum of objects"""
    print(a+b)
add('Code','gnan')
add(23,34)
#print(add(23,34))-->it returns result along with None
'''

#3.usage of return keyword
'''
name,age,salary='nikki',21,20000
def details():
    #return name,age,salary
    #return 'codegnan'-->#codegnan will be printed
    #return 23+45+34-->#it will print 102 as output
    #return-->it returns None as output
print(details()) #it stored in tuple,bcoz we passed more than 2 objects at a time

#without defining the values when we try to print it gives NameError
'''

#4.There are 5 types of arguments:
'''
1.positional arguments
2.default arguments
3.keyword arguments
4.varibale length arguments (*args)
5.keyword variable length arguments (**kwargs)
'''

#--->positional arguments-->number of arguments in function definition should match with function call
#(order has to be maintained)
'''
def details(name,place):
    """To store the details"""
    #name='Codegnan'
    #place='hyderabad'
    #return name,place
    print(f'Name is: {name}')
    print(f'Place is : {place}')
#print(details('nikki','ongole'))
#print(details('rishi','ongole'))
#print(details('vizag',34,'shyam'))-->it raises TypeError as only 2 arguments to be given
c,d=map(str,input('Enter the values:').split(','))
details(c,d)
'''

#--->default arguments-->we can make argumentsas default but not first arguments as default
#first case
'''
def grocery(item,price):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
'''

#second case
'''
def grocery(item,price=35):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread') #by default we had given price as 35
'''

#Third case
'''
def grocery(item='Cheese',price=100):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread')
grocery()
'''

#fourth case
#we cannot make first one as default,it raises syntaxError
#if the parameter is single then we can pass the default value to it
#if more than two parameters we cannot make default value for the first one
'''
def grocery(item='Burger',price): #non default is always follows default
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread')
'''

#--->keyword arguments-->whenever we wanted to specify the name of argument
'''
def employee(name,salary,role,place='Codegnan'):
    """Keyword argument usage"""
    print(f'Employee name is : {name}, Role is : {role}, and Salary is : {salary}, Work place is : {place}')
employee('nikki',20000,'Admin')
employee(salary=25000,role='Frontdesk',name='rishi')
employee("sadaf",25000,'IT','Cognizant')
'''












































