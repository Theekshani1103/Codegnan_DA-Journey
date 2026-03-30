'''
a = 9
print (a)
for j in range (1,10) :
    print(j)

range () ---> this is used to generate number
syntax ---> range (start,end,step)


for j in range (2,20,2) :
    print(j)

so =  123
print (str(so))
print (float(123))

an = [1,2,3]
vs = str (an)
print (type(vs))
print (vs)
print(tuple(an))'''

rev_str = "tenet"
empty_ = ""
for j in rev_str:
    empty_ = j + empty_
if empty_ == rev_str:
    print(f"{rev_str} is paindrome")
else:
        print(f"{rev_str} is not a palindrome")
        
