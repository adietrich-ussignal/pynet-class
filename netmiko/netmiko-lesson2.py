#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass()
}

net_connect = ConnectHandler(**cisco4)

output = net_connect.send_command("ping", expect_string=r'ip')
output += net_connect.send_command("\n", expect_string=r'address')
output += net_connect.send_command("8.8.8.8\n", expect_string=r'5')
output += net_connect.send_command("\n", expect_string=r'100')
output += net_connect.send_command("\n", expect_string=r'2')
output += net_connect.send_command("\n", expect_string=r'n')
output += net_connect.send_command("\n", expect_string=r'n')
output += net_connect.send_command("\n", expect_string=r'!')

print(output)
