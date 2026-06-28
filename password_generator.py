import random
import string
while True:
    print("\n---PASSWORD GENERATOR---")
    #ask for length and checkif it is at least 8
    length=int(input("Enter password length(minimum 8):"))
    if length<8:
        prinmt("error:Length must be 8 or more!")
     #Ask user what to include   
    print("Enter 'y' for yes and 'n' for no:")
    letters=input("Include Letters(a-z,A-Z)?")
    numbers=input("Include Numbers(0-9)?")
    symbols=input("Include symbols(@,#,$)?")
    #build character pool based on choice
    pool=""
    if letters=='y':
        pool+=string.ascii_letters
    if numbers=='y':
        pool+=string.digits
    if symbols=='y':
        pool+=string.punctuation   
    #check if user selected at least something
    if pool=="":
        print("Error:You must select at least one character type!")
        #generate password
        password=''.join(random.choice(pool) for i in range(length))
        print("Your Password is:",password)
    #ask to run again
    again=input("\nGenerat another passwoed?(y/n):")
    if again!='y':
        print("Goodbye!")
        break            

