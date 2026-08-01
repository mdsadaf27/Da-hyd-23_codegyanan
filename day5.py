#task:student marks and grade analyzer
#90-100--->'A'
#80-89-->'B'
#70-79--'C'
#60=69-->'D'
#50-59-->'E'
#also -ve case should not be alwed and marks should be grater then 100
"""
marks = int(input('Enter the marks:'))

if marks > 0 and marks <= 100:
    if marks >= 90 and marks <= 100:
        print("Grade A")
    if marks >= 80 and marks <= 89:
        print("Grade B")
    if marks >= 70 and marks <= 79:
        print("Grade C")
    if marks >= 60 and marks <= 69:
        print("Grade D")
    if marks < 60:
        print("Fail")
else:
    print("Enter only +ve values greater than 0")
 """

#elif keyword --> if elif - else

""""
if condition
    (statement )
    ......
elif <conditional>
    (statement )
    .....
    ...
else
   statement(s)...
   """
"""
marks=int(input("enter the student grade marks:"))
if marks >=100:
    print("enter the values  should be grater then 1 and less then 100")
elif marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
elif marks < 60 and marks >=0:
    print("user failed study again")
    """
"""
age = int(input("enter the age:"))
if age>=18 and age <=100:
    print("user has elgubility")
    print("access granted")
elif age<18 and age>0:
    print
    ("------user still need to get vote eligiblity--------")
    print("----- user need to wait for more ",(18-age),"years(s)----")
else:
    print("----------only +ve value and less than 100 acceptable-----")
""""    
    
# prefer if if-else ...
# output--> print()
#output formalating --->

"""'
arks = int(input("Enter the Student marks:"))
if marks >=100:
    print("Entered values should be greater than 1 and less than 100")
elif marks >= 90 and marks <=100:
    print("User has secured Grade A")
elif marks >= 80 and marks <= 89:
    print("User has secured Grade B")
elif marks >= 70 and marks <= 79:
    print("User has secured Grade C")
elif marks >= 60 and marks <= 69:
    print("User has secured Grade D")
elif marks < 60 and marks >=0:
    print("User has failed,study again")
else:
    print("No negative values")

#Task --> Same usecase try with if-elif-else usage in other way

#Voter Eligibility checkcase -->make sure to satisfy all possible conditions
#>=18 and 100 -->Access
#<18 --> no of years eligibility should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('------ User has Vote Eligibility -----')
    print('------ Access Granted -------')
elif age<18 and age >0:
    print('------ User still need to get Vote Eligibility -----')
    print('------User need to wait for more',(18-age),'year(s)-------')
else:
    print('-----Only +ve values and less than 100 Acceptable----')

#Prefer if-elif-else....
'''
#output --> print() -->we can pass any values also use sep and end
#Output Formatting -->old style formatting (using commas)
#% usage (%f,%d),.format() usage,fstring notation
'''a,b = 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "DataAnalysis"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='------->')
#end='\n' ,\t -->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderabad")'''

name='Codegnan';age=7;batch='DA-023';place='Hyderabad'
'''#Usage of commas
print(batch,'is in',name) #variables and msg to be separated by comma
print(name,'is in',place,'age is',age,'years')
#Old style formatting --> %d -->integer,%s-->string,%f-->float
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f --> rounding to 1 decimal
'''
#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)

print(f'{name} is in {place}')
print(f'{"Saketh"} is in {name}')

"""
































