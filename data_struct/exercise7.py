import yaml
from os import path
from ciscoconfparse import CiscoConfParse

filename = "bgp.txt"



cisco_cfg = CiscoConfParse(filename)

peer_ips = []

neighbors = cisco_cfg.find_objects_w_parents(parentspec=r"router bgp", childspec=r"neighbor")
for neighbor in neighbors:
    _, neighbor_ip = neighbor.text.split()
    for remote_as in neighbor.children:
        if "remote-as" in remote_as.text:
            remote_as_num = remote_as.text
    peer_ips.append((neighbor_ip, remote_as_num))
print(peer_ips)


print()



