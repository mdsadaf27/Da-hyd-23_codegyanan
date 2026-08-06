"""
total = 0

for i in range(1, 5):
    product = input("Enter product name: ")
    price = int(input("Enter product price: "))
    total = total + price

print("Total Bill =", total)



products=list(map(int,input().split(',')))
total = 0
for i in products:
    total = total+i
print(total)



password = input("Enter password: ")

letters = 0
digits = 0
special = 0

for ch in password:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Total characters:", len(password))
print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)

# Task ---> Password

password = input("Enter password: ")

upper = 0
lower = 0
digits = 0
special = 0

for ch in password:
    if 'A' <= ch <= 'Z':
        upper += 1
    elif 'a' <= ch <= 'z':
        lower += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Special Characters:", special)

email = input().split()
for mail in email:
    print(mail.split("@")[1])

"""
#task the movie names with serial numbers
for i in range(1, 6):
    movie = input("Enter movie name: ")
    print(i, ".", movie)
