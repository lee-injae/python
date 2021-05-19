from functools import reduce


def multiply_by2(li): 
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# map, filter, zip, and reduce 

print(map(multiply_by2, [1,2,3]))

my_list = [1,2,3]
u_list = [10,20,30]
t_list = (5,4,3)

# def multiply_by2(item): 
#     return item*2

# print(multiply_by2([1,2,3]))


# map, filter, zip, and reduce 

# print(map(multiply_by2, [1,2,3]))
# print(my_list)

def only_odd(item): 
    return item % 2 != 0 

def accumulator(acc, item):
    print(acc, item)
    return acc + item

# print(filter(only_odd, my_list))
# print(my_list)

# print(zip(my_list, u_list, t_list))

# print(reduce(accumulator,my_list, 0))

# ======================
# exercise
# ======================

#1. Captialize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'marley']

def caps(item):
    return item.capitalize 

# print(list(map(caps, my_pets)))

#2. Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest. 
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# print(zip(my_strings, sorted(my_numbers)))

#3. Filter the scores taht pass over 50%

scores = [73,20,65,19,76,100,88]

def over50(item):
    return item > 50

# print(filter(over50, scores))

#4. Combine all of the numbers that are in a list of this file using reduce (my_numbers and scores). what is the total? 

def add(acc, item):
    return item + acc 

# print (my_numbers + scores)

# print(reduce(add, (my_numbers + scores)))

# Lambda expressions 
lambda param: action(parameter)

# print(reduce(lambda acc, item: acc+item, my_list))

m_list = [5,4,3]

# print(map(lambda item: item **2, m_list))

# sort
a = [(0,2), (4,3), (9,9), (10,-1)]

# print(a.sort(key=lambda x: x[1]))
# print(a)

#list, set, dictionary comprehension 

m_listing = [char for char in 'hello']
m_listing2 = [num for num in range(0,100)]
m_listing3 = [num**2 for num in range(0,100)]
m_listing4 = [num**2 for num in range(0,100) if num % 2 ==0]

# print(m_listing4)

m_listing = {char for char in 'hello'}
m_listing2 = {num for num in range(0,100)}

# print(m_listing)

simple = {
    'a': 1,
    'b': 2
}

# print(simple.items())

my_dict = {key: value**2 for key, value in simple.items() if value % 2 == 0}
my_dict2 ={num: num*2 for num in [1,2,3]}

# print(my_dict2)

# Comprehension exercise 

s_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in s_list: 
#     if s_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)
duplicates = list(set([x for x in s_list if s_list.count(x) > 1]))

print(duplicates)













