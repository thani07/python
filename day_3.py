# x=lambda a:a+5
# print(x(5))

# def adds(n):
#     return lambda a,b: a+b+n

# mydoubler=adds(5)
# print(mydoubler(5,5))


# def func(n):
#     return lambda a:a*n

# square=func(2)
# print("the square root",square(2))

# triple=func(3)
# print("the triple root is",triple(2))

# quad=func(4)
# print("the quad root is",quad(2))

# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]


# models.sort(key=lambda x:x['color'])
# print(models)



# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# even_nums=list(filter(lambda x:x%2==0,n))
# odd_nums=list(filter(lambda x:x%2 !=0,n))
# print(even_nums)
# print(odd_nums)



# lesser_10=list(filter(lambda x:x<10,n))
# greater_10=list(filter(lambda x:x>10,n))
# print(lesser_10,greater_10)

# square_x=list(map(lambda x:x**2,n))
# print(square_x)
# triple_x=list(map(lambda x:x**3,n))
# print(triple_x)

# starts_with=lambda x: True if x.startswith('P') and x.endswith('n') else False
# print(starts_with('Python'))

# length=lambda x: True if len(x)==5 else False
# print(length("Pythn"))


# import datetime

# now=datetime.datetime.now()
# print(now)

# year=lambda x:x.year
# date=lambda x:x.date()
# t=lambda x:x.time()

# print(year(now))
# print(date(now))
# print(t(now))


# import array

# n=array.array("i",[1,2,3,4])
# print(n)

x=["a","e","i","o","u","A",'E','I','O','U']
n=input("Enter a string")
c={}
for char in n:
    if char in x:
        c[char]=c.get(char,0)+1
print(c)

