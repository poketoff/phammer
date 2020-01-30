from colorama import Fore, Back, Style
from datetime import datetime
from threading import Thread
import time
import sys
import os
import socket
import random
import threading
import progressbar

#Класс инициализации
class initializationClass():
	bar = progressbar.ProgressBar(maxval=5.0).start()
	t = 0.0
	while t <= 1.0:
		bar.update(t)
		time.sleep(0.005)
		t += 0.01
		bar.finish()
	print(Fore.GREEN + "Инициализация успешна")
	print(Style.RESET_ALL)

#Класс инициализации хеша
class initialization_hashClass():
	print("Проверка hash`а")
	bar = progressbar.ProgressBar(maxval=10.0).start()
	t = 0.0
	while t <= 1.0:
		bar.update(t)
		time.sleep(0.002)
		t += 0.01
	bar.finish()

#функция проверки хеша
class hash_checkClass():
	chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	number = 1
	length = 12
	for n in range(number):
		password =''
		for i in range(length):
			password += random.choice(chars)
		print("Твой hash=> " + password)
		time.sleep(3)

#функция вывода меню
class show_main_menuClass():
	print(Fore.GREEN + "Вывожу меню")
	print(Style.RESET_ALL)
	print("[0]Exit")
	print("[1]DDoS")
	print("[2]Check Port")
	print("[3]Repair module")