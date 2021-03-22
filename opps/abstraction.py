

#In Abstrction we cannot create instance of it.
 #we cannot create an object of child class beacuse in parent class we have created two abstractmethod and 
# #we have call only one method inside child class so if we want to create object of child class we should call all the abstract method inside child class


from abc import ABC, abstractmethod 
  
class R(ABC): 
    @abstractmethod
    def rk(self): 
        print("Abstract Base Class") 
  
class K(R): 
    def rk(self): 
        super().rk() 
        print("subclass ") 

a=K()
a.rk()



  
class Polygon(ABC): 
  
    # abstract method
    @abstractmethod 
    def noofsides(self): 
        print("jeee")
  
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 
  
p=Polygon()
p.noofsides()


class sum(ABC):
    @abstractmethod
    def tot(self,m1,m2,m3):
          pass

class sub(sum):
     def tot(self,m1,m2,m3):
        total=m1-m2+m3
        print("The sub is",total)
    


ni=sub()
ni.tot(10,10,5)



class parents(ABC):

    @abstractmethod
    def data1(self):
        pass
    @abstractmethod
    def data2(self):
        pass

class child(parents):
    def data1(self): 
nim=child()
nim.data1()



#abstraction using multilevel inheritance



class school(ABC):
    @abstractmethod
    def pattern(self):
        pass
    @abstractmethod

    def fibanoci(self):
        pass
class teacher(school):
    def pattern(self,num):
            for i in range(0, num):
                for j in range(0, i + 1):
                    print("* ", end="")
                print("")
            for i in range(num, 0 , -1):
                for j in range(0, i + 1):
                    print("* ", end="")
                print("")


class Student(teacher):
    def fibanoci(self,num):
        a = 0
        b = 1
        sum = 0
        count = 1
        print("Fibonacci Series: ", end = " ")
        while(count <= num):
            print(sum, end = " ")
            count += 1
            a = b
            b = sum
            sum = a + b
        
  



s1=Student()
s1.pattern(5)
s1.fibanoci(5)

#abstraction using construction

class name(ABC):
    def __init__(self,name,lastname):
        self.lastname=lastname
        self.name=name
        
    @abstractmethod
    def print_name(self):
        pass
    @abstractmethod
    def print_lastname(self):
        pass
    
    
class lastname(name):
    def print_name(self):
        print("Hello",self.name,"Here")
        
    def print_lastname(self):
        print("sirname is",self.lastname)
    
tk1=lastname("nimesh","prajapati")
tk1.print_name()
tk1.print_lastname()
        
        
