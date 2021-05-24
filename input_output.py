from os import lseek
from translate import Translator

try: 
    with open('sad.txt', mode='r') as my_file:
        # text = my_file.read(':(')
        print(my_file.read())
except FileNotFoundError as err: 
    print("file does not exist")
    raise err 
except IOError as err:
    print('IO error here')
    raise err 


# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

translator = Translator(to_lang='ko')

try: 
    with open('./translate.txt', mode='r') as my_translate:
        # text = my_translate.read("how many people are in your house?")
        text = my_translate.read()
        translation = translator.translate(text)
        with open('./test-ko.txt', mode='w') as my_translate2:
            my_translate2.write(translation)
except FileNotFoundError as e:
    print('check your faile path!')







