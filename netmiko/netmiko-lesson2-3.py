#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass()
}

net_connect = ConnectHandler(**cisco4)
cmds = ["show version", "show lldp neighbors"]
for cmd in cmds:
    output = net_connect.send_command(cmd, use_textfsm=True)
    print("#" * 80)
    print(cmd)
    print("#" * 80)
    pprint(output)
    print("#" * 80)
    print()
    if cmd == "show lldp neighbors":
        print("LLDP Data Structure Type: {}".format(type(output)))
        print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

net_connect.disconnect()
