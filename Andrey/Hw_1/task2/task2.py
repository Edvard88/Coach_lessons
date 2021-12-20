# Create a Singleton (don't use new() )
# Реализовать паттерн Singleton(не используя new())

#Articles
# https://webdevblog.ru/realizaciya-shablona-singleton-v-python/

# Method1 Decorator
def singleton1(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton1
class MyClass1:

    def return_random(self):
        print("Return random")
        return 1


# Плюсы
#
# Декораторы являются аддитивными в том смысле, который часто более интуитивен, чем множественное наследование.
# Минусы
#
# В то время как объекты, созданные с использованием MyClass(), будут истинными объектами singleton,
# MyClass сам по себе является функцией, а не классом, поэтому вы не можете вызывать методы класса из него.
# Также для


#Method2
class Singleton2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass2(Singleton2):
    def return_random(self):
        print("Return random")
        return 1

# Плюсы
# Это настоящий класс
# Минусы
# Множественное наследование - тьфу! __new__ может быть перезаписан во время наследования от второго базового класса?
# Нужно думать больше, чем необходимо.



# Method3
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# class MyClass(BaseClass, metaclass=Singleton):
#     pass


# Method2
# class Singleton2(object):
#     _instance = None
#
#     def __new__(class_, *args, **kwargs):
#         if not isinstance(class_._instance, class_):
#             class_._instance = object.__new__(class_, *args, **kwargs)
#         return class_._instance





#
#
# @my_singleton
# class MyClass1:
#     pass


if __name__ == '__main__':
    a = MyClass1()
    b = MyClass1()
    print("Method1 return: ", a is b)

    a = MyClass2()
    b = MyClass2()
    print("Method2 return: ", a is b)


    print(a.return_random())