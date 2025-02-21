# Zinampan-Programming-2
address_book = {}

#Ensure at least 3 contancts are added
name = input("enter your name")
num = int(input("enter your number"))
 
name = input("enter your name")
num = int(input("enter your number"))

name = input("enter your name")
num = int(input("enter your number"))
 
address_book[name] = num
 
print(f"address book: {address_book}")
 
search = input("lookup name:")
 
if search in address_book:
    print(f"number {address_book[search]}")
   
else:
    print("name not found")
   
   
address_book = {
