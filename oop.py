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

class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name 
		self.age = age


	def run(self):
		print('run')
		return 'done'

player1 = PlayerCharacter('Ocean', 2)
player2 = PlayerCharacter('Injae', 35)
player2.attack = 50 

print(player1)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
print(player1.run())

print(player2.attack)






