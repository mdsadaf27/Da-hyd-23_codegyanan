'''
An oop is a mechanism or a process which revolves around creating objects it consists of two important properties
1.Attributes-->varibles which carry the data to the class
2.Methods-->a method is a function defined inside a class which carry the behavior of the object

class-> a class is a blueprint(template) for an object ,an object is an instance(physical thing) which utilizes the class
example-->chair(object)-->wood,tools,dimensions,(blueprint),carpenter

the main features of OOP-->modularity,scalability,
encapsulation-->(binding the data(attributes), features to the class, objects will be used)
abstraction-->try to show relevant information to the class(object)
inheritence-->acquiring properties(attributes,methods)
a)single inheritence-->Fingerprint
b)multi inheritence-->parents(mother,father)-->child
c)milti-level inheritence-->grandparent-->parent-->child
polymorphism-->method overloading,method overriding,operator overriding

'''
#1.Syntax for class creation:
'''
class Class_Name:
    """Doc string"""
    attributes(characterstics)
    .........
    def func(self): -->it will give the behavior of the class
        ...........
        ...............
    .........
object=Class_Name()
'''
#--->simple example of a student class with basic details
#in this example we are passing only one student 
'''
class Student:
    """Understanding the usage of OOP"""
    name='nikki'
    id='CGH3882'
    gender='female'
    email_id='nikhithakoduri694@gmail.com'
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method 
        print(f'Student Name is: {self.name}')
        print(f'Student ID is: {self.id}')
        print(f'Student Gender is: {self.gender}')
        print(f'Student Mail_id is: {self.email_id}')
u1=Student()
u2=Student()
print(u1)
print(u2)
#print(dir(u1)) #dir-->directory-->which returns all available methods/attributes inside a class
u1.display()
u2.display()
'''
#--->student class for multiple objects
#in this we are asking user to give the input, and we can give only once
'''
class Students:
    """Understanding the usage of OOP"""
    name=input('Enter name:')
    id=input('Enter ID:')
    gender=input('Enter the Gender:')
    email_id=input('Enter the Mail_ID:')
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method 
        print(f'Student Name is: {self.name}')
        print(f'Student ID is: {self.id}')
        print(f'Student Gender is: {self.gender}')
        print(f'Student Mail_id is: {self.email_id}')
u1=Students()
u1.display()

u2=Students()
u2.display()
print(u1.__dict__) #it returns empty dictionary
print(u2.__dict__) #it returns empty dictionary
'''

#--->Student details with multiple objects
#in this we are passing the 2 or more details in the objects and we can store into the dictionary
'''
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name=name
        self.id=id
        self.gender=gender
        self.email_id=email_id
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method 
        print(f'Student Name is: {self.name}')
        print(f'Student ID is: {self.id}')
        print(f'Student Gender is: {self.gender}')
        print(f'Student Mail_id is: {self.email_id}')
u1=Students()
u1.data('nikki','CGH3882','female','nikki@gmail.com')
u1.display()

u2=Students()
u2.data('sadaf','CGH2003','female','sadaf@gmail.com')
u2.display()
print(u1.__dict__)
print(u2.__dict__)
'''
#Task-->create class with car brand name price color-->display()
class Car:
    """Understanding the usage of OOP"""
    def data(self,name,brand,price,color):
        self.name=name
        self.brand=brand
        self.price=price
        self.color=color
    #Methods(behavior of the attributes)
    def display(self): #self is a middle person for class and method 
        print(f'Car Name is: {self.name}')
        print(f'Car Brand is: {self.brand}')
        print(f'Price is: {self.price}')
        print(f'Color is: {self.color}')
u1=Car()
u1.data('BMW','sedans',24000,'Red')
u1.display()

u2=Car()
u2.data('Mustang','Ford',36000,'Red')
u2.display()
print(u1.__dict__)
print(u2.__dict__)