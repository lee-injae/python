# print(f"Hi {username}, your pw {hidden_pw} is {pw_length} letters long")

# int
# float
# bool
# str
# list
# tuple
# set
# dict
# fundamental data type
# Classes -> custom types
# age = input('how old are you?')
# print("so young " + age )

# print(9 % 7)
# print(9 // 7)
# print(type( 3 / 6))
# print(round(5.5))
# print(abs(-9))

# import math
# print(round(-5.4))
# print(math.floor(-5.4))
# print(math.ceil(-5.9999))
# print(math.ceil(5.0008))


#operator precedence
# ()
# **
# * /
# + -

# print((30-7) - 5 ** 2)
# print(4 / 2)
# print(4 // 2)
# print(5 + (4 * 10) / 2)
# print(5 + (4 * 10) // 2)

# print(-1 // 5 )

# print(bin(10))
# print(int('0b1010', 2))

# iq = 190
# print(iq)

# variables
# -snake_case
# -Letters, numbers, underscores,
# -case sensitive
# -Don't overwite keywords

# iq = 200

# iq2 = 2

# h = iq / iq2

# d = h

# print(d)

# a, b, c = 1,2,3

# print(a)
# print(c)

# some = 5

# some *= 4
# some += 3

# print(some)

# print(type("ocean"))

# long_string = '''
# WOW
# O O 
# ___ 
# ''' 

# print(long_string)
# first_name = 'injae'
# last_name = '5'

# full = first_name + " " + last_name
# print(full)

# Type conversion
# print(type(int(str(100))))

# Escape Sequence
# weather = "It's Sunny"
# sun = "\t It\\s \"kind of\" sunny \n hope you have a good day"

# print(sun)

#formatted string   

# name = 'Ocean'
# age = 2
# print("hi " + name + '. You are ' + str(age) + ' years old')

# name = "Ocean"
# age = 2 

# print(f'Hi {name}. You are {age} years old')

# print('hi {}. You are {} years old'.format('Ocean', '2'))

# print('hi {1}. You are {0} years old'.format(name, age))

# print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))

# string = "01234567"
         #01234567

# [start:stop:stepover]
# default stepover is 1

# print(string[2:7:1])
# print(string[2:8:2])
#default end go all the way 
# print(string[2:])
#default begin is 0 
# print(string[:4])
# :: also gives default behavior
# print(string[::2])
# negative index means start from back
# print(string[-2])
#start stop but stopover from back
# print(string[::-1])
# print(string[::-2])

#immutability
# son = "oceanjunglee"
# print(son[0:len(son)])
# quote = 'to be or not to be'

#builtin function vs method
# functions are global
# methods are owned by something(ex:.format in string)
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be', 'me'))
# print(quote)

#booleans
# bool

# name = 'Ocean'
# age = 40
# relationship = 'it\'s complicated'
# is_cool = False
# is_cool = True


# birth_year = int(input('what year were you born?'))
# current = 2020
# age = current - float(birth_year)
# print(f'your age is: {age}')

# username = input("username?")
# pw = input("password?")

# hidden_pw = '*' * len(pw)
# pw_length = len(pw)

# print(f'Hi {username}!, your password {hidden_pw} is {pw_length} letters long')

# list

#List slicing
# List is mutable


# cart = ["toy", "grape", "pillow", "apple"]
# cart[0] = 'laptop'
# new_cart = cart[:]
# new_cart[0] = 'gum'

# print(cart)
# print(new_cart)
  
#Matrix 
# matrix = [
#   [1,2,3]
#   [4,5,6]
#   [7,8,9]
# ]

#adding
# basket = ['a','b','c','d','e', 'd']
# print(len(basket))
# basket.append(100)
# basket.insert(3,300)
# new_list = basket.extend(["a", "b"])
# new = basket
#removing
# value = basket.clear()
#pop returns value
# basket.remove(2)
# print(basket.count('d'))
# print(new_list)

# using this list, 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
# basket.pop(0)
# basket.remove('Banana')
# print(basket)
# 2. Remove "Blueberries" from the list.
# basket.pop(3)
# basket.pop()
# print(basket)
# 3. Put "Kiwi" at the end of the list.
# basket.append('Kiwi')

# 4. Add "Apples" at the beginning of the list
# basket.insert(0,'Apples')
# 5. Count how many apples in the basket
# print(basket.count('Apples'))
# 6. empty the basket
# print(basket.clear())
# print(basket)

# basket = ['x','a','b','c','d','e', 'd']

# print(sorted(basket))
# basket.sort()
# print(basket)
# basket.sort()
# basket.reverse()
# print(basket) 
# basket.sort()
# basket.reverse()

# print(basket[::-1])
# print(basket)
# print(list(range(101)))

# new = ' '.join(['hi', 'my', 'name', 'is', 'Ocean'])
# print(new)

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# friends.sort()

# new_friend = ['Stanley']
# stan = new_friend[0]
# friends.append(stan)
# print(friends)
# print(new_friend)

# friends.extend(new_friend)
# print(sorted(friends))

#list unpacking
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

# print(d)

#Dictionary

# d = {
#   '123':[1,3],
#   'kk':True,
#   '[100]':"hello",
#   'age': 20
# }

# ii = dict(name= 'ocean')
# print(d.get('age', 88))
# print(ii)

# print(d.update({'ages': 99}))
# print(d)

#tuple -> immutable list

# mtuple = (1,2,3,4,5,5)
# ntuple = mtuple[1:2]
# x, y, z, *other = (1,2,3,4,5)

# print(len(mtuple)) 

#set
# ms = {4,5,5}
# ms.add(99)
# ms.add(1)
# print(ms)
# ys = {4,5,6,7,8,9,10}
# print(ys)
# print(set(ms))

# new = ms.copy()
# new.clear()/
# print(list(ms))
# print(new)

# ys = {4,5,6,7,8,9,10}

# # print(ms.difference(ys))
# # print(ms.discard(5))
# # print(ms)
# # print(ms.difference_update(ys))
# # print(ms)
# # print(ms.intersection(ys))
# # print(ms.isdisjoint(ys))
# print(ms & ys)
# print(ms | ys)
# print(ms.issuperset(ys))
# print(ys.issubset(ms))

# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# s = set(attendance_list)

# print(school.difference(attendance_list))















.p