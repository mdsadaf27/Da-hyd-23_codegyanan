"""
Task 1: Batsman Innings Analysis
Question: Write a Python program using a for loop to calculate the total score of a batsman's innings. Also count:
Number of boundaries (4s and 6s)
Number of dot balls (0s)
Use the following list:
list = [4, 6, 1, 0, 2, 4, 0, 6]

list = [4,6,1,0,2,4,0,6]

total = 0
boundaries = 0
dotballs = 0

for i in list:
    total = total + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dotballs = dotballs + 1

print("Total Score =", total)
print("Boundaries =", boundaries)
print("Dot Balls =", dotballs)


task-2 password 
pin = input ("enter the number: ")
max_attempts = 5
current_attempt = 0
while current_attempt <=max_attempts:
    entered_pin = input("enter the atm pin ")
    if entered_pin == pin:
        print("logic sucessful")
        break
    else:
        print(" entered is wrong....try again carefully")
        current_attempt +=1
else:
    print("account locked, try after 24 hours")
"""
password = "159"
count = 0

while count < 3:
    user = input("Enter Pattern: ")

    if user == password:
        print("Unlocked")
        print("*     ")
        print("  *   ")
        print("    * ")
        break
    else:
        count += 1
        if count < 3:
            print("Wrong Pattern! Try Again.")
        else:
            print("Wrong Pattern!")
            print("Try again after 30 seconds.")
