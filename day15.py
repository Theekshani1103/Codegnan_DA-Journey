'''
Recursive functions
-------------------
Recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by 98breaking it into smaller, simpler subproblems.
Recursion is especially useful for problems that can be 100 divided into identical smaller tasks, such as mathematical calculations, tree traversals or divide-and-conquer
algorithms.

def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num-1) - Fibonacci(num-2)
print(Fibonacci(1))

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit pin:")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print(" welcome to the ATM")
            return true
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f" Invalid pin Attempts left:{sel:self.remaining}")
            else:
                print(" card blocked. Please contact customer")
                return false'''


'''any = "My name is Theekshani"
vowstr_List = []
constr_List = []
def vowel_con(any):
    for j in any:
        if j in "AEIOUaeiou":
            vowstr_List.append(j)
        else:
            constr_List.append(j)
    print(f"{vowel_List} these are all vowels in the string")
vowel_con(any,vowstr_List,constr_List)'''


'''
SBI_Theeku_AC_details={"name":"Theeku",
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
        print("Enter valid 4 digit PIN")

'''












