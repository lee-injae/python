# is_old = True
# is_licensed = True

# if is_old and is_licensed: 
#   print('you are old enough and licensed')

# else:
#   print('can\'t drive')

# print('oo') 

#Ternary Operator
# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)

#Short Circuiting
# is_friend = True
# is_user = False

# if is_friend or is_user:
#   print("bff")

#Logical Operator
# <> == >= <=
# print(not(True))


# is_m = False
# is_e = True

# check if magician and expert: 'you are a master magician'
# check if magician but not expert: 'at least you're getting better'
# if you are not a magician: 'you need magic powers.'

# if is_m and is_e:
#   print("you are a master magician")
# elif is_m and not(is_e):
#   #elif is_m and not is_e:
#   print("at least you're getting better")
# elif not is_m:
#   print('you need magic powers')
# print(type(10.0))
# print(True == 1)
# print('1' == 1)
# print(type(10) == type(10.0))
# print(10 == 10.0)
# print([] == [])

# 'is' checks the location in memory

# print(True is True)
# print(1 is 1)
# print([] is [])
# print(10 is 10.0)
# a=[1,2,3]
# b=[1,2,3]
# print(b is b)
# print([1,2,3] is [1,2,3])

#loops

# for x in [1,2,3,4,5]:
#   for item in ('a','b','c','d'):
#     print(x, item)
#iterable -list, dictionary, tuple, set, string

# user = {
#   'name': 'injae',
#   'age': 5000,
#   'can_swim': False
# }

# for item in user:
#   print(item)

# for item in user.items():
#   print(item)

# for item in user.values():
#   print(item)

# for item in user.keys():
#   print(item)

# for k, v in user.items():
#   print(k, v)

# for item in 50:
#   print(item)

#counter 
# mlist = [1,2,3,4,5,6,7,8,9,10]

# counter = 0
# for item in mlist:
#   counter += item
# print(counter)

# ounter = 0
# for item in mlist:
#   counter = counter + item
# print(counter)

# for _ in range(10,0,-2):
#   print(_)

# for _ in range(2):
#   print(list(range(10)))

#enumerate

# for i, char in enumerate(list(range(100))):
#   print(i, char)
#   if char == 50:
#     print(f'index of 50 is: {i}')

#while Loop   

# i = 0 
# while i < 50:
#   print(i)
#   # i = i + 1
#   i += 1
#   break
# # else: 
# #   print('done')

# print('done')

#for loop vs while Loop   
# mlist = [1,2,3]
# for item in mlist:
#   print(item)

# i = 0
# while i < len(mlist):
#   print(mlist[i])
#   i += 1 


# while True:
#   response = input("say sth: ")
#   if (response == 'bye'):
#     break

# mlist = [1,2,3]
# for item in mlist:
#   #thinking
#   pass

# i = 0 
# while i < len(mlist):
#   print(mlist[i])
#   i += 1 
#   pass
  
#Exercise!
# pic = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0],
# ]

# for row in pic:
#   for j in row:
#     if (j == 0):
#       print(" ", end="")
#     else:
#       print("*", end="")
#   print(' ')

#iterate over picture.
  # if 0 -> print ''
  # if 1 -> print * 

# slist = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# em = []
# for item in slist:
#   if slist.count(item) > 1:
#     if item not in em:
#       em.append(item)

# print(em)

#parameters
# def say_hello(name, emoji):
#   print(f'hello {name} {emoji}')

# #Default parameters
# def say_hello(name='karam', emoji='OTL'):
#   print(f'hi {name} {emoji}')

# say_hello()

# #arguments
# say_hello('injae', ':)')

# #positional arguments
# say_hello('Andre', ':/')
# say_hello(':?', 'Dan')

# #keyword arguments
# say_hello(emoji=':)', name='Ocean')


# age = input("What is your age?: ")

# def checkDriverAge(age):
#     if int(age) < 18:
#       print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#       print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#       print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(age)

# def checkDriverAge(age=0):

#   if int(age) < 18:
#     print("Sorry")
#   elif int(age) > 18:
#     print("Powering on")
#   elif int(age) == 18:
#     print("Congratulations, get your license") 

# checkDriverAge(18)

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

# long code -> clean code
# def is_even(num):
#   if num % 2 == 0:
#     return True
#   elif num % 2 != 0:
#     return False 

# # clean code      
# def is_even2(num):
#   return num % 2 == 0 

# print(is_even2(8))


#docstring   
 
# def test(a): 
#   '''
#   Info: this function test and prints param a. 
#   '''
#   print(a) 

# help(test)
# print(test.__doc__)

#*args **kwargs

# def super(*args, **kwargs): 
#   total = 0 
#   for items in kwargs.values():
#     total += items 
#   return sum(args) + total

# print(super(1,2,3,4,5, num1=5, num2=10))

#Rule of order: params, *args, default params, **kwargs

# def super_f(name, *args, i='hi', **kwargs):
#   total = 0 
#   for items in kwargs.values():
#     total += items 
#   return sum(args) + total

# print(super_f('Injae', 1,2,3,4, num1=5, num2=10))

 #Exercise
# def high_even(lis):
#   i = 0
#   for item in lis:
#     if (item > i and item % 2 == 0):
#       i = item
#   return i    

# print(high_even([10,2,16,4,8,11]))


# def highest_even(li):
#   evens = []
#   for item in li:
#     if item % 2 == 0:
#       evens.append(item)
#   return max(evens)

# print(highest_even([10,1,2,3,4,8]))

#walrus


# a = "hiiiiiiiiiiiii"
# if (len(a) > 10): 
#   print(f'too long {len(a)} elements')
# #-->
# if ((n := len(a)) > 10): 
#   print(f'too long {n} elements')

# while ((n := len(a)) > 1): 
#   print(n)
#   a = a[:-1]


# print(a)


#scope - what variable do I have access to? 
# a = 1 

# def parent():
#   a = 10
#   def confusion():
#     return a 
#   return confusion()  

# print(a)
# print(parent())

# 1. start with local scope 
# 2. Parent local? 
# 3. Global 
# 4. built in python functions. 

# parameters are considered local variables 

# total = 0 
# def count(): 
#   global total 
#   total += 1 
#   return total 

# count()
# count()
# count()
# print(count())

# total = 0 
# def count(total):
#   total += 1
#   return total 

# print(count(count(count(count(total))))) 
# print(count(count(2)))

# def outer():
#   x = 'local'
#   def inner():
#     nonlocal x 
#     x ='nonlocal'
#     print('inner:', x)

#   inner()
#   print('outer:', x)

# outer()

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car.get("Ford"))

# i = 0
# while i < 6:
#   i += 1
#   if i == 3 or i == 4:
#     continue
#   print(i)

# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function('ocean', 'derek')

# def my_function(**kid):
#   print(kid)    
#   print("His last name is " + kid["fname"])
  
# print(my_function(fname="ocean", lname="lee"))

# def my_f(**kwargs):
#   print(kwargs)

# print(my_f(num1=10, num2=5))


import functional_programming
import shopping.shopping_cart

print(functional_programming.multiply_by2([3,4]))
print(shopping.shopping_cart.buy('pencil'))







