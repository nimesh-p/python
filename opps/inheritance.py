#inheritance
class first():
    def prime_number(self,num):
        if num > 1:
	        for i in range(2,num):
		        if (num%i)==0:
			        print(num,"is not prime")
			        break
	        else:
		        print("is prime number")
        else:       
	        print("not prime number")			


    def lastname(self):
        print("hello prajapati")
class second(first):
    def mes_stud():
        print("second classs")
a=second()
a.prime_number(9)





class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the Botree", self.graduationyear)

x = Student("nimesh", "prajapati", 2021)
x.welcome()



#multilevel inheritance

class A():
    def __init__(self,age):
        self.sage=age
    def print_age(self):
        print(self.sage)    
class B(A):
    def __init__(self,name):
        self.sname=name
    def print_name(self):
        print(self.sname)
class C(B):
    def print_mess(self):
        print("hello this is c class")

ob=B("nimesh")
ob.print_name()


#overiding
class Robot:
    
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print("Hi, I am " + self.name)
        
class PhysicianRobot(Robot):

    def say_hi(self):
        print("Everything will be okay! ") 
        print(self.name + " takes care of you!")

y = PhysicianRobot("James")
y.say_hi()