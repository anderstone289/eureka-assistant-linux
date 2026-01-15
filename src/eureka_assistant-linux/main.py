import requests
import os
import pathlib
import dotenv
import asyncio
import aiohttp
import json
import webbrowser
from importlib import resources

mode = input("Введите режим Эврики: 'AImode/StandartMode': ")

#Класс для создания объекта Стандартного мода
class StandardMode:
    def __init__(self):
        self.comand = input("Введите команду:")

    @staticmethod
    #Функция для выведения доступных команд в терминал.
    def help():
        with resources.open_text("eureka_assistant-linux", "comands.txt") as file:
            content = file.read()
            print(content)
    """Реализовать потом когда добавлю ИИ режим"""
    # def openfile(self):
    #     f = open(f'{self.comand}', 'r')
    #     return f
    def main(self):
        comand = self.comand.split()
        while True:
            if comand[0] == "открой":
                webbrowser.open(self.comand[1])
#Класс для создания объекта AI мода
class AImode:
    def __init__(self):
        pass

"""Точка входа (включение программы)"""
if __name__ == '__main__':
    if mode == "AImode":
        AImode = AImode()
    elif mode == "StandartMode":
        StandartMode = StandardMode()
        StandartMode.main()
