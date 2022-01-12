import yaml
from pprint import pprint

arista1 = {"device_name": "arista1", "hostname": "arista1.lasthop.io"}


arista2 = {"device_name": "arista2", "hostname": "arista2.lasthop.io"}


arista3 = {"device_name": "arista3", "hostname": "arista3.lasthop.io"}

arista4 = {"device_name": "arista4", "hostname": "arista4.lasthop.io"}

devices = [arista1, arista2, arista3, arista4]

for device in devices:
    device['username'] = "root"
    device['password'] = "root"

with open("devices.yml", "w") as f:
    yaml.dump(devices, f, default_flow_style=False)



pprint(devices)
