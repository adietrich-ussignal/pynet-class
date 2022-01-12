#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'port': '22'
}


nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
    'port': '22',
    'session_log': 'nxos2_session.txt'
}

device_list = [nxos1, nxos2]



for device in device_list:
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    if device == nxos2:
        net_connect.send_command('show version')
    net_connect.disconnect()

    
