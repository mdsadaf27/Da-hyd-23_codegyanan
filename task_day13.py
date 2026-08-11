# Task 1: Text Case Converter
"""
text = input("Enter text: ")

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("Capital:", text.capitalize())
print("Swap:", text.swapcase())

if text.isupper():
    print("Uppercase")
elif text.islower():
    print("Lowercase")
else:
    print("Mixed case")

# Task 2: Username Validator

while True:
    name = input("Enter username: ")

    if name == "quit":
        break

    if name.isalnum():
        print("Only letters and numbers")
    else:
        print("Has special characters")

    if name[0].isalpha():
        print("Starts with a letter")
    else:
        print("Does not start with a letter")

    if name.isidentifier():
        print("Valid username")
    else:
        print("Invalid username")
        
# Task 3: Student Report

print("STUDENT REPORT")

for i in range(3):
    name = input("Name: ")
    marks = int(input("Marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(name, marks, grade)
    """
# Task 4: Character and Text Analyzer

text = input("Enter text: ")

letters = 0
digits = 0
spaces = 0

for x in text:
    if x.isalpha():
        letters += 1
    if x.isdigit():
        digits += 1
    if x.isspace():
        spaces += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Lowercase:", text.islower())
print("Uppercase:", text.isupper())
print("Title case:", text.istitle())
