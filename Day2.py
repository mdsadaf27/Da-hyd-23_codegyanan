 #DAY "2"

#Tokens --> variables,punchuaters
# variable---> named memory location, its a palceholder for data
'''
#multiasssignment of variables
name,age,place='codegnan',7,'hydrabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='----')

#a,b=2,4,5 #valueerror as too many value too many values
#reeassigning variables

name = "afreen"
a,b=45,1.5
print(a,b)
a,b=b,a   #swapping
print(a,b,sep=',')

#deleting the variable
#del a variables 
#print(a)
#del a,b
#print(a,b)

#punchuaters (),{},[]
#[] for list
#() for tuples
#{} for dictionary , sets


name = "afreen";age=7 ;course='data_analysist'
print(name,age,course)

#sequence data types
#-----> numeric (int,float,complex),boolean,none
   #-->sequnces---> lists,tuples,sets,strings
      #--->frozensets,mapping(dict)
#NUMERIC type -->int,float,complex
#int datatype----> quntity,age ,
age=7
print(age)
print(type(age)) #type--->returns the data type of object
  # quntity=07 # it is not allowed
  #print(quntity)

  # FLOAT data type ---> temparature, salary, price
price=750.24;discount=2.5
print(price,discount)
print(type(price))


#complex numbers ----> it is combination of real and imagenary number
i2=4
data = 5+i2
print(data)


data =5+2j  #n j is a img representation
print (data)
print(type(data))



#boolean--->True/false

valid =True
print(type(valid))



error=False
print(type(error))


#typecasting--->Converting one type to another type
#python by defaualt follows implict type (we need not mention the datatype )

 #we will go for explicit convertion
#every built in data type is built in fuction
#int ,float ,complex,bool

#type casting --->int--->float , bool,complex
age=34
print(type(age))
b=float(age)
print(b)
c=complex(age) #returning true for existing data
print(d)
e=bool(0)
print(e)

#float --->type casting
age=33.2
print(type(age))
b=float(age)
print(b)
c=complex(age) #returning true for existing data
print(d)
e=bool(0)
print(e)



price=750.45
print(type(price))
d=int(price)
print(d)
print(type(d))
e=complex(price)
print(e)
f= bool(price)
print(f)

#complex-->type cast --->int floot bool
data=2+5j
print(type(data))
#b=initial #type error
#print(data)
#c=flooat(data)

'''
e=int(float(bool(45)))
print(e)

f=45+2.5+2+2J+False
print(f)
