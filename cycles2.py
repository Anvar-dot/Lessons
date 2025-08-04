# cycle for
# строка это последовательность символов 
# цикл for используется для перебора элементов в последовательности

# text = "Hello, world!"
# # print(text[0:5])


# for перменная in последовательность :
#     действия

# for i in text:
#     print(i, end=' ')
    
#range это функция которая создает последовательность чисел
# range(start, stop, step)
# start - начальное значение (включительно)
# stop - конечное значение (исключительно)
# step - шаг (по умолчанию 1)

# for i in range(0,21,3):
#     print(i)

# num = int(input("Введите число: "))

# for i in range(1, 11):
#     result = num * i
#     print(f"{num} * {i} = {result}")


# for i in range(11,1, -1):
#     for j in range(1, i -1):
#         print(j, end=' ')
#     print()
    
    
import random
import string

def generate_password(length=10):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password())
print(f"Сгенерированный пароль: {generate_password(20)}")