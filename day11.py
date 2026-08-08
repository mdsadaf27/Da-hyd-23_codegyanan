#passwod secret code  program
"""
correct_code = "159"

while True:
    code = input("Enter secret code: ")

    if code == correct_code:
        print("Correct")
        break
    else:
        print("Wrong")

otp = "2727"
attempt = 0

while attempt < 5:
    code = input("Enter OTP: ")

    if code == otp:
        print("Correct OTP")
        break
    else:
        print("Wrong OTP")

    attempt = attempt + 1

if attempt == 5:
    print("OTP Expired")
    print ("try after 10 min")
    


count = 0

while True:
    food = input("Enter food: ")

    if food == "exit":
        print("Thank you for ordering!")
        print("Total orders:", count)
        break

    print(food, "added to order")
    count = count + 1
"""
secret = 'python'
attempt = 0

while attempt < 3:
    game = input('Enter the game name: ')
    if game == secret:
        print("You win the game")
        break
    else:
        print("Try again...")
        attempt += 1
else:
    print("You lost the game")
