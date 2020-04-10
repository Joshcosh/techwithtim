class Dog(object):  # Dog inherits from the object class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 3, 4]

    def speak(self):
        print("Hi I am", self.name, 'and I am ', self.age, 'years old')

    def change_age(self, age):
        self.age = age;

    def add_weight(self, weight):
        self.weight = weight


tim = Dog('Tim', 32)  # tim is an instance of type Dog
fred = Dog('Fred', 5)  # fred is an instance of type Dog

tim.speak()
fred.speak()

tim.change_age(92)
tim.speak()

print(tim.age)
print(tim.li)
print(fred.li)

tim.add_weight(12)
print(tim.weight)