'''
Lists,tuples...
'''
#List-->mutable,ordered,heterogenous
#index(),count(),copy(),sort(),reverse()

#---->index()
'''
details=['Codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('Codegnan'))
details.extend([7,21,45,21])
print(details)
print(details.index(21)) #it returns first occurance
print(details.index(21,6))
#print(details.index('Python'))-->it raises valueError
'''
#--->count()
'''
print(details.count(21))
print(details.count('python'))


#-------------> yestarday's task code
data=['codegnan','saketh','python','java']
for i in data:
    print(data.index(i),':',i)

#another way-->
for obj in range(len(data)):
    print(obj,':',data[obj])


#copy() ---> shallow copy of the given collection
data=['codegnan','saketh','python','java','afreen']
new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'agintic ai'
print(new)
print(data)

data.append('saketh')
print(new)
print(data)

data.remove('saketh')
print(new)
print(data)

data.extend('saketh')
print(new)
print(data)

data.pop(4)
print(new)
print(data)

data.append('saketh')
print(new)
print(data)

data = [1,4,5,[21,34,45,],23]
print(data)
new = data.copy()

new[3] = "agents"# whenever we make changes in nested liast original will also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)

'''
#marks = [14,24,-45,27,35]
#print(marks)
#print(marks.sort()) #retuns none
#print(marks) # return in ascending order
#marks.sort(reverse = True )# returns in decending oreder
#print(marks)
#marks.insert(.2,'code')
#marks.sort
#reverse() ---> returns in revers order
#marks.resverse()
#print(marks)
#print(marks[::-1])

# type(), len(), max(), min(),print()
#print(sorted('codegnan'))# returns list in ascending order
#print(sorted(['code','23',23,45]))#raises error



#tuples are also indexed, ordered, hetrogenous, immutable collection
#imenssion,cordinates,database record we prfer () for tuple notation
"""
a = ()
print(type(a))
print(len(a))

dimentions = 1.5,2.5
print(type(dimentions))
print(len(dimentions))

#operation --> indexing, sclicing, string, membership,mergging, merging,repetation

courses = ('PFS','JFS',('DA'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
#courses[2] =23 tuples are immutable
courses[-1].append('codegnan') # we can make any modifications inside list
print(courses)
# create a nested tuple as above and work on sclicing, striding, and list function
print('PFS' in courses)
d = courses * 2
print(d)
e = courses + (2,3,4,5)# merging
print(e)

# tuples are immutable  ----> count(),index()
#--->tuples immutable-->count(),index()
courses=('PFS','JFS',('DA','DS'),'agentic ai',[100,6,6])
print(courses.index('agentic ai'))
print(courses.count('Agents'))

#print(courses.sort())-->attributeError
#sort is in list not in tuple

print(sorted(courses[-1]))

#print(sorted(courses))-->it raises an error, as we have an mixed type

d=tuple(sorted((23,67,47))) #TypeCasting
print(d)


# accept group of integers sapce separated
a, b = map(int,input("enter the values").split())
print (a,b)

a = map(int,input("enter the values").split(','))
print(a)

print(9+4)
eval()#fuction can take any kind of input
print(eval('9+4'))


"""
print('9+4')
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input("Enter a list"))#in this case u can exactly enter data as list
print(a)
print(type(a))
'''

#Task:Take a user input as string,do this in two ways..
'''
1) give the count of each repeating character
Test case 1 :programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index =[6,7]
'''
      










