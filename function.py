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


def is_even(number):
    if number % 2 ==0:
        return "Число четное."
    else:
        return "Число нечетное."
    
print(is_even(123))