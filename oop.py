#OOP

# class BigObject: #Class
# 	pass

# obj1 = BigObject() # Instantiate
# obj2 = BigObject() # Instantiate
# obj3 = BigObject() # Instantiate

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

# class PlayerCharacter:
# 	# Class Object Attribute
# 	membership = True
# 	def __init__(self, name, age):
# 		if (self.membership): # or PlayerCharacter.membership works the same
# 			self.name = name #attributes
# 			self.age = age


# 	def run(self, hello):
# 		print(hello)
# 		return 'done'

# 	def shout(self):
# 		print(f'my name is {self.name}')


# player1 = PlayerCharacter('Ocean', 2)
# player2 = PlayerCharacter('Injae', 35)
# player2.attack = 50 

# print(player1)
# print(player1.name)
# print(player2.name)
# print(player1.age)
# print(player2.age)
# print(player1.run('hello'))

# print(player2.attack)

# print(player1.membership)
# print(player2.membership)

# print(player2.shout())

# __init__

# class PlayerCharacter:
# 	# Class Object Attribute
# 	membership = True
# 	def __init__(self, name='member', age=0):
# 		if (age > 18):
# 			self.name = name
# 			self.age = age

# 	def shout(self): 
# 		print(f'my name is {self.name}')

# player1 = PlayerCharacter('Tom', 20)
# player2 = PlayerCharacter()

# print(player1.shout())

#Given the below class:
class Cat:
    species = 'mammal'
    cats = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def set(self):
    	cats[self.name] = self.age

# put cats in dict
# compare age
# return the oldest
    	
def oldest(cat_dict):
 	cats = {}
 	cats[cat_dict.name] = cat_dict.age
 	return cats


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("a", 1)
cat2 = Cat('b', 2)
cat3 = Cat('c', 3)


# 2 Create a function that finds the oldest cat
#{}
def get_oldest(*args):
	return max(args)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The odest cat is {get_oldest(cat1.age, cat2.age, cat3.age)} years old')














