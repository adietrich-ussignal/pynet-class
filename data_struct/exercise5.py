import yaml
from netmiko import ConnectHandler
from os import path
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    device_list = yaml.safe_load(f)

device = device_list["cisco4"]


