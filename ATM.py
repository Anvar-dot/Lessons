pin_code = "1616"
balance = 10000
tries = 3

# Авторизация
while tries > 0:
    entered_pin = input("Введите PIN-код: ")
    if entered_pin == pin_code:
        print("PIN-код принят.")
        break
    else:
        tries -= 1
        print(f"Неверный PIN-код. Осталось попыток: {tries}")
else:
    print("Доступ заблокирован.")
    exit()

# Главное меню
while True:
    print("\nВы в главном меню:")
    print("1. Проверить баланс")
    print("2. Снять деньги")
    print("3. Пополнить счёт")
    print("4. Выйти")

    menu = input("Выберите действие (1-4): ").strip()

    if menu == "1":
        print(f"Ваш текущий баланс: {balance} руб.")

    elif menu == "2":
        answer = input("Хотите ли вы снять деньги? (да/нет): ").lower()
        if answer == "да":
            minus = int(input("Введите сумму для снятия: "))
            if minus <= balance:
                balance -= minus
                print(f"Вы сняли {minus} руб. Остаток: {balance} руб.")
            else:
                print("Недостаточно средств.")

    elif menu == "3":
        answer = input("Хотите пополнить счёт? (да/нет): ").lower()
        if answer == "да":
            plus = int(input("Введите сумму для пополнения: "))
            balance += plus
            print(f"Вы внесли {plus} руб. Новый баланс: {balance} руб.")

    elif menu == "4":
        print("Выход. Спасибо, что воспользовались банкоматом.")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")



# print("Хотите ли вы снять деньги? (да/нет)")
# if input().lower() == "да":
#     minus = int(input("Введите сумму для снятия: "))
#     if minus <= balance:
#         balance -= minus
#         print(f"Вы сняли {minus} руб. Остаток в вашей карте {balance}")