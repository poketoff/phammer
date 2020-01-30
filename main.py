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

# Вывод poket
from modules.banner import *

print(Style.RESET_ALL)

# Вызов инициализации
from modules.defs import initializationClass

# Вызов проверки хеша
from modules.defs import initialization_hashClass
from modules.defs import hash_checkClass

# Вызов меню
from modules.defs import show_main_menuClass

choice = input(Fore.RED + "[?]> ")
print(Style.RESET_ALL)

# Логика меню
if choice == "0":
    exit("ТВОЙ IP УЖЕ У ФСБ :3")

elif choice == "1":
    from modules.ddos import DoS
elif choice == "2":
    from modules.scan import *
elif choice == "3":
    from modules.repair import repair_module
elif choice == "4":
    from modules.mac import *
