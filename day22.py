'''
Encapsulation
-------------
--> The principle of bunding data (Attributes) and methods that operates on that data into single unit, which is a class


class BankAc:
    def __init__ (self, balance):
        self.__balance

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

Acc = BankAc(15000)
Acc.deposite(7000)
print(acc.get_balance())

Inheritance
-----------
--> This allows a child class(sub class) to acquire the attributes and method of the parent class (base class)
this is called inheritance
1.Single Inheritance
--> Accessing only one method from the base class(parent) is called as single inheritance
ex code:
class parent:
    def display(self):
        print("This is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
obj = child()
obj.display()
        
2.Multiple Inheritance
----------------------
--> A child class inherits from more than one parent class..

ex code:
class Father:
    def skill_1(self):
        print("Father: hard working")

class Mother:
    def skill_2(self):
        print("Mother: Cooking")

class child(Father, Mother):
    def All_skills(self):
        print("child: Coding")
obj = child()
obj.skill_1()
obj.skill_2()
obj.All_skills()



super()
-------
--> This is used to call methods of the parent class from the child class'''


class person:
    def name(self):
        print("name: Theeku")

class address:
    def addr(self):
        print("address: odisha")

class contact:
    def mobile(self):
        print("mobile: 2929292929")

class adhar(person,address,contact):
    def adhar_no(self):
        print("adhar number: 1274 4673 0000")

my = adhar()
my.name()
my.addr()
my.mobile()
my.adhar_no()


        






        


        





