import yaml
from netmiko import ConnectHandler
from os import path
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    device_list = yaml.safe_load(f)

device = device_list["cisco4"]
net_connect = ConnectHandler(**device)

show_run = net_connect.send_command("show run")
cisco_cfg = CiscoConfParse(show_run.splitlines())

interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()

for interface in interfaces:
    print ("Interface: {}".format(interface.text))
    ip_address = interface.re_search_children(r"ip address")[0].text
    print("IP Address: {}".format(ip_address))
    print()


