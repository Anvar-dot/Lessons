# num1 = 30

# while num1 >0:
#     print(num1)
#     num1 -= 1
    
# print("Blastoff!")

# num1 = 30
# while num1 > 0 :
#     num1 -= 1
#     if num1 != 12:
#         print(num1, end='  ')
#     else:
#         # break
#         continue
    
    
# print("\nBlastoff!")

# num = 10
# while num >0:
#     num -=1
#     if num == 7:
#         print("Skipping 7")
#         continue
#     elif num == 3:
#         print("Skipping 3")
#         continue
#     print(num, end=' ')
    
# print("\nОбратный отсчет завершен!")


# start_num = int(input("Введите первое число: "))
# end_num = int(input("Введите второе число: "))
# total_num = 0

# while start_num <= end_num:
#     if start_num % 2 == 0:
#         total_num += start_num
#     start_num += 1
    
    
    
# while True:
#     for i in range(1, 10):
#         if i % 2 == 0:
#             print(i, end=' ')
#         else:
#             if i ==10:
#                 break
        
# print("\nСчет успешно завершен !")



# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1

# print("\nСчет успешно завершен!")


# i = 1
# while i <=25:
#     if i % 2 == 0:
#         print(i,end=' ')
#     i += 3
    
# print("\nСчет успешно завершен!")




password = "agent007"
get_password = input("Введите пароль: ")


while get_password != password:
    if get_password == "exit":
        print("Вы вышли из программы. ")
        break
    else:
        print("Неверный пароль. Попробуйте еще раз.")
        get_password = input("Введите пароль: ")
        
else:
    print("Добро пожаловать в систему!")