 # Task 1: Student Marks Manager
"""
marks = []

# Accept 3 marks
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

# Sort in ascending order
numbers.sort()

print("Ascending order:", numbers)

# Reverse to descending order
numbers.reverse()

print("Descending order:", numbers)

search_number = int(input("\nEnter a number to search: "))

if search_number in numbers:
    print("Number found!")
    print("Count:", numbers.count(search_number))
    print("First index:", numbers.index(search_number))
else:
    print("Number not found.")

# Numerical summary
print("\nSmallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers))


# Task 3: Even and Odd Number Separator

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []
for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Original list:", numbers)

print("\nEven numbers:", even)
print("Odd numbers:", odd)
print("\nFirst three values:", numbers[:3])
print("Last three values:", numbers[-3:])
backup = numbers.copy()
numbers.clear()

print("\nOriginal list after clear():", numbers)
print("Backup list:", backup)


# Task 4: Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
unique_names = set(names)

print("Unique names:", unique_names)

# Add Meera
unique_names.add("Meera")

# Add Arun and Priya together
unique_names.update(["Arun", "Priya"])

print("\nAfter adding names:", unique_names)

# Check whether John exists
if "John" in unique_names:
    unique_names.remove("John")
    print("John was removed.")
else:
    print("John was not found.")
unique_names.discard("David")

# Display every unique name
print("\nFinal unique names:")

for name in unique_names:
    print(name)
    """
# Task 5: Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

# Union
all_students = python_students.union(da_students)

# Intersection
both_courses = python_students.intersection(da_students)
only_python = python_students.difference(da_students)
only_one_course = python_students.symmetric_difference(da_students)
da_is_subset = da_students.issubset(python_students)
python_is_superset = python_students.issuperset(da_students)
courses_are_disjoint = python_students.isdisjoint(da_students)


print("Students in both courses:", all_students)
print("Students learning both courses:", both_courses)
print("Students only in Python:", only_python)
print("Students in only one course:", only_one_course)

print("\nIs DA a subset of Python?", da_is_subset)
print("Is Python a superset of DA?", python_is_superset)
print("Are the two courses disjoint?", courses_are_disjoint)


# Use loops to display results

print("\nAll students:")
for student in all_students:
    print(student)

print("\nStudents in both courses:")
for student in both_courses:
    print(student)

# Conditions to explain relationships

if da_is_subset:
    print("\nDA students are completely inside Python students.")
else:
    print("\nDA students are NOT completely inside Python students.")

if courses_are_disjoint:
    print("The two courses have no students in common.")
else:
    print("The two courses have students in common.")
