# def get_prime(n):
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("it is prime,",n)
# get_prime(17)


#######################

# w="aabbcc"
# d={}
# for char in w:
#     d[char]=d.get(char,0)+1
# print(d)

########################
# import random
# def num_guessing_game():
#     print("welcome to the number guess game:")
#     attempt=0
#     guess=None
#     num=random.randint(1,100)

#     while guess!=num:
#         guess=int(input("Enter the guessing number :"))
#         attempt+=1
#         if guess>num:
#             print("THE NUMBER IS SMALLER THAN YOU GUESSED")
#         elif guess<num:
#             print("THE NUMBER IS LARGER THAN YOU GUESSED ")
#         else:
#             print("YOU GUESSED CORRECTLY")

# num_guessing_game()



##################
# import random 
# def game():
#     choices=["rock","paper","scissors"]
#     won=0

#     while True:
#         user_choice=input("rock paper scissors :").lower()
#         bot_choice=random.choice(choices)
#         if user_choice not in choices:
#             print("invalid choice")
#             continue
    
#         elif user_choice==bot_choice:
#             print("it is a draw")
#             print("your choice :",user_choice)
#             print("bot_choice :",bot_choice)
#         elif user_choice in choices:
#             if (user_choice =="rock" and bot_choice=="scissors") | (user_choice=="scissors" and bot_choice=="paper") | (user_choice=="paper" and bot_choice=="scissors"):
#                print("you win")
#                print("your choice :",user_choice)
#                print("bot_choice :",bot_choice)
#                won+=1
#                break
#             else:
#                print("computer wins")
#                print("your choice :",user_choice)
#                print("bot_choice :",bot_choice)
# game()


#######

# try:
#     x = int(input("Enter a number: "))
#     y = 10 / x
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
# #     print("You cannot divide by zero!")

##########################################

# x=10

# try:
#     b=int(input("enter the number:"))
#     print("project intiated")
#     c=x/b
# except ValueError:
#     print("the value cannot be string")
# except ZeroDivisionError:
#     print("the value is cannot divided by zero")
# except Exception as e:
#     print("something went wrong error is",e)

####################
try :
    l=[1,2,3,4,5]
    c=int(input("Give me the index number that should be print:"))
    c-=1
    print(l[c])
except IndexError:
    print("the index you called is out of range")
except ValueError:
    print("The value it cannot be string")


