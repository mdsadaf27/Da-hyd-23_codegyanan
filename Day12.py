'''
Strings are immutable
Strings---> CaseConversations,searchng,and findings,string testing methods,
replace,space removal
'''
#1.Searching,finding,replacing,joining--->
'''
a='Codegnan'
print(len(a))
print(min(a))
print(max(a))
'''
#--->Searching-->
'''
a='Codegnan'
b=a.index('g') #it returns the index position
print(b)
c=a.index('n') #it returns only the first occurance
print(c)
d=a.index('n',6) #it returns the next occurance
print(d)
#e=a.index('n',8) #ValueError
#print(e)
#f=a.index('t') #valueError
#print(f)
#for i in a:
    #print(a.rindex(i))
g=a.index('n',2,6)
print(g)
'''

#--->rindex()-->returns last occurance
'''
a='Codegnan'
b=a.rindex('g')
print(b)
c=a.rindex('n') #here 'n' is occuring 7th index
print(c)
#d=a.rindex('n',8)-->valueError
#print(d)
'''

#--->count()-->it returns the number of items object is repeating
'''
print('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we dont have 'w' in 'code'
print('nikhitha'.count('a'))
'''

#--->find()-->first occrance but it avoid error returns -1 if
#substring is not found
'''
print('Codegnan'.find('r')) #it returns -1
print('Codegnan'.find('n'))
print('Codegnan'.rfind('n'))
'''

#--->example-->
'''
a='DataAnalysis'
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
'''

#--->replacing,splitting,joining-->
#immutable-->which cannot be modified
#it only applicable only with the strings
'''
a='Codegnan'
a=a.replace('g','s')
print(a)
print('nikhitha'.replace('nikhitha','nikki'))
print(a.replace('x','nikki'))
'''

#--->splitting-->
'''
a='Code nikki python'
b=a.split() #by default if we have space it splits(returns list)
print(b)
print(len(a))
print(len(b))
c='Code,nikki,python'
d=c.split()
print(d)
e=c.split(',')
print(e)
'''

#--->Joining-->join() it need an iterable,concatenate any number of strings
'''
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('nikki'))
print(' '.join('nikki'))
'''

#2.String testing methods(boolean)
#isalpha(),isalnum(),isdigit(),isupper(),islower()...
'''
a='Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else false
b='Codegnan'
print(b.isalnum())
c='Codegnan'
print(c.isalpha()) #returns True only for alphabets
#print(c.isdigit()) #returns True only for digits else false
#print(c.isupper()) #returns True only for all upper letters else false
#print(c.islower()) #returns True only for all Lower letters else false
d='123456789'
print(d.isdigit())
print(d.isnumeric()) #this has upper edge(numbers,fractions,romans)
e='NIKHITHA'
print(e.isupper())
f='nikki'
print(f.islower())
'''

#--->startswith()-->how its starting
'''
print('Codegnan'.startswith('C'))
print('Codegnan'.startswith('g',4))
print('Codegnan'.endswith('f'))
'''

#--->space removal-->strip() removes leading and trailing spaces
'''
a='Codegnan'
print(a.strip())
b=input('Enter the string:').strip().lower()
print(b)
'''

#--->zfill() filling with zeroes as per the numeric string
'''
print('123'.zfill(7))
'''
#--->center() is moving to center by creating some space
'''
print('hai'.center(6))
print('hai'.center(5,'#'))
'''
#--->ljust() and rjust()-->are for alignment
#check length and modify the width accordingly
'''
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
'''



