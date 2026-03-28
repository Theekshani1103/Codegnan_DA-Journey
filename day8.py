Dictionaries : We can store data as KEY : VALUE
keys()--- are unique and immutable
values()--- all data types are (immutable and mutable) used to get all values from the dict.
clear()---  used to delete the dict.
epresented by "{}"

cod_var = {"name":"Theekshani","Role":"Student","C-id":1234}
print(cod_var.keys())
print(cod_var.values())
cod_var.clear()
print(cod_var)

set{}---> set data type is a unordered collection and it never allow duplicates.

methods
-------
union--- this is used add or get 2 diferent sets without duplicated
intersection --- this method is used to find out commion items from 2 sets
difference --- this method is used to find the different once from the 2nd set



any = {1,2,3,4}
so = {4,5,6}
print (any.union(so))
print (any.intersection(so))
print (any.difference(so))


User={"Name":"Theekshani","Pin":1234}
user_pin = int(input("Enter the Pin :"))
if user_pin in User.values():
       print("Entered Pin was Correct")
else :                                                                        
       print("Entered Pin was Incorrect")   


Tasks :
    1. From any random book take a para of 2-3 lines by using for loop, if-else tell the count of consonants,
       vowels,and  spaces.
       
