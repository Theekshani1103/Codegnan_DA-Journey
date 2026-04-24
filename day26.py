'''
Error Handling
--------------
try block
---------
--> try block will test a block of code for errors
eg
---
try:
  print(b)

Except block
------------
--> this block will take care of any errors

try:
  print(b)
except:
  print("This block can handle error")

else block
----------
--> else keyword to define a block of code to be executed if no error were raised
try:
  a = 9
  b = 10
  print(a+c)
  
except:
  print("error here")
else:
    print("No error in the code")


try:
  a = 9
  b = 10
  print(a-b)

except:
  print("error here")
else:
    print("No error in the code")


finally block
-------------
--> This block will execute either try block contain errors or no errors


#with error
try:
  a = 9
  b = 10
  print(a+c)

except:
  print("error here")
else:
    print("No error in the code")
finally:
    print("the try-except block is finished")

#without error
try:
  a = 9
  b = 10
  print(a+b)

except:
  print("error here")
else:
    print("No error in the code")
finally:
    print("the try-except block is finished")

try:
    num1 = 10   
    num2 = 2    
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result")
finally:
    print("Everything is ok")


try:
    num1 = 4
    num2 = 5
    result = num1 / num2
    print(result + x)   
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except NameError:
    print("Variable not defined")
else:
    print("Result is:", result)'''
    










