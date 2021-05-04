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


gen = MyGen(0,100)
for i in gen:
    print(i)



