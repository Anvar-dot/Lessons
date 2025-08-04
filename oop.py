from abc import ABC , abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass
     
    
class Car(Transport):
    def move(self):
        print("Машина едет по дороге.")
        
class Bike(Transport):
    def move(self):
        print("Велосипед едет по тропинке.")
        
        
car = Car()
bike = Bike()

car.move()
bike.move()