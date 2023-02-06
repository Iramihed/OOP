from abc import abstractclassmethod
class Animal:
    def __init__(self):
        pass
    @abstractclassmethod
    def run (self):
        pass
    @abstractclassmethod
    def prigat (self):
        pass
    @abstractclassmethod
    def sound (self):
        pass
class Dog(Animal):
    def __init__(self):
        pass
    def run (self):
        print(" Собака бегает")
    def prigat (self):
        print(" Собака пригает")
    def sound (self):
        print(" Собака гавкает")
    def juds(self):
        print(" Это животное - Мухтар ")
class Cat(Animal):
    def __init__(self):
        pass
    def run(self):
        print(" Кот бегает")
    def prigat(self):
        print(" Кот прыгает")
    def sound(self):
        print(" Кот мяукает")
    def udis(self):
        print(" Это животное - Мурка ")
animal1=Dog()
animal1.run()
animal1.prigat()
animal1.sound()
animal1.juds()
cat1=Cat()
cat1.run()
cat1.prigat()
cat1.sound()
cat1.udis()