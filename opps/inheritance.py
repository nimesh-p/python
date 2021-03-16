# inheritance
class first:
    def prime_number(self, num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not prime")
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


a = second()
a.prime_number(9)


class Person:
    names = "nimu"

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
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the Botree",
            self.graduationyear,
        )


x = Student("nimesh", "prajapati", 2021)
x.welcome()
p1 = Person("nimesh", "praja")
p1.printname()
p1.names


# multilevel inheritance


class A:
    def __init__(self, age):
        self.sage = age

    def print_age(self):
        print(self.sage)


class B(A):
    def __init__(self, name, age):
        # self.sage=age
        self.sname = name
        A.__init__(self, age)

    def print_name(self):
        print(self.sname)


class C(B):
    def print_mess(self):
        print("hello this is c class")


t1 = C("shailesh", 25)
t1.print_name()
t1.print_mess()
t1.print_age()

# multilevel
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)


# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather name :", self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son("Prince", "Rampal", "Lal mani")
print(s1.grandfathername)
s1.print_name()


# multiple inheritance
class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)


class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)


obj = Class4()
obj.m()

# overiding
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


class sum:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def add(self):
        m3 = self.m1 + self.m2
        print("the sum is ", m3)


class sub(sum):
    def __init__(self, m1, m2):
        # self.p1=p1
        # self.p2=p2
        sum.__init__(self, m1, m2)

    def subt(self):
        m3 = self.m1 - self.m2
        print("the diffrenece is", m3)


class mul(sub):
    def __init__(self, m1, m2):
        sub.__init__(self, m1, m2)

    def mult(self):
        m3 = self.m1 * self.m2
        print("multiplication", m3)


pk = mul(5, 2)
pk.add()
pk.subt()
pk.mult()


class circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_ans(self):
        return self.radius * self.pi * 2


my_circle = circle()
print(my_circle.pi)
print(my_circle.get_ans())
