from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))
sentence = 'blah ahahah haha' 

print(Counter(li))
print(Counter(sentence))

# dictionary = {'a': 1, 'b':2}

dictionary = defaultdict(str,{'a': 1, 'b':2})

print(str)
print(dictionary['y'])

dc = OrderedDict()
dc['a'] = 1 
dc['b'] = 2 

dc2 = OrderedDict()
dc2['b'] = 2
dc2['a'] = 1

# print(dc == dc2)
# print(dc2)
# print(dc)

dc = {'c': 100}
dc['a'] = 1 
dc['b'] = 2 

dc2 = {'c': 100}
dc2['b'] = 2
dc2['a'] = 1

print(dc == dc2)
print(dc2)
print(dc)