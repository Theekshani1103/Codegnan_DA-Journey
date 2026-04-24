'''
String methods
casefold():-
---------
text = "PYTHON"
print(text.casefold())

strip():-
-------

text = " hello python   "
print(text.strip())

isalnum():-
---------
text = "Python123"
print(text.isalnum())

isupper():-
-------
text = "HELLO"
print(text.isupper())

replace():-
--------
text = "I like Java"
print(text.replace("Java", "Python"))

isalpha():-
--------
text = "Python"
print(text.isalpha())

split():-
-------
text = "Python is easy"
print(text.split())

isdigit():-
--------
num = "1234"
print(num.isdigit())
'''



'''Break --> this is used to exit from the loop when we find the require element or value...

for j in range(1,10):
    print(j)
    if j == 5:
        break


lis_ = [1,2,3,4]
for n in lis_:
    print(n)
    if n == 1:
        break


Continue --> This is used to skip that particular loop 
for j in range(1,10):
  if j == 5:
      continue
  print(j)


lis_ =  [1,2,3,4]
for n in lis_:
    if n == 3:
        continue
    print(n)


Pass --> This is called as space holder,it is used when incase any statement like(if , for ,else, elif...)
this should be complete , if not we will get indentation error to avoid this we are using pass 

for j in range(1,100):
    pass

else -- for
-----------
it will fall back to else block, when all the loops are completed

for m in range(1,10):
    print(m)
else:
    print("else block")

While --> this is a combination of for and if statements , if we did not end the loop in proper way it will run
upto the memory space in the system becomes empty


'''
'''#fibonnaci series
user_in = int(input("Enter the limit:"))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")
      
'''

num = "1234"
print(num.isdigit())
























