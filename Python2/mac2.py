import subprocess
import os
import time
os.system('clear')
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script."
    "\nPlease try again, this time using 'su -', and entering your root password"
    '\nExiting the Program')
print("Mac Changer")
subprocess.call('ifconfig')
print("Mac Changer for Python2")

def mac():
    try:
        int_name = raw_input("Enter interface name:")
        add_name = raw_input('Enter new Address : ')
        subprocess.call(['ifconfig ' + int_name + ' down'], shell=True)
        subprocess.call(['ifconfig ' + int_name + ' hw ' + 'ether ' +  add_name], shell=True)
        subprocess.call(['ifconfig ' +  int_name +  ' up'], shell=True)
        #subprocess.call(['ifconfig ' +  int_name +  ' ether'], shell=True)
        print("Your mac address was changed successfully!!!!!")
        time.sleep(2)
        print('Your new mac address' + add_name)
        subprocess.call(['ifconfig'])

    except:
        time.sleep(3)
        print('===================================')
        print('An error occurred, make sure your interface name or new mac address was correct, try running the script again..')


mac()
