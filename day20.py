'''
Introduction to oops
classes
Attributes
Methods

oops
----
--> object-oriented language(oop) is a style of programming where we model real-world things as the objects contain
both data and functions()
--> reusability of code
--> and also scalable

Class
-----
--> class is a blue-print or template that defines what kind of data on behaviour a certain type of object will have

object
------
--> This is nothing but instance of class or An object is a real instance created from a class.
It is the actual thing that exists in the memory while the program runs.

class car:
    pass
car1 = car()#object
car2 = car()

Attributes
----------
--> these are the variables that store data related to class or object


class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
car_1 = car("wagnor", "brown")
car_2 = car("Tiago", "white")
print(car_1.brand)


for animals:-

class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
animal_1 = Animal("lion", "brown", "medium")
animal_2 = Animal("cat", "white", "small")
print(animal_1.name)

for food items:-

class Food_items:
    def __init__(self, name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
items_1 = Food_items("rice","high","100")
items_2 = Food_items("dal","medium","50")
items_3 = Food_items("curry","small","80")
print(items_2.price)

for vegetables:-

class vegetables:
    def __init__(self, name,quantity):
        self.name = name
        self.quantity = quantity
Veg_1 = vegetables("potato","1kg")
Veg_2 = vegetables("carrot","2kg")
print(Veg_2.name)'''



class car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 20

    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total: {self.mileage}"

    def info(self):
        return f"{self.make} {self.model} {self.year}"

car_1 = car(make="Ford", model="Mustang", year="2008")
car_2 = car(make="Toyota", model="Camry", year="2023")

print(car_1.info())
print(car_2.info())
print(car_2.drive(10))
        
            
    



        




