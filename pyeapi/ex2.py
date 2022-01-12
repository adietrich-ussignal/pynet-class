import pyeapi
from pprint import pprint
from getpass import getpass
import yaml
from my_funcs import function1, function2

def main():
    
    devices = function1()
    password = getpass()

    for name, device_dict in devices.items(): 
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        show_arp = device.enable('show ip arp')

        print ()

        arp_list = show_arp[0]['result']['ipV4Neighbors']

        function2(arp_list)

        print()

if __name__ == "__main__":
    main()
