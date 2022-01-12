from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment 
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2
import time
import re


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


nxos1_conf = {
    'intf': 'Ethernet1/1',
    'ip_address': '10.1.100.1',
    'netmask': '24',
    'local_as': '22',
}

nxos2_conf = {
    'intf': 'Ethernet1/1',
    'ip_address': '10.1.100.2',
    'netmask': '24',
    'local_as': '22',
}

nxos1_conf["peer_ip"] = nxos2_conf["ip_address"]
nxos2_conf["peer_ip"] = nxos1_conf["ip_address"]

template_file = "ex2b.j2"

nxos1["j2_vars"] = nxos1_conf
nxos2["j2_vars"] = nxos2_conf

for device in (nxos1, nxos2):
    tmp_device = device.copy()
    j2_vars = tmp_device.pop("j2_vars")
    template = env.get_template(template_file)
    cfg = template.render(**j2_vars)
    
    print(cfg)
    
    cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]

    print(tmp_device)
    net_connect = ConnectHandler(**tmp_device)
    device["ssh_conn"] = net_connect
    output = net_connect.send_config_set(cfg_lines)
    print(output)

sleep_time = 15
print(f"Sleeping for {sleep_time} seconds...")
time.sleep(sleep_time)

print("Testing BGP and Ping")
for device in (nxos1, nxos2):
    net_connect = device["ssh_conn"]
    remote_ip = device["j2_vars"]["peer_ip"]
    output = net_connect.send_command(f"ping {remote_ip}")
    print(output)
    if "64 bytes" not in output:
        print("\nPing Failed!!!")
    print("\n\n")
    bgp_verify = f"show ip bgp summary | include {remote_ip}"
    output = net_connect.send_command(bgp_verify)
    match = re.search(r"\s+(\S+)\s*$", output)
    prefix_received = match.group(1)
    try:
        int(prefix_received)
        print(
            f"BGP reached an established state"
        )
    except ValueError:
        print("BGP Failed to reach an established state")    
