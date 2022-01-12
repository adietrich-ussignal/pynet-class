#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "fast_cli": True
}

net_connect = ConnectHandler(**cisco3)
start_time = datetime.now()
cmds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
output = net_connect.send_config_set(cmds)
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()
end_time = datetime.now()
print("Execution time: {}".format(end_time - start_time))


ping_output = net_connect.send_command("ping google.com")
if "!!!!!" in ping_output:
    print("Ping Successful!")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing failed: {}\n\n".format(ping_output))


net_connect.disconnect()
