# #!/usr/bin/env python
import subprocess
import time
import optparse
import random
def random_mac():
    hexa = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    mac = ""
    for i in range(5):
        y = (random.choice(hexa),2)
        y1 = str(y[0])
        y2 = str(y[1]) 
        yf = y1 + y2
        mac = mac + (f":{yf}")

    mac = mac[1:]
    return mac



def arg():
    parser = optparse.OptionParser()
    parser.add_option("-i","--inteface ",dest="interface",help="Interface to change mac adress")
    parser.add_option("-m","--mac ",dest="new_mac",help="New Mac adress for change [Optional] (Don't Have Mac Adress, Chill! I Have Random mac_adress Generator)")
    (options,arguments) = parser.parse_args()
    if not options.interface :
        parser.error("[-] Please Enter your interface to run the code, use --help for more info")
    elif not options.new_mac :
       options.new_mac = random_mac()
    return options
def mc(interface,new_mac):
    print(f"Changing Mac Adress for {interface} to {new_mac}")
    subprocess.call(f"sudo ifconfig {interface} down",shell=True)
    subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac}",shell=True)
    subprocess.call(f"sudo ifconfig {interface} up",shell=True)




options= arg()
mc(options.interface,options.new_mac)



random_mac()

