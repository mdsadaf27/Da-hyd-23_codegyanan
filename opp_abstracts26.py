'''
oop-->class(attributes,methods(constructor,instance method)),
object-->creation,utilization-->encapsulation,inheritance,polymorphism
oop-->abstraction,usage of class methods,static method
'''
#1.usage of class methods-->these are termed by using @classmethod decorator
#it applies for entire class level data,there by every object utilization will be modified
#--->example related to ecommerce
'''
class ecommerce:
    """usage of classmethod and class attribute"""
    company='flipkart' #class attribute
    delivery_charge=50
    @classmethod  #decorator
    def update_delivery(cls):
        cls.delivery_charge=100
        print(f'New delivery charges {cls.delivery_charge}')
product=ecommerce()
print(product.company) #calling class attribute with object 
print(product.delivery_charge)
print(ecommerce.company) #we can call class attributes with class name (possiblity in classmethod only)
print(ecommerce.delivery_charge)

product.update_delivery() #accessing the classmethod
print(product.delivery_charge)

#we can create many objects, and when we call with that object (changes automatically applied for all the new objects)
#so in the below mobile object the output will be 100 bcoz we had updaed the value 50 to 100
mobile=ecommerce() #another object
print(mobile.delivery_charge)

laptop=ecommerce()
print(laptop.delivery_charge)
'''

#--->apply inheritance and usage of class methods and class attributes
#-->banking scenario-->RBI-->SBI,HDFC...(with different class attribute names)
'''
class RBI: #parent class
    """inheritance usage of classmethod"""
    available_cash=5000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        print(f'Available cash rbi is {cls.available_cash}')
class SBI(RBI): #child class
    pass
class HDFC(RBI): #child class
    """now we will also add some cash to it"""
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        #print(f'Total cash is {cls.cash+cls.available_cash}')
        print(f'Total cash is {HDFC.cash+RBI.available_cash}') #we can call with the class names also instead of using cls(only applicable in inheritence)
a=SBI()
print(a.available_cash)
a.rbi_cash()
SBI.rbi_cash() #bcoz rbi is a parent so it acquire all properties from parent class and also we used classmethod 
#so that we can call (child class.parent class(method))
b=HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash() #calling object.parent class(method)
b.hdfc_cash() #calling object.child class(method)
'''

#-->banking scenario-->RBI-->SBI,HDFC...(with same class attribute names)
'''
class RBI: #parent class
    """inheritance usage of classmethod"""
    cash=5000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        #print(f'Available cash rbi is {cls.cash}')
        print(f'Available cash rbi is {RBI.cash}') #when attribute name is same to access this method, we should give (classname.classattribute)
        #so that when we call with object of rbi_cash 50lakhs will be accessed and returns the value
class SBI(RBI): #child class
    pass
class HDFC(RBI): #child class
    """now we will also add some cash to it"""
    cash=3000000
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total cash os {cls.cash+RBI.cash}')
a=HDFC()
print(a.cash) 
a.hdfc_cash() #it returns the hdfc cash as 30lakhs and also prints total cash
#a.rbi_cash() #it returns 30lakhs only classattribute is modified
a.rbi_cash() #after modifying 50lakhs will be returned
#if in case as above scenario we have same name for class attributes in both parent and child classes, 
#the best approach is call the class attributes is using class name, such as (RBI.cash)
'''
#2.Static method--->it doesnot depend either on the object or to the class
#we can create it using @staticmethod decorator
#it is mainly use utility or helper functions
'''
class ecommerce:
    """usage of static method"""
    @staticmethod  #it doesnt depend on anything(we can use directly and also call directly)
    def free_delivery(price):
        return price>500
u1=ecommerce()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))


#--->now lets relate both classmethod and staticmethod in a single use
class ecommerce:
    """usage of class and static method"""
    platform='flipkart' #classattribute
    @classmethod
    def show_platform(cls):
        print(f'Welcome to the platform {cls.platform}')
    @staticmethod
    def free_delivery(price):
        return price>500
u1=ecommerce()
u1.show_platform()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))
'''

#3.Abstraction-->it is also one of the key feature of OOP where it shows only the relevant details to the user 
#and hides the implementation features
#--->example-->instagram-->uploading photo,uploading video,reel
#we have abc(abstraction class) module to implement abstraction
#when we need all child classes to follow same pattern
import abc
from abc import ABC,abstractmethod  #ABC is parentclass by default , abc is a module
class content(ABC): #content is child class
    @abstractmethod #it possible when abstractmethod is available(it doesnt override)
    def upload(self):
        pass
class upload_photo(content):
    '''def upload(self):
        print('compressing the picture')
        print('edit the picture')
        print('photo uplaoded successfully...')'''
    pass #as we made upload as abstract method mandatory it has be followed
class upload_video(content):
    def upload(self):
        print('encoding the video')
        print('video editing is in process')
        print('video uploaded successfully...')
    pass
class Reel(content):
    def upload(self):
        print('adding effects to the reel')
        print('reel is edited')
        print('reel is uploaded successfully with tags...')
    pass
'''Contents=[upload_photo(),upload_video(),Reel()]  #throwing all classes to the object
#print(Contents)
for content in Contents:
    content.upload()''' #all classes will be retured

#obj=upload_photo()
#print(obj) #it raises typeerror we are not following the upload pattern
a=upload_video()
a.upload() #only upload_video will be displayed
 