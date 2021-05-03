# @classmethod
# @staticmethod 

from time import time 

def hello():
    print("hellooo"); 

greet = hello

del hello 

# print(greet()) 

def helo(func):
    func()

def greet():
    print('still here')

# a = helo(greet)

# print(a)


#Higher Order Functoin (HOC)

# def greet(func):
#     func()

# def greet2(): 
#     def func(): 
#         return 5
#     return func 

#Decorator 

def m_dec(func):
    def wrap_func(x, y):
        print ("************")
        func(x, y)
        print ("************")
    return wrap_func

# easier & cleaner way
def m_dec(func):
    def wrap_func(*args, **kwargs):
        # print ("************")
        func(*args, **kwargs)
        # print ("************")
    return wrap_func

# def hi():
#     print('hiiii')

# @m_dec 
# def bye():
#     print("see ya later")

# bye()

@m_dec
def hi(greeting, emoji=':/'):
    print(greeting, emoji)

# hi('hi')

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result 
    return wrapper

@performance 
def long_time(): 
    for i in range(10000000): 
        i*5 

# long_time()

#exercise

user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
    def wrap(*args, **kwargs):
        # print(*args['valid'])
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrap
        
@authenticated
def message_friend(user):
    print('msg sent')

message_friend(user1)







