range(100)
list(range(100))

def make_list(num):
    result = [] 
    for i in range(num):
        result.append(i*2)
    return result 

# my_list = make_list(100)
# print(my_list) 

def generator_func(num):
    for i in range(num):
        yield i*2

g = generator_func(100)
print(g)

def special(iterable):
    iterator = iter(iterable)
    while True:
        try: 
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

# special([1,2,3])

# range method under the hood
class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first 
        self.last = last 
    
    def __iter__(self):
        return self 

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current 
            MyGen.current +=1
            return num
        raise StopIteration 


# gen = MyGen(0,100)
# for i in gen:
#     print(i)

# fibonacci numbers in generator and in list

def fib(number):
    a = 0 
    b = 1 
    for i in range(number):
       yield a
       temp = a
       a = b 
       b = temp + b

for x in fib(10000):
    print(x)


def fib2(number):
    a = 0 
    b = 1 
    result = []
    for i in range(number):
       result.append(a)
       temp = a
       a = b 
       b = temp + b
    return result

# print(fib2(20))



 

# def fib(n):
#     range(n)


