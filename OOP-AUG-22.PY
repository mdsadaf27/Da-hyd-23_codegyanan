'''
constructor-->instance methods-->public attributes-->encapsulation
'''
#1.Constructor-->it is a special method(__init__()) init means initialization
#which will automatically initialize the attributes and the method to the object in the class
'''
class Car:
    """Understanding the usage of Constructor"""
    def __init__(self,name,brand,price,color):
        self.name=name #public attributes
        self.brand=brand
        self.price=price
        self.color=color
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method 
        print(f'Car Name is: {self.name}')
        print(f'Car Brand is: {self.brand}')
        print(f'Price is: {self.price}')
        print(f'Color is: {self.color}')
u1=Car('tata','nexon',900000,'blue') #by using init constructor, we can directly pass values in the object and no need to create another method
u1.display()
'''

#-->same example with Non-parameterized
#in this example we didnt passed any parameters inside the method
#and we can directly use print() and pass values at last or we can call display method 
#in this only one car detail can be used
'''
class Car:
    """Understanding the usage of Constructor"""
    def __init__(self):
        self.name='BMW'
        self.brand='Sedans'
        self.price='50Lakhs'
        self.color='Red'
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method and it is a instance method
        print(f'Car Name is: {self.name}')
        print(f'Car Brand is: {self.brand}')
        print(f'Price is: {self.price}')
        print(f'Color is: {self.color}')
u1=Car()
#print(u1.name,u1.brand,u1.price,u1.color)
u1.display()
'''

#writing attributes inside the constructor called as public attributes
#writing method after the constructor called instance method

#2.Encapsulation-->it is one of the main feature of OOP
#it binds(bundles) the data(attributes) and the methods(behavior) into a single unit(class)-->multiple objects
#attributes can be termed into three ways-->public,private,protected

#--->public attribute-->attributes defined inside the class(constructor) and can be modified outside the class
'''
class CodegnanPortal: #creating
    """codegnan portal with users by using public attribute"""
    def __init__(self,username):
        self.user=username #username is a public attribute
        #to access student details
    def display(self): #accessing
        print(f'Student Username is :{self.user}')
u1=CodegnanPortal('nikki')
u1.display()
u1.user='nikhitha' #we can modify (updating)
print(f'Updated username is: {u1.user}')
u1.display()
print(u1.__dict__)
u2=CodegnanPortal('sadaf')
u2.display()
print(u2.__dict__)
'''

#--->protected attributes-->we use single underscore before 
#attribute moreover it can be modifies also outside the class 
#and even accessible in subclasses...
'''
class CodegnanPortal: 
    """codegnan portal with users by using protected attribute"""
    def __init__(self,username,_otp):
        self.user=username 
        self._otp=_otp #protected attribute
    def display(self):
        print(f'Student username is : {self.user}')
        print(f'Student has received OTP as : {self._otp}')
u1=CodegnanPortal('nikki',1234)
u1.display()
u1._otp=2345
print(f'Modified OTP: {u1._otp}')
u1.display()
'''

#--->private attribute-->we use special notation as double underscore such as __password
#we can access only inside the class and cannot be directly modify
'''
class CodegnanPortal: 
    """codegnan portal with users by using private attribute"""
    def __init__(self,username,_otp,__password):
        self.user=username 
        self._otp=_otp #protected attribute
        self.__password=__password #private attribute
    def display(self):
        print(f'Student username is : {self.user}')
        print(f'Student has received OTP as : {self._otp}')
u1=CodegnanPortal('nikki',1234,'admin123')
u1.display()
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling
#we cannot call password directly 
#we use getter,setter method or NameMangling method
'''

#--->in above case we are using name mangling but the right way is usage of getter and setter methods
class CodegnanPortal: 
    """codegnan portal with users by using getter and setter method"""
    def __init__(self,username,_otp,__password):
        self.user=username 
        self._otp=_otp #protected attribute
        self.__password=__password #private attribute
        #usage of getter() method
    def get_password(self):
        #return '*****'
        return self.__password
    #to modify the password we use setter() method
    def set_password(self,new_password):
        if len(new_password)>6:
            print('Now password is updated')
            self.__password=new_password
        else:
            print('Wrong password')
u1=CodegnanPortal('nikki',1234,'admin123')
print(u1.get_password())
u1.set_password('nikki123') #compulsory morethan 6
print(u1.get_password())