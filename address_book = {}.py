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
    print("Contact or name not found")
   
   
address_book = {
   
    "contact 1" : {
        "name" : "negga1",
        "num" : "09967872154"
    },
    "contact 2" : {
        "name" : "negga 2",
        "num" : "01864173245"
    },
    "contact 3" : {
        "name" : "negga 3",
        "num" : "09565628936"
    },
}