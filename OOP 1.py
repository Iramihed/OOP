# Создайте класс на тему животных. В классе должен присутствовать конструктор не менее трёх методов.
class Animal:
    def __init__(self, name, sex, gam):
        self.name = name
        self.sex = sex
        self.age = 4
        self.gam = gam

    def dog (self):
        print("Животное - " + self.name  + " , его пол - " +  self.sex )

    def dog_age (self):
        print("Возраст " + str(self.age) )

    def dog_gam (self):
        print("Оно любит играть в " + self.gam  )

Аnimal1 = Animal( " Каспер " ,  " мальчик " , "мяч" )
Аnimal1.dog()
Аnimal1.dog_age()
Аnimal1.dog_gam()
