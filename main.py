
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



#Вывод poket
print(Fore.YELLOW + '''
////////   //////////   //     //   ////////   //////////
//    //   //      //   //   //     //             //
//    //   //      //   // //       //             //
////////   //      //   ///         ////////       //
//         //      //   // //       //             //
//         //      //   //   //     //             //
//         //////////   //    //    ////////       // 
>--------------------------------------------->
Phammer0.1 создан в Python3.7
                            Create by Poketoff
┌─────────────────────────────────────────────┐
│   Tos:  Не используйте для ддоса дневников  │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          + Добавлен тул сканирования портов │
│          + Добавлен тул ддоса сайта/ip      │
│                                             │
│                                             │
├─────────────────────────────────────────────┤
│ Link: https://github.com/poketoff/phammer   │
└─────────────────────────────────────────────┘''')

print(Style.RESET_ALL)

#функция инициализации
def initialization():
	bar = progressbar.ProgressBar(maxval=5.0).start()
	t = 0.0
	while t <= 1.0:
		bar.update(t)
		time.sleep(0.005)
		t += 0.01
	bar.finish()


#функция инициализации хеша
def initialization_hash():
	bar = progressbar.ProgressBar(maxval=10.0).start()
	t = 0.0
	while t <= 1.0:
		bar.update(t)
		time.sleep(0.002)
		t += 0.01
	bar.finish()

#функция проверки хеша
def hash_check():
	chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	number = 1
	length = 12
	for n in range(number):
		password =''
		for i in range(length):
			password += random.choice(chars)
		print("Твой hash=> " + password)
#функция ddos





initialization()
print(Fore.GREEN + "Инициализация успешна")
print(Style.RESET_ALL)

time.sleep(2)
print("Проверка hash`а")
initialization_hash()

hash_check()

print(Fore.GREEN + "Вывожу меню")


#функция вывода меню
def show_main_menu():
	print(Style.RESET_ALL)
	print("[0]Exit")
	print("[1]DDoS-Site")
	print("[2]DDoS-ip")
	print("[3]Check Port")
	print("[4]Repair module")

show_main_menu()

choice = input(Fore.RED + "> ")
print(Style.RESET_ALL)

if choice == "0":
	exit("ТВОЙ IP УЖЕ У ФСБ :3")

elif choice == "1":
	from ddos import DoS
elif choice == "4"
