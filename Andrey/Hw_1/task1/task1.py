# Create abstract class Animal
# create methods sound() sound(), move(), die(), breed() and
# attributes name, legs, wings, tails, teeth, color.

# Сделать абстрактный класс Animal.
# В нем будут функции sound(), move(), die(), breed() и
# переменные name, legs, wings, tails, teeth, color.


from abc import ABCMeta, abstractmethod, abstractproperty


class Animal(metaclass=ABCMeta):

    def __init__(self, name, legs, wings, tails, teeth, color):
        self.name = name
        self.legs = legs
        self.wings = wings
        self.tails = tails
        self.teeth = teeth
        self.color = color

    def die(self):
        print("Every alive being die the same. We don't need abstract method")

    # @property
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def breed(self):
        pass


class Lion(Animal):

    @property
    def sound(self):
        print("Lion sound")
        return self.name + "_property"

    def move(self):
        print("Lion move")

    def die(self):
        print("Lion die")

    def breed(self):
        print("Lion breed")


if __name__ == '__main__':
    print("Hello")

    lion = Lion(name="Leo", legs=4, wings = 0, tails=1, teeth=32, color='yellow')

    print(lion.name)
    print(lion.sound)
    print(lion.wings)
