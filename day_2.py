# this_tuple=("a","p","p","u")
# print(this_tuple[1])

# print(this_tuple[0:4])
  

# # changing the value of tuples
# x=("asd","dfg","ghj","jkl")
# c=list(x)
# c[1]="abcd"
# d=tuple(c)
# print(d)

# """
# Key Idea: * in unpacking

# The * operator tells Python: “put all the leftover values here as a list”.

# You can use it in different positions:
# """

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print("\nthe output for the unpaacking is ")
# print(green)
# print(yellow)
# print(red)


# tupl_1=("appu","cherry","apple","rasberry")
# for i in tupl_1:
#     print(i)

# print("using the range function")
# for i in range(len(tupl_1)):
#     print(tupl_1[i])


# fruits1= ("apple", "banana", "cherry")
# mytuple = fruits1 * 2

# print(mytuple) 

# # Return the number of times the value 5 appears in the tuple:

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# print("number of times 5 occurs")
# print(x)
# print("the index of 8 is ")
# y=thistuple.index(8)
# print(y)

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)
# set2={"apple","orange","watermelon"}
# thisset.update(set2)
# print("the set is",thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print("\n\nthe output using the update method")
# print(thisset)

# #Remove "banana" by using the remove() method:

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print("Output using the remove method")
# print(thisset)


# #joining the set into the new using the union function

# set_a={'appu','banana','apple',"asdfghj"}
# set_b={'apple','orange','pineapple',"asdfghj"}
# set_z=set_a | set_b
# print("the output using the union method ")
# print(set_z)

# set_a.clear()
# print(set_a)

# set_c={"asdfghj"}
# x=set_c.difference(set_b,set_a)
# print("to print the difference in the set ")
# print(x)

# def new_func():
#     x1={"apple","banana","orange"}
#     x2={"apple","orange","watermelon"}
#     y1=x1.intersection(x2)
#     print(y1)

# new_func()


# def new_func1():
#     x1={"apple","banana","orange"}
#     x2={"apple","orange","watermelon"}
#     y1=x1.symmetric_difference(x2)
#     print("the symmetric difference")
#     print(y1)

# new_func1()

# def dict_func():
#     x={"model":"mustang",
#        "year":2025}
#     print(x)

# dict_func()

# def dict_func1(x):
#     print(x["brand"])

# x={"brand":"appu"}
# dict_func1(x)

# # the dict as a constructor 
# x1=dict(age=32,location="India")
# print(x1)

# d=x1.keys()
# v=x1.values()
# print("\nthe values for the dictionary")
# print(v)
# print("\nthe keys for the dictionary ")
# print(d)

# x2={"age":22,"name":"appu"}
# x2["age"]=21
# print(x2)


# x3={"age":22,"name":"appu"}
# print("the creating a update method ")
# x3.update({"location":"chennai"})
# print(x3)

# day = 4
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 7:
#     print("Today is Sunday")
#   case _:
#     print("Looking forward to the Weekend")

# day=2
# match day:
#     case 1|2|3|4|5:
#         print("This is a weekdays")
#     case 6|7:
#         print("this is holiday")


# day=4
# match day:
#     case 1|2|3:
#         print("this is a weekdays")
    
#     case _:
#         print("looking for the message")

# day=6
# month=4
# match day:
#     case 1|2|3|4|5:
#         if month==4:
#            print("A normal day in april")
#     case 6|7:
#         if month==4:
#            print("A weekend in april")

# def func1(a,b):
#     add=a+b
#     print(add)

# func1(5,5)

# def func(a):
#     count=0
#     for i in range(len(a)):
#         count+=a[i]

#     print(count)

# a=[1,2,3,4,5]
# func(a)

# def alpha1(a):
#     if a.isalnum():
#         return True
#     else:
#         return False
    
# a="appu123"
# if alpha1(a):
#     print("IT IS ALPHABET")
# else:
#     print("no alpha")


# def func1(*sno,**kid):
#     print(sno[0],"My child last name is",kid["lname"])

# func1(1,2,3,fname="appu",lname="chin")

# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner
# def chaning(func):
#     def myinner():
#         return func().lower()
#     return myinner
# @changecase
# def funct1():
#     return "Happie"
# @chaning
# def func2():
#     return "SAD"
# print(funct1())
# print(func2())



# def changecase(func):
#     def inner(x):
#         return func(x).upper()
#     return inner

# @changecase
# def func1(nam):
#     return "hello"+" "+ nam

# print(func1("appu"))

# import functools

# def changecase(func):
#   @functools.wraps(func)
#   def myinner():
#     return func().upper()
#   return myinner
# @changecase
# def myfunction():
#   return "Have a great day!"
# print(myfunction.__name__)




def changecase(n):
    def decorator(func):
        def myinner(x):
           if n==1:
              print("The apples are",func(x))
           else:
              print("no apples are there")
        return myinner
    return decorator
@changecase(2)
def func1(x):
    return x +" Color "
func1("RED")


