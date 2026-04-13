'''
Generators
----------
--> This is a special type of function that returns an ITERATOR which one at a time

Yield
-----
--> It will take a pause and again resume, this is not a nrml keyword can not be used in the nrml functions
--> This is used to produce a value and pause execution.

Next
----
--> This is used to get next value from a generator
--> When a value is finished,it will stop the iterator 

def my_generator():
    yield 10
    yield 20
    yield 30
honey = my_generator()
print(next(honey))
print(next(honey))
print(next(honey))


def sq_gen(n):
    for i in range(n):
        yield i*i
for value in sq_gen(5):
    print(value)

def sub(n):
    for i in range(n):
        yield i-10
for value in sub(6):
    print(value)

def add(n):
    for i in range(n):
        yield i+10
for value in add(100):
    print(value)

def div(n):
    for i in range(n):
        yield i/10
for value in div(15):
    print(value)

def mod(n):
    for i in range(n):
        yield i%10
for value in mod(15):
    print(value)'''


'''SBI_Theeku_AC_details={"name":"Theeku",
                     "ATM PIN":"2004",
                     "Balance":5000}
while True:
    print("\n===== Welcome to SBI ATM =====")
    print("Please insert your ATM card")
    SBI_user_pin=input("Enter your 4 digit ATM PIN: ")
    if len(SBI_user_pin)== 4 and SBI_user_pin.isdigit():
        if SBI_user_pin == SBI_Theeku_AC_details["ATM PIN"]:
            print("PIN correct")
            user_choice = int(input("Enter:\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Change PIN\n5.Exit\n"))
            if user_choice == 1:
                money_w=int(input("Enter amount: "))
                if money_w<=SBI_Theeku_AC_details["Balance"]:
                    SBI_Theeku_AC_details["Balance"]-=money_w
                    print("Balance:",SBI_Theeku_AC_details["Balance"])
                else:
                    print("Insufficient balance")
            elif user_choice == 2:
                deposit_m = int(input("Enter amount: "))
                if deposit_m % 100 == 0 and deposit_m >= 100:
                    SBI_Theeku_AC_details["Balance"] += deposit_m
                    print("Total balance:",SBI_Theeku_AC_details["Balance"])
                else:
                    print("Invalid amount")
            elif user_choice == 3:
                print("Balance:",SBI_Theeku_AC_details["Balance"])
            elif user_choice == 4:
                attempts=3
                while attempts>0:
                    old_pin=input("Enter old PIN: ")
                    if old_pin==SBI_Theeku_AC_details["ATM PIN"]:
                        new_pin=input("Enter new 4 digit PIN: ")
                        if len(new_pin)==4 and new_pin.isdigit():
                            SBI_Theeku_AC_details["ATM PIN"]=new_pin
                            print("PIN changed successfully")
                            break
                        else:
                            print("Invalid new PIN")
                    else:
                        attempts-=1
                        print("Wrong PIN, attempts left:",attempts)
                continue
            elif user_choice==5:
                print("Thank you")
                break
            else:
                print("Invalid choice")
        else:
            print("Invalid PIN")
    else:
        print("Enter valid 4 digit PIN")'''








