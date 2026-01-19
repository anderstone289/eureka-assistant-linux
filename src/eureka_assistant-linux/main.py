import requests
import os
import pathlib
import dotenv
import asyncio
import aiohttp
import json
from openai import OpenAI
import time
from datetime import datetime
import webbrowser
from importlib import resources
from dotenv import load_dotenv, find_dotenv, set_key

#Загружаем файл ".env"
load_dotenv()

#Достаем переменную счетчик для проверки выводилась ли функция help() уже или нет.
dotenv_path = find_dotenv()

if os.getenv("HELP_CALL_COUNT") is None:
    set_key(dotenv_path, "HELP_CALL_COUNT", "0")

#Время сейчас
now = datetime.now()

#Инициилизация API ключа.
API_KEY = os.getenv("API_KEY")

mode = input("Введите режим Эврики: 'AImode/StandartMode': ")

#Класс для создания объекта Стандартного мода
class StandartMode:
    def __init__(self):
        self.comand = input("Введите команду или 'помощь' для вывода доступных команд:")

    @staticmethod
    #Функция для выведения доступных команд в терминал.
    def comands():
        with resources.open_text("eureka_assistant-linux", "comands.txt") as file:
            content = file.read()
            print(content)
    def hello(self):
        print("Здравствуйте сэр, я эврика ваш виртуальный ассистент.")
        name = input("Введите ваше имя Подсказка:если вы нажмете 'enter' и ввод будет пустым я буду называть вас 'Cэр':")
    """Основной цикл"""
    def main(self):
        comand = self.comand.split()
        while True:
            comand = input("Введите команду или 'помощь' для вывода доступных команд:").split()
            if not comand:
                continue
            elif comand[0] == "открой":
                webbrowser.open(self.comand[1])
                continue
            elif comand[0] == "помощь":
                StandartMode.comands()
                continue
            elif comand[0] == "время":
                local_time = time.localtime()
                print(time.strftime("%H:%M:%S", local_time))
                continue
            elif comand[0] == "дата":
                print(now.strftime("%d.%m.%Y %H:%M"))
                continue
                """Реализовать потом."""
            # elif comand[0] == "режим":
            #     mode = input("Введите режим Эврики: 'AImode/StandartMode': ")
            #     continue
            else:
                print("Команда не распознана, сэр.")

#Класс для создания объекта AI мода
class AImode:
    def __init__(self):
        self.api_key = API_KEY
    def DeepseekModel(self):
        pass

"""Точка входа (включение программы)"""
if __name__ == '__main__':
    while mode not in ['StandartMode','AImode']:
        mode = input("Введите режим Эврики: 'AImode/StandartMode': ")
    if mode == "AImode":
        ai_mode = AImode()
        ai_mode.DeepseekModel()
    elif mode == "StandartMode":
        standart_mode = StandartMode()
        help_call_count = int(os.environ.get("HELP_CALL_COUNT", 0))
        if help_call_count == 0:
            standart_mode.hello()
            help_call_count = set_key(dotenv_path, "HELP_CALL_COUNT","1")
            standart_mode.main()
        elif help_call_count == 1:
            standart_mode.main()

