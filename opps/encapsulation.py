#using protected variable
class Base:
    def __init__(self):
         
        # Protected member
        self._a = 2
 
# Creating a derived class    
class Derived(Base):
    def __init__(self):
         
        # Calling constructor of
        # Base class
        Base.__init__(self) 
        print("Calling protected member of base class: ")
        print(self._a)
 
obj1 = Derived()        
obj2 = Base()



#using private 
class parent():
    def __init__(self):
        self.a="hello"
        self.__name="nimesh"

class child(parent):
    def __init__(Self):
        parent.__init__(Self)
        print("welcome",Self.a)
        # print("name is",Self.__name)
        
        
ob=child()
ob1=parent()
# print(parent__name) #we cannot call private variable outside the class
print(ob._parent__name) #calling private variable using mangling function



#Getter and Setter method
class SampleClass:

    def __init__(self, fname):
        ## private varibale or property in Python
        self.__fname = fname

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__fname

    ## setter method to change the value 'a' using an object
    def set_a(self, fname):
        self.__fname = fname
gt=SampleClass("nimehs hello")
print(gt.get_a())
gt.set_a("nimesh bye")
print(gt.get_a())





class SampleClass1:

    def __init__(self, a):
        ## calling the set_a() method to set the value 'a' by checking certain conditions
        self.set_a(a)

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

    ## setter method to change the value 'a' using an object
    def set_a(self, a):

        ## condition to check whether 'a' is suitable or not
        if a > 0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2

nim=SampleClass1(8)
print(nim.get_a())