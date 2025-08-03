password = input("Введите пароль: ")

def check_password(password):
    if len(password) < 8:
        return "Используйте пароль длиной не менее 8 символов."
    elif not any(char.isdigit() for char in password):
        return "Пароль должен содержать хотя бы одну цифру."
    elif not any(char.isalpha() for char in password):
        return "Пароль должен содержать хотя бы одну букву."
    else:
        return "Пароль принят."
    
    
print(check_password(password))