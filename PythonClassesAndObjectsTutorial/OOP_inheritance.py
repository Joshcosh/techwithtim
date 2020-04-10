class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep beep')


class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('Honk honk')









# class Dog(object):  # Dog inherits from the object class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("Hi I am", self.name, 'and I am ', self.age, 'years old')
#
#     def talk(self):
#         print('Bark!')
#
#
# # class Cat(object):
# #     def __init__(self, name, age, color):
# #         self.name = name
# #         self.age = age
# #         self.color = color
# #
# #     def speak(self):
# #         print("Hi I am", self.name, 'and I am ', self.age, 'years old')
#
# class Cat(Dog):  # Cat inherits from Dog
#     def __init__(self, name, age, color):
#         super().__init__(name, age)  # uses the init function from the Dog which is the super class of Cat
#         self.name = 'Tech'
#         self.color = color
#
#     # overiding super methonds
#
#     def talk(self):
#         print('Meow!')
#
# class
#
# jim = Dog('Jim', 70)
# jim.speak()
# jim.talk()
#
# tim = Cat('Tim', 5, 'blue')
# tim.speak()
# tim.talk()
