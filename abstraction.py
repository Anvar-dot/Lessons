# from abc import ABC , abstractmethod
















from abc import ABC, abstractmethod

# Абстрактный класс. В нем есть и реализация, и абстрактный метод.
class Worker(ABC):
    def __init__(self, name, money):
        # Приватные атрибуты, защищенные инкапсуляцией
        self.__name = name
        self.__money = money
        
    def get_name(self):
        # Публичный метод для получения приватного имени
        return self.__name
    
    def get_money(self):
        # Публичный метод для получения приватной зарплаты
        return self.__money
    
    @abstractmethod
    def premy(self):
        # Это абстрактный метод. Он не имеет тела и должен быть реализован в потомках.
        pass

class Programmer(Worker):
    def premy(self):
        # Реализация абстрактного метода. Зарплата берется через get_money().
        premy_amount = self.get_money() * 0.10
        print(f"Премия программиста {self.get_name()} составляет {premy_amount} рублей.")
        return premy_amount
        
class Manager(Worker):
    def premy(self):
        # Реализация абстрактного метода. Зарплата берется через get_money().
        premy_amount = self.get_money() * 0.15
        print(f"Премия менеджера {self.get_name()} составляет {premy_amount} рублей.")
        return premy_amount
        
# Создавать объекты можно только из конкретных классов.
prog = Programmer('Алексей', 60000)
manager = Manager('Мария', 70000)

print(f"Имя: {prog.get_name()}, Зарплата: {prog.get_money()}")
prog.premy()

print("-" * 20)

print(f"Имя: {manager.get_name()}, Зарплата: {manager.get_money()}")
manager.premy()





# class Worker(ABC):
#     def __init__(self, name, money):
#         self.__name = name
#         self.__money = money
        
#     def get_name(self):
#         return self.__name
    
#     def get_money(self):
#         return self.__money
    
#     @abstractmethod
#     def premy(self):
#         pass

# class Programmer(Worker):
#     def give_premy(self,premy):
#         if premy > 0:
#             premy_percent = money/10
#             money += premy_percent
#             print(f"У программиста {self.get_name()} с учетом премии вышло {self.get_money() + premy_percent} рублей.")
#         # print(f"Программист {self.get_name()} получил премию в размере {premy} рублей.")
        
        
# class Manager(Worker):
#     def give_premy(self, premy):
#         if premy > 0:
#             premy_percent = self.get_money() * 0.15
#             self.__money += premy_percent
#             print(f"У менеджера {self.get_name()} с учетом премии вышло {self.get_money() + premy_percent} рублей.")
#         # print(f"Менеджер {self.get_name()} получил премию в размере {premy} рублей.")
        
        
# prog = Programmer('Алексей', 60000)
# manager = Manager('Мария', 70000)

      







# # class BankList(ABC):
# #     def __init__(self):
# #         self.__balance = 0.0

# #     def add_balance(self, summa):
# #         if summa > 0:
# #             self.__balance += summa
# #             print(f"Сумма пополнен на {summa} текущий баланс {self.__balance}")
# #         else:
# #             print("Сумма пополнения должна быть больше нуля.")
            
            
# #     def get_balance(self, summa):
# #         if summa > 0 and summa <= self.__balance:
# #             self.__balance -= summa
# #             print(f"Сумма снята {summa} текущий баланс {self.__balance}")
# #         else:
# #             print("Недостаточно средств на счете или сумма снятия должна быть больше нуля.")
            
# #     def see_balance(self):
# #         return self.__balance
    
# # mylist = BankList()
# # mylist.add_balance(10000)
# # mylist.get_balance(500)
# # print(mylist.see_balance())

# # now_balance = mylist.see_balance()
# # print(f"Текущий баланс: {now_balance}")




# # class Authentification(ABC):
# #     @abstractmethod
# #     def login(self):
# #         pass
    
# # class Login_Password(Authentification):
# #     def login(self):
# #         print("Вход с помощью логина и пароля.")

# # class Instagram(Authentification):
# #     def login(self):
# #         print("Вход через Instagram.")
        
# # class Facebook(Authentification):
# #     def login(self):
# #         print("Вход через Facebook.")
        
        
# # login = Login_Password()
# # instagram = Instagram()
# # facebook = Facebook()

# # login.login()
# # instagram.login()
# # facebook.login()


# # class Payment_System(ABC):
# #     @abstractmethod
# #     def pay(self, amount):
# #         pass
    
# # class Bank_Card(Payment_System):
# #     def pay(self, amount):
# #         print(f"Оплата на сумму {amount} рублей с помощью банковской карты")
        
# # class E_Wallet(Payment_System):
# #     def pay(self, amount):
# #         print(f"Оплата на сумму {amount} рублей через электронный кошелек.")
        
# # class Cash(Payment_System):
# #     def pay(self, amount):
# #         print(f"Оплата на сумму {amount} рублей наличными.")
        
        
# # bank = Bank_Card()
# # wallet = E_Wallet()
# # cash = Cash()

# # bank.pay(1000)
# # wallet.pay(500)
# # cash.pay(200)





# # class Transport(ABC):
# #     @abstractmethod
# #     def move(self):
# #         pass
    
# # class Car(Transport):
# #     def move(self):
# #         print("Машина едет по дороге.")
        
# # class Bike(Transport):
# #     def move(self):
# #         print("Велосипед едет по тропинке.")
        
        
# # class Ship(Transport):
# #     def move(self):
# #         print("Корабль плывет по морю.")
        
        
# # car = Car()
# # bike = Bike()
# # ship = Ship()

# # car.move()
# # bike.move()
# # ship.move()