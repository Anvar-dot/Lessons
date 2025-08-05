from abc import ABC , abstractmethod

class BankList(ABC):
    def __init__(self):
        self.__balance = 0.0

    def add_balance(self, summa):
        if summa > 0:
            self.__balance += summa
            print(f"Сумма пополнен на {summa} текущий баланс {self.__balance}")
        else:
            print("Сумма пополнения должна быть больше нуля.")
            
            
    def get_balance(self, summa):
        if summa > 0 and summa <= self.__balance:
            self.__balance -= summa
            print(f"Сумма снята {summa} текущий баланс {self.__balance}")
        else:
            print("Недостаточно средств на счете или сумма снятия должна быть больше нуля.")
            
    def see_balance(self):
        return self.__balance
    
mylist = BankList()
mylist.add_balance(10000)
mylist.get_balance(500)
print(mylist.see_balance())

now_balance = mylist.see_balance()
print(f"Текущий баланс: {now_balance}")












# class Authentification(ABC):
#     @abstractmethod
#     def login(self):
#         pass
    
# class Login_Password(Authentification):
#     def login(self):
#         print("Вход с помощью логина и пароля.")

# class Instagram(Authentification):
#     def login(self):
#         print("Вход через Instagram.")
        
# class Facebook(Authentification):
#     def login(self):
#         print("Вход через Facebook.")
        
        
# login = Login_Password()
# instagram = Instagram()
# facebook = Facebook()

# login.login()
# instagram.login()
# facebook.login()


# class Payment_System(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
    
# class Bank_Card(Payment_System):
#     def pay(self, amount):
#         print(f"Оплата на сумму {amount} рублей с помощью банковской карты")
        
# class E_Wallet(Payment_System):
#     def pay(self, amount):
#         print(f"Оплата на сумму {amount} рублей через электронный кошелек.")
        
# class Cash(Payment_System):
#     def pay(self, amount):
#         print(f"Оплата на сумму {amount} рублей наличными.")
        
        
# bank = Bank_Card()
# wallet = E_Wallet()
# cash = Cash()

# bank.pay(1000)
# wallet.pay(500)
# cash.pay(200)











# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
    
# class Car(Transport):
#     def move(self):
#         print("Машина едет по дороге.")
        
# class Bike(Transport):
#     def move(self):
#         print("Велосипед едет по тропинке.")
        
        
# class Ship(Transport):
#     def move(self):
#         print("Корабль плывет по морю.")
        
        
# car = Car()
# bike = Bike()
# ship = Ship()

# car.move()
# bike.move()
# ship.move()