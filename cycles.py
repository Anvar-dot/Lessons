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


start_num = int(input("Введите первое число: "))
end_num = int(input("Введите второе число: "))
total_num = 0

while start_num <= end_num:
    if start_num % 2 == 0:
        total_num += start_num
    start_num += 1
    
