
# #method overloading
# class fruits():
#     def __init__(self,name):
#         self.name=name
#     def print_mess(self):
#         print("hello welcome",self.name)
    
# class flowers(fruits):
#     def __init__(self,color,types):
#         self.color=color
#         self.types=types
#     def print_mess(self):
#         print("hi",self.color)
#         print("nimesh",self.types)

# # obj=flowers("nimesh")
# # obj.print_mess()
# obj1=flowers("red","mast")
# obj1.print_mess()

       
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.l = length
#         self.b = breadth
#     def area(self):
#         return self.l * self.b
# class Square:
#     def __init__(self, side):
#         self.s = side
#     def area(self):
#         return self.s ** 2
# rec = Rectangle(10, 20)
# squ = Square(10)
# print("Area of rectangle is: ", rec.area())
# print("Area of square is: ", squ.area())
  

# # #duck typing
# class parents():
#     def viewdata(self):
#         print("this is parents class")
#         print("welcome to parents class")

# class subchild():
#     def viewdata(self):
#         print("hello")
#         print("welcome")
#         print("good morning")

# class hello():
#     def Data(self):
#         print("nimesh")

# class child():
#     def code(self,id):
#         id.viewdata()

# id=subchild()

# obj=child()
# obj.code(id)

# #overrridding
# class fruits:
#     def print_mess(self):
#         print("hello")
        
    
# class flowers(fruits):
#     def print_mess(self):
#         pass
#         # print("hello welcome")
    
# p1=flowers()
# print(p1.print_mess())


# #multiple inheritance using overriding
# class Parent1(): 
          
#     # Parent's show method 
#     def show(self): 
#         print("Inside Parent1") 
          
# # Defining Parent class 2 
# class Parent2(): 
          
#     # Parent's show method 
#     def display(self): 
#         print("Inside Parent2") 
          
          
# # Defining child class 
# class Child(Parent1, Parent2):  
#     def show(self): 
#         Parent1.show(self)
#         # print("Inside Child") 
     
        
# # Driver's code 
# obj = Child() 
# obj.show()


# #multilevel inheritance

# class Parent():  
        
#     # Parent's show method 
#     def display(self): 
#         print("Inside Parent") 
    
    
# # Inherited or Sub class (Note Parent in bracket)  
# class Child(Parent):  
        
#     # Child's show method 
#     def show(self): 
#         print("Inside Child") 
    
# # Inherited or Sub class (Note Child in bracket)  
# class GrandChild(Child):  
          
#     # Child's show method 
#     def show(self):
#         Child.show(self)
#         pass 
#         # print("Inside GrandChild")          
    
# # Driver code  
# g = GrandChild()    
# g.show() 
# g.display() 


# # #multiple inheritance

# class one:
#     def data(self):
#         pass
#         # print("from first classs")
# class two:
#     def data(self):
#         print("from second class")
# class three(one,two):
#     def display(self):
#         two.data
#         print("third classs")

# m1=three()
# m1.data()



# #method overriding example with multilevel inheritance

# class odd_even():
#     def __init__(self,num):
#         self.num=num
#     def check_num(self):
#         if self.num == 0:
#             print("must be greater than zero")
#         elif self.num%2==0:
#             print(self.num," Is Even number")
#         else:
#             print(self.num," Is odd number")


# class pos_neg(odd_even):
#     def __init__(self,num):
#         self.num=num
#         odd_even.check_num(self)
#     def check_num(self):
#         if self.num > 0:
#             print(self.num,"Is Positive Number")
#         elif self.num==0:
#             print("Number is zero")
#         else:
#             print(self.num,"Is Negative Number")
    
# class is_prime(pos_neg):
#     def __init__(self,num):
#         self.num=num
#         odd_even.check_num(self)
#     def check_num(self):
#         if (self.num == 1):
#             print("1 is neither prime nor composite")
#         elif (self.num <= 0):
#             print("Enter valid number")
#         else:
#             for number in range(2, self.num):
#                 if(self.num % number == 0):
#                     print(self.num," Is not Prime Number")
#                     break
#             else:
#                 print(self.num,"Is Prime Number")

            

# obj=odd_even(4)
# obj.check_num()
# obj1=pos_neg(1)
# obj1.check_num()
# obj=is_prime(1)
# obj.check_num()



a.rk()