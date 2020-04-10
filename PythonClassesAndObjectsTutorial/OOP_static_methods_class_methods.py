class Dog:
    dogs = []  # usually at the top of the class, can be called with the class name, doesn't require an instance of
    # the class
    xc = 5  # just another example global variable

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod  # can be called on the name of the class, will work the same if called on an instance
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod  # good for interfaces more than for classes, if thought of as C++
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("Bark!")


Dog.bark(5)


class Math:
    @staticmethod
    def add(x, x2):
        return x + x2



# print(Dog.num_dogs())
# tim = Dog("Tim")
# print(Dog.num_dogs())
# jim = Dog("Jim")
#
# print(Dog.dogs)
# print(Dog.num_dogs())