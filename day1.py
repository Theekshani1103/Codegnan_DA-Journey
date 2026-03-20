'''
Operators -->  An operator is a symbol that performs an operation on one or more values (operands)  and produces a result

operators are primarily used :
--> calculate values
compare values/inputs
make decisions
contol the program flow


there are major seven categories of operators python
arthematic operators
assignment operators
comparison operators
memebership operators
identity operators
bitwise operators
Logical operators
'''
'''
#Arthematic operators--> Arithematic operators perform mathematical operators
# + Addition , - substraction , * Multiplication , /Divison ,** Exponent , % Modulus , // Integer division
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''

'''
#Assignment operators
#--> = Assign , += Addition Assignment, -= Subtract Assignment , *=,/= , %= , // , **=
#they are majorly uesd for  code repetitions in applications usage
a = 4
b = 3
a += 2 #-->  a = a+2
print(a)
b += a
print (b)
a -= 3
print (a)
b -= 3 #b = b-3
print (b)
print (f'The updated values of a and b are {a} and {b}')
b*= a #b= b*a
print (b)
b/= a
print (b)
'''


'''
#Relational operators or comparison operstors  -->  they always return the boolean values (True/false)
# == is equal to,!= not equals to < less than , > greater than , >= ,<=

a = int (input("Enter a value:"))
b = int (input("Enter a  another value:"))
print (a==b)
print (a!=b)
print (a<b)
print (a>b)
print (a<=b)
print (a>=b)
'''
'''
#Membership operators --> they check for the existance of an object in a #collection --> in , not in

a = "codegnan"
print(type(a))
print('a' in 'a' )
print('z' in 'saketh')
print('z' not in 'codegnan')

b = [12,6,3,4]
c = int(input("Enter the value"))
print(c)
print(c in b)
print(c not in b)
'''
'''
#Logical operators --> they are used to combine multiple conditions # and ,or, not

age = int(input("Enter the age : "))
vote_right = True

print(age >= 18 and vote_right)
print(age != 18 or vote_right)
print(not vote_right)
'''
'''
#Identity operators --> they check the/ compare the memory location and validate we  use
#(id) function it is differnt from == operator ->is,is not

a=[1,2,4]
b=[1,2,4]
print(a==b)
print(id (a))#returns the identity of object
print(id (b))
print(a is b)
print(a is not b)

c=b
print(c)
print(id(c))
print(c is b)
'''

#Bitwise operators --> Bitwise operators AND & ,Bitwise OR | perform bitwise operations
#we get the result (remember binary number)
print(5&3)
print(bin(5))#returns binary number

#task --> now  you have all the operators create a checker task




