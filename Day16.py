'''
sequences-->strings,lists,tuples,set,frozenset
mapping-->dictionary(dict)-->{}
'''

#1.Sets-->a set is a 'unique' collection of elements(objects),unordered collection
#set is a mutable,we use hashing and it is unindexed,heterogeneous
#we cannot keep 'list' in the set
#set(),{} is a representation
#a={}-->it is an empty dictionary
'''
a=set()
print(type(a))
stud_ids={123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])-->TypeError
print(234 in stud_ids)
#print(stud_ids*2)-->TypeError->two sets cannot me merged and cannot be repeated
'''

#2.Methods/functions of a set
#and also we cannot give set inside a set
'''
data={12,3,4,5,(12,3,4),'nikki'}
print(data) #no list inside a set (hashing technique follows) as lists are mutable
print(len(data))
for i in data:
    print(i)
'''

#--->Methods on set-->add(),update(),remove(),discard(),pop()
#--->add() will insert an element into the set,it can be anywhere but only in unique
'''
names={'nikki','rishi','sadaf','nithya'}
print(len(names))
names.add('python')
print(names)

#names.add('nikki','poll')--->pass a error bcoz we should add only single element to the set
#print(names)

names.add(('poll','police')) #passing a tuple
print(names)
'''

#--->update()
#in update we can keep any braces in the update
'''
names={'nikki','rishi','sadaf','nithya'}
da_names={'nani','nikki','keerthi','baji'}
names.update(da_names)
print(names)
print(da_names)
print(len(names))
print(len(da_names))

da_names.update(names)  
print(names)
print(da_names)
print(len(names))
print(len(da_names))
'''

#--->remove(),discard(),pop(),clear()
#remove() removes an element from the set (it must be a memeber)
'''
da_names={'nani','nikki','keerthi','baji'}
da_names.remove('nani')
print(da_names)
#da_names.remove('nani')-->KeyError-->bcoz we already removed that element 
'''

#--->discrad()
#if there is a member it will discard
#if there no member in that list it doesnt raise any error just it print the list again
#it will ignore
'''
da_names.discard('nani')
print(da_names)
'''

#--->pop()
#we cannot tell which element will be pop
'''
da_names={'nani','nikki','keerthi','baji'}
da_names.pop()
print(da_names)
da_names.pop()
print(da_names)
print(da_names.pop()) #removes and returns an arbritary element
'''

#--->clear()
#all the elements will be clear and returns set() in the output
'''
da_names={'nani','nikki','keerthi','baji'}
da_names.clear()
print(da_names)

da_names.add('nikki') #we should pass only single element in this we cannot pass []
print(da_names)
print(len(da_names))
'''

#--->copy()-->creates a shallow copy of set (independent of each other)
'''
da_names={'nani','nikki','keerthi','baji'}
d=da_names.copy()
print(d)
d.update({'python','java'})
print(d)
'''

#3.mathematical operations-->union(),intersection(),difference(),symmetric_difference
#issubset(),issuperset(),isdisjoint()
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}

#--->union()
'''
event=da_23.union(da_24)
print(event)
print(len(event))

e=da_23 | da_24 # ( '|' is for union)
print(e)

d=da_24.union(da_23)
print(d)
print(len(d))
'''


#--->intersection()
'''
common=da_23.intersection(da_24)
print(common)
print(len(common))

b=da_23 & da_24 #( '&' is for intersection)
print(b)

a=da_24.intersection(da_23)
print(a)
print(len(a))
'''

#--->update()-->intersection with update and there is no union in update
'''
common=da_23.intersection_update(da_24)
print(common) #it returns None here
print(da_23) #common elemenrs are finally stored
'''

#--->difference()
#the elements which are different those will be printed
'''
print(da_23)
print(da_24)
diff=da_23.difference(da_24) #it prints all the elements which are in da_23
print(diff)

f=da_24.difference(da_23) #it prints all the elements which are in da_24
print(f)
'''

#--->symmetric_differece()
#it removes all the common elements and prints all the remianing elements
'''
sym=da_23.symmetric_difference(da_24)
print(sym)

h=da_23 ^ da_24 #NOT
print(h)
'''

#--->issubset() and issuperset()-->checks for all elements to be present in other set
'''
da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
'''

#--->isdisjoint()-->returns false for sets having common elements
'''
print(da_23.isdisjoint(da_24))
'''

#length of unique student ids in a class, where user can enter first input
#he should be giving number of student_ids,he will enter student_ids
'''
n=(int(input('Enter numbers:')))
student_ids=input().split()
print(student_ids)
result=set(student_ids)
print(result)
print(len(result))
'''
