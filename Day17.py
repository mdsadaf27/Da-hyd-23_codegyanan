"""
mapping ---> dictionary --> collection of key-value pairs used to  store
related data --> json.APIs,database records
dict --> data = {}---> data = { key : value}
dictionary is a mutable, indexed throgh keys , ordered , hetrogenious.
key must be unique( int , str , float values ..)

"""

details ={}
print(type(details))

details = {'id ': 'CGH4022','Name':'manasa',
           'gender': 'f','age':20,
           'batch':'DA23','place':'hyd'}
print(details)
print(len(details))

# acess the data  from dictionary
#details{0]# key error
print(details.keys()) # it returns keys keys from the dictionary
#print(details['Id'],details['Name'])
#if key name is not matching /invalid
details ['marks'] = []
print(details)
print(type(details['marks']))

details['marks'].extend([15,20,25,20,20])
print(details)

# create  a key value pairs  of practice section

details['ps'] = ('tuesday','thursday','saturday')
print(details['marks'][2])
# accessing 2nd day of practice session
print(details['ps'][1])

details['mock_interview'] =('MONDAY','WEDNESDAY','FRIDAY')
#oprations --->mutable,indexing through keys membership
""""
print('WEDNESDAY' in details)
print('mock_interview' in details)
for i in details:
    print(i) # returns key one by one 

for i in details.keys():
    print(f'key ={i}')
    print(f'value ={details[i]}')

#keys() --> returns keys from the dictionary
for i in details.values(): # return value from dictionory 

for i in details.items(): #returns a key value pair  in tuple
    print(i)
    
for key,value in details.items():
    print('key is {key}')
    print(f'value is {value}')
    

# update---------> updating the dictionary with key value pairs
details.update({'marks':[],
                'ps':('tuesday','thursday','saturday')})
print(details)
details['marks'].extend([25,30,25])
print(details)
marks = list(map(int,input(" enter the marks:").split(',')))
print(marks)
details['marks'],extend(marks)
print(details)

"""
print(details.keys())
print(details.get('Name'))
print(details.get('branch')) # it returns NOne as we dont have branch as key


details.setdefault('branch')# if key is not present it inserts int dict 
print(details)
details['branch'] = 'CSE'
print(details)

print(details.setdefault('Name'))

print(details.pop('branch'))
print(details.keys())


#--->pop()
'''
print(details.pop('Branch')) #we need to mention key
print(details.keys())
'''

#--->popitem()-->removes and returns a key value pair as a 2-tuple
'''
print(details.popitem())
print(details.popitem())
'''

#--->del()
'''
del details['id']
print(details.keys())
'''

#--->clear()
'''
details.clear()
print(details)
'''

#--->fromkeys()-->creates a dictionary from iterable(lists,tuples,sets,strings)
'''
data=['nikki','rishi','data']
a=dict.fromkeys(data) #creates a dictionary but values set to None
print(a)
a['nikki']=21
print(a)
c=dict.fromkeys(['CGH3882','CGH1234'],['Code','gnan'])
print(c)
'''

#Task: create a dictionary with your personal details, similar to your codegnan profile













    
