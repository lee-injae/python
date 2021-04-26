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
# class Cat:
#     species = 'mammal'
#     cats = {}
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

#     def set(self):
#     	cats[self.name] = self.age

# put cats in dict
# compare age
# return the oldest
    	
# def oldest(cat_dict):
#  	cats = {}
#  	cats[cat_dict.name] = cat_dict.age
#  	return cats


# 1 Instantiate the Cat object with 3 cats
# cat1 = Cat("a", 1)
# cat2 = Cat('b', 2)
# cat3 = Cat('c', 3)


# 2 Create a function that finds the oldest cat
#{}
# def get_oldest(*args):
# 	return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# print(f'The odest cat is {get_oldest(cat1.age, cat2.age, cat3.age)} years old')

#users
    
# class User:
    # def __init__(self, email):
    #     self.email = email

#     def sign_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name, power):
#         # super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         # User.attack(self)
#         print(f'attacking with power of {self.power}')
           
# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def check_arrows(self):
#         print(f'{self.arrows} remaining')
    
#     def run(self):
#         print('ran fast')

    # def attack(self):
    #     print(f'attacking with arrows: arrows left- {self.num_arrows}')

# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)

# borg1 = HybridBorg('oc', 10, 100)

# # print(borg1.check_arrows())
# print(borg1.attack())
# print(borg1.sign_in())


# # bb = User('b@b.com')
# # print(bb.email)

# wizard1 = Wizard('ocean', 50, 'a@a.com')
# archer1 = Archer('injae', 100)

# # print(dir(wizard1))

# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age 
#         self.my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }

#     def __str__(self):
#         return f'{self.color}'

#     def __len__(self):
#         return 5

#     def __call__(self):
#         print('called')

#     def __getitem__(self, i):
#         return self.my_dict[i]



# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])









# print(wizard1)

# print(wizard1)
# print(wizard1.sign_in())
# wizard1.attack()
# archer1.attack()

# print(isinstance(wizard1, object))

# def p_attack(char):
#     char.attack()

# p_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

class SuperList(list):
    def __len__(self):
        return 1000

    
superlist1 = SuperList()
superlist1.append(4)
# print(len(superlist1))

# print(superlist1[0])
# print(issubclass(list, object))


#1 Add another Cat

# cat1 = Cat('ocean', 2)
# cat2 = Cat('ij', 3)
# cat3 = Cat('karam', 4)

# class Marley(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)

# my_cats = [Simon('simon', 3), Sally('sally', 4), Marley('marley',9)]

# print(my_cats)
#3 Instantiate the Pet class with all your cats use cariable my_pets

# my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance

# my_pets.walk()


#MRO - Method Resolution Order
# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1 

# class D(B,C):
#     pass 

# print(D.mro())

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)










