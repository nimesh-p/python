#public access modifier
class one():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('age is',self.age)    
m1=one('nimesh',25)
print("Name:",m1.name)
m1.display()



#protected
class person():
    # protected data members 
    _name=None
    _age=None
    _std=None
    def __init__(self, name, age, std):   
        self._name = name 
        self._age = age 
        self._std = std

     #protected memeber function   
    def _display(self):
        print("Name:",self._name)
        print("Age:",self._age)
        print("Std:",self._std)
#inheriting from person class
class child(person):
    def __init__(self,name,age,std):
        person.__init__(self, name,age,std)    
    #public memeber function
    def display_data(self):
        # print("Name:",self._name)     
        self._display()     

p2=child("nimesh",25,"SPU")
p2.display_data()



#private 
class parents():
    __name=None
    __lastname=None
    __roll=None
    def __init__(self,name,lastname,roll):
        self.__name=name
        self.__lastname=lastname
        self.__roll=roll
    def __Display(self):
        print("Name:",self.__name)
        print("Lastname:",self.__lastname)
        print("Roll:",self.__roll)
    #creating public method to acces display method variable
    def accesprivatefunction(self):
        self.__Display()    

# pp1=parents("nimesh","prajapati",18)
# pp1.accesprivatefunction()        
class childeren(parents):
    pass

pp1=childeren("nimesh","prajapati",25)
pp1.accesprivatefunction()


