import json

with open("arp_data.json") as f: 
    arp_data = json.load(f)

arp_addresses = {}

arp_entries = arp_data["ipV4Neighbors"]

for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_addresses[ip_addr] = mac_addr

print(arp_addresses)
