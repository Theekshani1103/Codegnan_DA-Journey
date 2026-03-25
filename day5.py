'''
Strings --> String is a collection of characters , which represented by "" or '' and we can access a string using
indexing (numbering the string) string can also allow negative indexing and also slicing (cutting the string)(ex:print(any[7:15])).this is also immutable,
where i could not able to modify on that particular vari...'''

'''#any = 'python programming'
#print(any[20])
#so = any.replace("python","Java")
#print(any)
#print(so)'''
'''

a_day = 'i am Theekshani from visakhapatnam , i have completed my btech  in the year 2025 in electronics and communiction engineering'
print(len(a_day))
len()-->it is used to get the char present in the string
#print(f"My name is {a_day[-10:-2]}")(negative indexing)
#print(f"My name is {a_day[2:20]}")(indexing)

#a_day = "Theeku"
#print(a_day[::-1])(Reversing a string)
'''
'''Note: we can convert a string into integer ,if the string contain only integer values... '''
''' methods of string :-
----------------------
1)split()--> remove space, and the is in the list[] each seperated thing in each index
syntax ----> variable_name.split("substring")
2)Lower()--> this is used to convert all letters into lower case
syntax ----> variable_name.lower()
3)Upper()--> ex code ->some = "python is a prograMMing lanGuage"
print(some.upper())
4)replace()---> this is used to replace old str with the new str
syntax---> variable_name.replace("old string","new string")


#some = "python is a programming language"
#print(some.split("is"))'''

'''some = "python is a programming language"
if "A" in some:
    print("yes, it is there")
else:
    print("No , it is not there")

#some = "python is a programming language"
#print(some.replace("programming","nrml"))'''

'''some = "python is a programming language"
if "python" in some:
    print ("yes")
else:
    print("no")'''

word = input("Enter a word:")
count = word.count('a')+ word.count('e')+ word.count('i')+ word.count('o')+ word.count('u')
print("Number of vowels:",count)




