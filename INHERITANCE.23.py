'''
oop-->class,object,methods(__init__)
encapsulation-->public,protected,private
'''
#1.Inheritence-->it is one of the key feature of OOP where we inherit the properties(attributes/methods) from one class to another class
#class(base class (parent class))-->derived class(child class)
#features-->code reusability,avoiding code duplication,code maintainability,polymorphism(method ovveriding(super()),method overloading,operator overloading)
#Types of inheritence(single,multiple,multilevel,heirarchy,hybrid)

'''
--->Single inheritence(finger print)-->one child class inheritence properties from one parent class
--->multiple inheritence(mother,father-->child)-->one child class inherit properties from two parent classes
--->multilevel inheritence(grandparent-->parent-->child)-->level by level
--->hierarchical inheritence(multiple child classes inheriting properties from single parent)-->one to many
--->hybrid inheritence(it can carry one or more type of inheritences)-->combination of above all four
'''

#--->Single inheritence
#syntax:
'''
class baseclass:
    statement(s).....
    ......
class derivedclass(baseclass):
    .........
    .................
'''
#--->example of whattsap scenario for single inheritence(personal user,business user)
'''
class user:
    """Single inheritence usage"""
    def send_message(self):
        print('Sending message')
    def voice_call(self):
        print('Making voice calls')
    def video_call(self):
        print('Making video calls')
class businessuser(user):
    def create_catalog(self):
        print('Displaying products catalog')
u1=businessuser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()
u1.create_catalog()
'''

#another example social media login-->users-->update_users
'''
class users: #parent class
    """single inheritence usage"""
    company='codegnan' #class attribute
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname+self.lname
#u1=users('nikhitha','koduri')
#print(u1.full_name())
#print(u1.company)
class update_users(users): #child class
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1=update_users('nikhitha',' koduri')
print(u1.company)
print(u1.full_name())
print(u1.update_name())

u2=users('sadaf','duray')
print(u2.full_name())
print(u2.company)
'''

#what if we have constructor in child class also
#father-->kid(property)
#in this example parent class is having constructor and child class is also having constructor, so constructor overriding is happening
#to avoid constructor overriding-->calling superclass with constructor, calling superclass with constructor along with arguments,and calling superclass with method(polymorphism)
'''
class father:
    """usage of constructor in single inheritence"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'father property is {self.property}')
#class kid(father):
    #pass
class kid(father):
    """now child class will have constructor"""
    def __init__(self):
        self.cash=200000
    def kid_property(self):
        print(f'kid property is {self.cash}')
obj=kid()
obj.father_property()
obj.kid_property()
'''
#in the above case it is giving same value for father also as 2lakhs and i again changed
#to avoid this use super class constructor
class father:
    """usage of constructor in single inheritence"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'father property is {self.property}')
#class kid(father):
    #pass
class kid(father):
    """now child class will have constructor"""
    def __init__(self):
        super().__init__() #it tries to access parent class
        self.cash=20000
    def kid_property(self):
        print(f'kid property is {self.cash}')
        print(f'kid final propery is {self.cash+self.property}')
obj=kid()
obj.father_property()
obj.kid_property()










