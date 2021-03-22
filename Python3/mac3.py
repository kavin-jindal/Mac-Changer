import subprocess
import os
import time
import platform
from colorama import *
print(Fore.CYAN + "Mac Changer")
print(Fore.CYAN + "Mac Changer for Python3")
print(Fore.GREEN + '=================================')
print(Fore.YELLOW + f'User System : {platform.system()}')
print(Fore.YELLOW + f'OS Release  : {platform.release()}')
print(Fore.YELLOW + f'Machine : {platform.machine()}')
print(Fore.YELLOW + f'Python Version : {platform.python_version()}')
print(Fore.GREEN + '=================================')
input("Press to continue >> ")


def mac():
    try:
        subprocess.call(['ifconfig'])
        int_name = input("Enter interface name:")
        add_name = input('Enter new Address : ')
        subprocess.call(['ifconfig ' + int_name + ' down'], shell=True)
        subprocess.call(['ifconfig ' + int_name + ' hw ' + 'ether ' +  add_name], shell=True)
        subprocess.call(['ifconfig ' +  int_name +  ' up'], shell=True)
        #subprocess.call(['ifconfig ' +  int_name +  ' ether'], shell=True)
        print(Fore.GREEN + "Your mac address was changed successfully!!!!!")
        time.sleep(2)
        print(Fore.GREEN + 'Your new mac address' + add_name)
        subprocess.call(['ifconfig'])

    except:
        time.sleep(3)
        print(Fore.RED + '===================================')
        print(Fore.RED + 'An error occurred, make sure your interface name or new mac address was correct, try running the script again..')


mac()
