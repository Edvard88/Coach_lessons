# 3) Создать три класса: APIAlpha, APIDelta, APIGamma. Эти классы должны реализовывать функцию для взятия данных с API
# (пусть в нашем случае они возвращают случайные числа).
# Создать программу, которая выводит результат с одного из API.

from abc import ABCMeta, abstractmethod
from random import randint


class API(metaclass=ABCMeta):
    def __init__(self, user_api, password_api):
        print("Init AbstractClass method")
        self.user_api = user_api
        self.password_api = password_api

    @abstractmethod
    def get_count_of_users(self):
        pass


class APIAlpha_VK(API):

    def __init__(self, token_vk, user_api_vk='defult', password_api_vk='defult'):
        super().__init__(user_api=user_api_vk, password_api=password_api_vk)
        print("Init in VK API")
        self.token_vk = token_vk

    def get_count_of_users(self):
        print("Return count of users")
        return randint(1, 10)


class APIDelta_OK(API):

    def __init__(self, token_ok, user_api_ok='defult', password_api_ok='defult'):
        super().__init__(user_api=user_api_ok, password_api=password_api_ok)
        print("Init in OK API")
        self.token_ok = token_ok

    def get_count_of_users(self):
        print("Return count of users")
        return randint(1, 10)


class APIGamma_FB(API):

    def __init__(self, token_fb, user_fb='defult', password_fb='defult'):
        super().__init__(user_api=user_fb, password_api=password_fb)
        print("Init in FB API")
        self.token_fb = token_fb

    def get_count_of_users(self):
        print("Return count of users")
        return randint(1, 10)


if __name__ == '__main__':
    apialpha_vk = APIAlpha_VK(user_api_vk="user_vk", password_api_vk='password_vk', token_vk="token_vk_abcdef")
    apidelta_ok = APIDelta_OK(user_api_ok="user_ok", token_ok="token_ok_abcdef")
    apidelta_fb = APIGamma_FB(token_fb="token_fb_abcdef")

    print("Count of users VK: ", apialpha_vk.get_count_of_users())
    print("Count of users OK: ", apidelta_ok.get_count_of_users())
    print("Count of users FB: ", apidelta_fb.get_count_of_users())
