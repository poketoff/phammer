from modules.banners import *
from colorama import Fore, Back, Style
import random
import time
import progressbar

city_list = [banFirst, banSecond, banThird]
print(random.choice(city_list))

print(Fore.GREEN + 'Инициализация')
time.sleep(3)
bar = progressbar.ProgressBar().start() # Создаём новый progress bar
 
for t in range(101):
    bar.update(t) # Таким образом можно устанавливать значение.
    time.sleep(0.01)

bar.finish() # Заканчиваем обновлять -- далее можно

def showMenu(): # Отрисовка главного меню
    print(Fore.BLUE + "=======================================")
    print(Fore.WHITE + "       [1]DDoS")
    print(Fore.WHITE + "       [2]Check Port")
    print(Fore.WHITE + "       [3]Mac Changer")
    print(Fore.WHITE + "       [00]exit")
    print(Fore.BLUE + "=======================================")
showMenu()

choise = input('[?] ')

if choise == '1':
    from modules.ddos import ddos

elif choise == '2':
    from modules.check import *

elif choise == '3':
    pass

else:
    print(Style.RESET_ALL)
    print(Back.RED + '\nunsapported function')
    print(Style.RESET_ALL)
    showMenu()

