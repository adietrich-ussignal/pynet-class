from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "global_delay_factor": 2
}
start_time = datetime.now()
print(start_time)
net_connect = ConnectHandler(**device)

output = net_connect.send_command("show lldp neighbors detail")

print(output)
end_time = datetime.now()
print("\n\n Execution Time: {}".format(end_time-start_time))

start_time = datetime.now()
print(start_time)

output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)

print(output)
end_time = datetime.now()
print("\n\n Execution Time: {}".format(end_time-start_time))
