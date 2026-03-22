'''
variables -->  variables are named storage locations
that is usedtto hold the data in the memory,
to make it simple it is the label which points
out the value --> also called as storage placeholders

rules for defining variables 
--> A-Z,a-z,0-9
-->start with uppercase,lowercase,even with underscore_
--> but you cannot start with symbols(@,#,$...)


Better preferable way is to go with general purpose
--> such as you want to store your details name,email_id,account_number..
'''
'''
a = 1
b = 5
a = 25
#python is dynamically typed,you need not define the datatype and also
#only the recent value to  variable with same name is pointed

print(a)
print(b)

#1a23 = 25 #syntac error

#@werf = 4.5 #syntaxerror

#$dsf = 12 #Invalid syntax

#store your personal details

name = "Theeku"
location = "Vizag"
Age = 7
email_id = "cmp@codegnan.com"
emailid = "cmp@codegnan.com"
print(name,location,Age,email_id)

#How to assign multiple values to a variable
aksh,praneeth,ajay=21,20,23
print(aksh)
print(praneeth)
print(ajay)

#assign same values to multiple variables
x = y = z = 21
print(x,y,z)


#Keywords
#they are reserved words which will have specific usage
#there are 35 keywords in python
#never use keywords as identifiers

#if = 23
#lambda = 'saketh'
#False = 0 #cannot assign

#python is case-sensitive
false = 25


#Identifiers are names given to variables ,functions,classes,objects...

#Literals are fixed values to a Identifier
age = 25
name = 'Theeku'
#name is Identifier,25 is literal

#in python we have single line comments -->#
#multiple line comments -->#start end with triple quotes

'''

'''
#Built-in Datatypes --> Numeric,boolean,Collections

#Numeric datatypes --> int,float,complex
#int --> count,values,quantities
#float --> temperature,percentage,price
#complex --> specific conversions (complex is combination of real and imaginary)
#implicit as python follows dynamic type

count = 40
print(count)
print(type(count))

price = 175.25
print(price)
print(type(price))

j3 = 25
value = 2+j3
print(value)
print(type(value))


value = 2+3j
print(value)
print(type(value))
'''

'''
#Typecasting --> converting one type to another

#int --> float,complex

age = 25
print(type(age))

b = float(age)
print(b)
print(type(b))

c = complex(age)
print(c)
print(type(c))
'''
'''
#float,complex
percent = 70.34
print(type(percent))

d = int(percent)
print(d)
print(type(d))
e = complex(percent)
print(e)
print(type(e))
f = 2+5j
print(type(f))
#g = int(f) #complex to int is not possible
#print(g)
h = float(f) #complex to float is not possible
print(h)

'''
'''
#boolean datatype --> validation --> True/False
a = True
print(a)
print(type(a))

#Typeconversion of bool

b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))     
'''
'''
#Input --> input()/ output --> print()
a = 5
print(a)

a = input("Enter a Value") #any input but result as str
print(a)
print(type(a))

a = int(input("Enter a Value:")) #only integer input
print(a)
print(type(a))

b = float(input("Enter another value"))
print(b)
print(type(b))
'''


#now let's work on a simple case study  using above --> Fee calculator

#details of Student
name = input("Enter the student name:")
admission_fees = int(input("Enter the Admission fees:"))
Tuition_fees = float(input("Enter the tution fees:"))
Hostel_fees = float(input("Enter the Hostel fees:"))
#calculate the Total fees
total_fees = admission_fees + Tuition_fees + Hostel_fees
print("total fees is = ", total_fees)
print("<---------------------->")
print("student name:",name)
print("Admission fees is = ",admission_fees)
print("Tuition fees is = ",Tuition_fees)
print("Hostel fees is = ",Hostel_fees)
print("Total fees is = ",total_fees)
print("-----------------------")

