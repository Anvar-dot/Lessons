# # function.py
# def check_password(password):
#     if len(password) < 8:
#         return "Используйте пароль длиной не менее 8 символов."
#     elif not any(char.isdigit() for char in password):
#         return "Пароль должен содержать хотя бы одну цифру."
#     elif not any(char.isalpha() for char in password):
#         return "Пароль должен содержать хотя бы одну букву."
#     else:
#         return "Пароль принят."
    
    
# while True:
#     password = input("Введите пароль: ")
#     result = check_password(password)
#     print(result)
#     if result == "Пароль принят.":
#         break


# def is_even(number):
#     if number % 2 ==0:
#         return "Число четное."
#     else:
#         return "Число нечетное."
    
# print(is_even(123))

# import random



# secret_number = random.randint(1,10)
# tries = 0

# while True:
#     guess = int(input("Угадайте число от 1 до 10: "))
#     tries += 1
#     if guess == secret_number:
#         print(f"Поздравляю! Вы угадали число {secret_number} за {tries} попыток.")
#         break
#     elif guess < secret_number:
#         print("Ваше число меньше загаданного.")
#     else:
#         print("Ваше число больше загаданного.")


names = str(input("Введите имена через запятую:  "))
def greet_names(names):
    name_list = names.split(",")
    return len(name_list)
    
    
    
print("Количество имен:", greet_names(names))
capitalized_list = []
for item in names:
    capitalized_list.append(item.capitalize())
print(capitalized_list)
# capitalized_list = [item.capitalize() for item in names]
# print(capitalized_list)
# names_capitalized = names.capitalize()
# print(names_capitalized)