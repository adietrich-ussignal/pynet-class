import pyeapi
from pprint import pprint
from getpass import getpass

node = pyeapi.connect(host = 'arista3.lasthop.io', username='pyclass', password=getpass(), transport='https')
device = pyeapi.client.Node(node)
show_arp = device.enable('show ip arp')


arp_list = show_arp[0]['result']['ipV4Neighbors']

for arp_entry in arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    print('{}  -->  {}'.format(mac_address, ip_address))
