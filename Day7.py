
"""
#---->usage of the  else with for 

work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0 #target variable 
current_streak = 0 
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak}')

work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0 #target variable 
current_streak = 0 
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak}')
# in this case when the entire loop execution is done we get result of  ekse back
#same program with break usage 

work_log = [0,1,1,1,0,1,0]
#result variable -->longest_streak
longest_streak = 0 #target variable 
current_streak = 0 
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'Longest Streak is {longest_streak}')

            
    else:
        current_streak = 0 #streak breaks
else:
    print(f'Longest Streak is {longest_streak}')
print (f'excecution done')

#for else with notification senario

notification = [0,0,0,0]
for natification in notification :
    if notification == 1:
        print("unread notification")
        break
else:
    print("all caught up")
    
#for else with notification senario

notifications = [0,0,1,0]
for notification in notifications :
    if notification == 1:
        print("unread notification")
        break
else:
    print("all caught up")

    
#for else with notification senario


notification = list(map(int,input("enter the values 0:1:").split(',')))
for natification in notification :
    if notification == 1:
        print("unread notification")
        break
else:
    print("all caught up")


#wh the
#wile --> it relies on condition,it will be completly executed until
#condition is satisfied
 syntax
while < conditiom >:
    statment(s)......
    .....
    ....
  
#controll c to stop infinate loop
#it runs an infinate loop we need to press cntrl+c to stop 
while True:
    print("yes")
    

i=0 # intialised statement 
while i<=10:
    print(i)
    i=i+1
    
i=1 # to get a o/p from 123....
while i<=10:
    print(i)
    i=i+1
    
 # intialised statement
 #revers order 10 9 8 7....
i=0
while i<=10:
    print(10-i)
    i=i+1

i=0
while i<=10:
    print(10-i)
    i=i+1

#banking sinario---> pin authentication if more then 3 attpms acconcnt block

pin = "1234"
max_attempts = 3
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
pin = "1234"
max_attempts = 3
current_attempt = 0
while current_attempt <=max_attempts:
    entered_pin = input("enter the atm pin ")
    if entered_pin == pin:
        print("logic sucessful")
        break
        continue
    else:
        print(" entered is wrong....try again carefully")
        current_attempt +=1
else:
    print("account locked, try after 24 hours")



