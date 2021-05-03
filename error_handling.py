# Error Handling

while True:
    try: 
        age = int(input('what is your age?'))
        10/age
        # raise ValueError('hey cut it out')
    except ValueError: 
        print('please enter a number')
        continue
    except ZeroDivisionError: 
        print('please enter age higher than 0')
        # break
    else: 
        print('thanks')
        break
    finally:
        print('ok, final')
    print('')


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err: 
#         # print(f'pls enter numbers {err}') 
#         print(err)

# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err: 
#         # print(f'pls enter numbers {err}') 
#         print(err)

# print(sum(1, '4'))



