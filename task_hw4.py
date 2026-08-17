 # Task 1: Student Marks Manager
"""
marks = []
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

print("\nOriginal marks:", marks)
marks.insert(0, 90)
marks.extend([75, 85])
print("After adding 90, 75 and 85:", marks)
if 75 in marks:
    marks.remove(75)
    print("75 was removed.")
else:
    print("75 was not found.")
removed_mark = marks.pop()
print("Removed final mark:", removed_mark)
print("Final marks:", marks)
print("Number of marks:", len(marks))

# Task 2: Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

print("Original list:", numbers)
numbers.sort()
print("Ascending order:", numbers)
numbers.reverse()

print("Descending order:", numbers)

search_number = int(input("\nEnter a number to search: "))

if search_number in numbers:
    print("Number found!")
    print("Count:", numbers.count(search_number))
    print("First index:", numbers.index(search_number))
else:
    print("Number not found.")
print("\nSmallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))


# Task 3: Even and Odd Number Separator
'''
numbers=[10,15,20,25,30,35]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list:",even)
print("odd list:",odd)
print("first 3 numbers:",numbers[:3])
print("first 3 numbers:",numbers[3:])
copy_numbers=numbers.copy()
numbers.clear()
print("original numbers:",numbers)
print("copy numbers:",copy_numbers)
'''


# Task 4: Unique Name Manager
'''
names=['Asha','Rahul','Asha','John','Rahul']
x=set(names)
print(x)
x.add('Meera')
print(x)
x.update(("Arun","Priya"))
print(x)
if 'John' in x:
    x.remove("John")
print(x)
x.discard('John')
for i in x:
    print(i)
'''

#5.Course student comparision
'''
python_students={'Asha','Rahul','John','Meera'}
da_students={'Rahul','Meera','Arun'}
a=python_students.union(da_students)
b=python_students.intersection(da_students)
c=python_students.difference(da_students)
d=python_students.symmetric_difference(da_students)
print('All Students:')
for i in a:
    print(i)
print('Students have both courses:')
for j in b:
    print(j)
print('Only Python:') 
for k in c:
    print(k)
print('Only one course:')
for m in d:
    print(m)
    
print("\nDA is subset of Python:", da_students.issubset(python_students))
if da_students.issubset(python_students):
    print("All DA students are also Python students")
else:
    print("All DA students are not Python students")

print("Python is superset of DA:", python_students.issuperset(da_students))
if python_students.issuperset(da_students):
    print("Python contains all DA students")
else:
    print("Python does not contain all DA students")

print("Both sets are disjoint:", python_students.isdisjoint(da_students))
if python_students.isdisjoint(da_students):
    print("There are no common students")
else:
    print("There are common students in both courses")

'''
