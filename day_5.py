# import pandas as pd
# data=pd.read_csv("Book(Sheet1).csv")
# class bank:
#     def __init__(self,account_no,name,balance):
#         self.account=account_no
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         a=self.balance
#         print("The amount before deposit",a)
#         self.balance+=amount
#         print("The amount after deposit",self.balance)
#         return self.balance
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance! Withdrawal cancelled.")
#             return self.balance
#         print("The amount before withdraw", self.balance)
#         self.balance -= amount
#         print(f"The balance after the withdraw :\n Withdraw amount {amount}\n Your balance: {self.balance}")
#         return self.balance
#     def balances(self):
#         print("The balance in your account: ",self.balance)

# acc=int(input("enter your account number: "))
# name=input("enter your name: ")
# bac=0
# row=data[data["name"]==name]
# if not row.empty:
#     bac=row["balance"].values[0]
#     print("your balance",bac)
#     obj=bank(acc,name,bac)
#     X=int(input("ENTER THE AMOUNT TO DEPOSIT: "))
#     obj.deposit(X)
#     y=int(input("ENTER THE AMOUNT TO WITHDRAW : "))
#     obj.withdraw(y)
#     print("Do you want to check the balance: ")
#     x=input("yes or no : ")
#     if x=="yes":
#       obj.balances()
#     else:
#       print("Thank you")
# else:
#     print("user is not found")
#######################################

# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print("The Brand And Model is :",self.brand,self.model)
    
# class car(vehicle):
#     def __init__(self,brand,model,rate):
#         super().__init__(brand,model)
#         self.rate=rate
#     def display1(self):
#         super().display()
#         print("The Rate of the vehicle :",self.rate)

# class bike(vehicle):
#     def __init__(self,brand,model,area):
#         super().__init__(brand,model)
#         self.area=area
#     def display2(self):
#         super().display()
#         print("The area of manufactured ",self.area)
# obj=car("xuv","500",100000)
# obj.display1()
# obj1=bike("gt","650",400000)
# obj1.display2()



class iteration:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
obj=iteration()
myiter=iter(obj)
print(next(myiter))