#control stataments --> controlflow excecution of the program
##        --> conditional stataments --->if elif else

#   ----> reptation statements ---> for while (for with else)
#  jummping statments --> break continue  pass

#looping--->loops are helpful for repitation (automative tasks)
#syntax for keyword
# for keyword will be helpful to itarate over a sequnce/ranage
"""
for(<temp_var>in sequnce/range function:
statement......
...
#range function (start,stop,step)

#by defalut range picks o as start value 
for i in range(10):
    print(i)
#in abve case we got 10 itration


for i in range(1,10):
    print(f"value of i is {i}")

for i in range(1,10):
    if  i > 5:
        print(f"value of i is {i}")


#now i want only even conditions which we used in before program

if  i > 5 and i%2==0:
    print(f"final value of i is ---> {i}")



# range start stop step ----> here stop --->interval..

for i in range(1,10,4):
    print(i)
    print("done")


for i in range(-10,0,1):
    print(i)
    print("helloo ")

#[] we genarelly lits
names = ['sadaf','sai','nikki']
for name in names:
    print(name)

names = ['sadaf','sai','nikki']
for name in names:
    print(name)
#print("student name is {name}")
    if name == "sadaf":
        print(f"student name is {name}")

result = 0
for i in range(11):
    result = result + i
    print(f" now the result is {result}")
    print (f" sum of 10 mumbers {result}")
"""
#understand the usage with fitness strek example \
# workout --->1 work out missed -->
work_log = [0,1,1,1,0,1,0]
# result variable -->logest_strek
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak +1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
        
        
#Loops --> Loops are helpful for repetition (Automative tasks)
#for keyword will be helpful to iterate over a sequence / range
#Syntax for (for keyword):
'''
for <temp_var> in sequence/range:
    statement(s)....
    .......

#range(stop) -->default 0 ends at stop-1
#range(start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations 
for i in range(1,10):
    #if i > 5:
        #print(f'Value of i is -->{i}')
    #Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print(f'Final Value of i is --> {i}')

#range(start,stop,step) -->here step --> interval..
for i in range(1,10,2):
    print(i)
    print("Done")
#it returns counter in reverse order
for i in range(10,0,-1):
    print(i)

#Print -10 to -1
for i in range(-10,0,1):
    print(i)

#[] --> we generally Lists
names = ['saketh','sairam','akash']
print(len(names)) #len(obj) --> returns the number of items in a container
for name in names:
    #print(name)
    #print(f'Student Name is {name}')
    if name == "sairam":
        print(f"Student name is {name}")

'''
#Calculate the sum of first 10 numbers 
#first understand your input --> range(11) -->10 numbers
#second understand your output --> sum (number)
#third we need to map the logic 
'''
result = 0 #target variable
for i in range(11):
    #print(i)
    #print(f'result is {i+i}')
    result = result + i #result += i
    #print(f'Now the result is {result}')
print(f'Sum of 10 numbers is {result}')

#Sum of first 10 even numbers

result = 0 #target variable
for i in range(21):
    if i %2 == 0:
        print(i)
        result = result + i #result += i
        print(result)
print(f'Sum of 10 even numbers is {result}')
'''
#Understand the loops usage with Fitness Streak example
#work_out -->1,work_out_missed --> 0

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
    else:
        current_streak = 0 #streak breaks
print(f'Longest Streak is {longest_streak}')


