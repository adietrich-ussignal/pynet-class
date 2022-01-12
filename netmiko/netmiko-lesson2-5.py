#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

password = getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "fast_cli": True
}

def display_output(output):
    
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()


for device in (nxos1, nxos2):

    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("vlans.txt")
    display_output(output)
    net_connect.save_config()
    net_connect.disconnect()


