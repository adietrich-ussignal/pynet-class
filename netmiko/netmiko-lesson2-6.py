#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime
import time


device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "session_log": "my_output.txt"
}

net_connect = ConnectHandler(**device)

print(net_connect.find_prompt())

net_connect.config_mode()

print(net_connect.find_prompt())

net_connect.exit_config_mode()

print(net_connect.find_prompt())

net_connect.write_channel("disable\n")
time.sleep(2)
print(net_connect.read_channel())

net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()

