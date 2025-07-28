# import random 

# secret_number = random.randint(1, 100)
# tries = 5

# while tries > 0:
#     quess = int(input("Угадайте число от 1 до 100:  "))
#     tries -= 1
#     if quess == secret_number:
#         print("Поздравляю! Вы угадали число!")
#         break
#     elif quess < secret_number:
#         print("Ваше число меньше загаданного.")
#     else:
#         print("Ваше число больше загаданного.")
# else:
#     print(f"Вы не угадали число. Загаданное число было {secret_number}.")


# number = input("Введите число: ")
# for digit in number:
#     for i in number:
#         print(f"{digit} + {i}")


number = input("Введите число: ")

total = 0
digits = []

for digit in number:
    total += int(digit)
    digits.append(digit)

print(" + ".join(digits), "=", total)