'''
-----> polymorphism <--------
its a key feauture of OOP
poly--> many
moph--> forms
method with same name can take diffrent parameters (arguments-->list...str..)
this haves types 
1---> method overloading (compile thime polymorphism)
2---> method overloading (run-time)
3---> operotor overloading (+,*) (__add__,__str__)magic method

Hotstar 
---> free user --> can watch the movies with advertisments
--->premium user ---> can watch premium content without advertisment
--->vip user---->live content, streaming quality, premium content 

#method over loading : 
   

class Hotstar:
    """understand polymorphsm"""
    def watch ():
        print(f'user logged into Hotstar ...OPening home page' )
    def watch(self,movie):
        self.movie = movie 
        print(f'User watching {self.movie}')
app = Hotstar()
app.watch("Leo")
#app.watch() it return error as watch() is overload

#1.  usage wmethodith dfault arrguments
#2. method usage with variable length arguments (*agrs)
#3. method usage with type of arguments


#2. method usage with variable length arguments (*agrs)


class Hotstar:
    """ usage wmethodith dfault arrguments """
    def watch (self ,movie=None):
        if movie is None:
            print(f'User logged into Hoststar....checking ...')
        else:
             self .movie =movie 
             print(f'User started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch("vikram")

class Hotstar:

    def watch(self, *args):
        if len(args) == 0:
            print("User logged into Hotstar....checking...")
        else:
            for movie in args:
                print(f"User started watching {movie}")


app = Hotstar()
app.watch()
app.watch("Vikram")
app.watch("Vikram", "Leo", "Jailer")



#3. method usage with type of arguments 


class HotStar:
       """ method Overloading with type of arguments usage """
       def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}')
        elif isinstance(content,list):
            print(' backgrouplaying playlist:')
            for movie in content:
                print(movie)
app=HotStar()
app.watch('leo')
app.watch(["Vikram", "hello", "Jailer"])



class Freeuser:
    """understanding method overriding"""
    def watch(self):
        print('user logged into homepage...')
class premium_user(Freeuser):
    """using inheritence"""
    def watch(self,movie):
        self.movie=movie
        print(f'user is watching {self.movie}')
#obj behavior is changing
obj=Freeuser()
obj.watch()
obj2=premium_user()
obj2.watch('leo')

'''

class Freeuser:
    def watch(self):
        print("user logged into homepage...")
class PremiumUser(Freeuser):
    def watch(self, movie):
        super().watch()
        print(f"user is watching {movie}")

obj = PremiumUser()
obj.watch("namastey india")