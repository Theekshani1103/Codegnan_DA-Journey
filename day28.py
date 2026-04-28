'''
Regular expressions(RegEx)
--------------------------
-->This is the regular expression or regex is a sequence of characters
that forms a searching pattern.
--> To use this we have to import re, which will unlock the package

Functions
---------
1)findall
---------
--> by using this function, it will find all the sequence in the string
syntax--> re.findall(metachar,variable_name)

import re
any = "This is the regular234 expression or regex is a sequence of characters"
so = re.findall("[a-z]",any)
print(so)

2)search
--------
--> by using this function,it will only find the first sequence in the string
syntax--> re.search("metachar",variable_name)

import re
any = "This is the regular234 expression or regex is a sequence of characters"
an = re.search("[a]",any)
print(an)

metacharacters
--------------
--> metacharacters are used to``form searching pattern
1)[]
----
--> In this meta charcter we can search for [a-z],[A-Z],[0-9]
import re
any = "This is the regular234 expression or regex is a sequence of characters"
an = re.search("[a-z0-9]",any)
print(an)


2)dot(.)
--------
--> This metacharcter will form a searching pattern as it will take any single character for(.)
import re
we = "hello"
the = re.findall("h...o",we)
v = re.search("he..o",we)
print(the)
print(v)



3)^
---
-->This metacharacter  is used to find the string starting with the sequence or not"
import re
how = "This is used to find the string starting with the sequence of the characters"
who = re.findall("^This is",how)
then = re.search("^This",how)
print(who)
print(then)

4)$
---
--> This is used to find the string ending with sequence or not
import re
out = "This is used to find the string starting with the sequence of"
one = re.findall("of$",out)
two = re.search("of$",out)
print(one)
print(two)

5)*
---
--> This metacharcter will form a searching pattern as it will take any zero or more character for(*)
syntax --> re.findall(".*",variable_name)

import re
honey = "This is used to find the string starting with the sequence "
v = re.findall("u.*i",honey)
t = re.search("r.*i",honey)
print(v)
print(t)

6)+
---
--> This metacharcter will form a searching pattern as it will take any one or more character for(+)
syntax --> re.search(".+",variable_name)

import re
honey = "This is used to find the string starting with the sequence "
v = re.findall("a.+y",honey)
t = re.search("r.+e",honey)
print(v)
print(t)



7. ?
----
-->This metha character will form a searching pattern as it will take any zero or one character for (?)
syntax:- re.findall(".?",variable_name)

import re
any ="This is meta used to find the string is ending with the sequence or not"
an = re.findall("This.?",any)
has = re.search("This.?",any)
print(an)
print(has)

8.{}
----
-->This meta character will form a searching pattern as we mention the size in the {}
import re
syntax:- re.findall(".{size}",variable_name)

import re
any ="This is meta used to find the string is ending with the sequence or not"
an = re.findall("This.{11}",any)
has = re.search("This.{8}",any)
print(an)
print(has)

9. |
----
-->this meta character will form a searching pattern as it consider
right or left any string is present or not for (|)
syntax:- re.findall("string|string",variable_name)

import re
any ="This is meta used to find the string is ending with the sequence or not"
an = re.findall("this|not",any)
has = re.search("this|to",any)
print(an)
print(has)'''











