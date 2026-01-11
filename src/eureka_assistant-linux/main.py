import requests
import os
import pathlib
import dotenv

#Класс для создания объекта Стандартного мода
class StandardMode:
    def __init__(self):
        self.comand = input("Введите команду:")

    @staticmethod
    def help():
        print("""
            Method 'help' may be 'static'
        """)
#Класс для создания объекта AI мода
class AImode:
    def __init__(self):
        pass

"""Точка входа (включение программы)"""
if __name__ == '__main__':
    Standartmode = StandardMode()
