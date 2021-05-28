import re

# print('search' in string) 

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'Injae@gmail.com'

a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

print(a)
# print(b)
# print(c)
# print(d)

# create password validation - 
# at least 8 char long
# contain any sort letters, numbers $%#@ 

pattern2 = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[%$#@])[a-zA-Z0-9$#@%]{8,}\d$")
password = 'asdfasDf553%$#9'

check = pattern2.fullmatch(password)

print(check)


