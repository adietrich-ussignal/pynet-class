import pyeapi
from pprint import pprint
from getpass import getpass
import yaml
from my_funcs import function1, function2, print_route

def main():
    
    devices = function1()
    password = getpass()

    for name, device_dict in devices.items(): 
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        show_route = device.enable('show ip route')

        print ()
        
        route_list = show_route[0]['result']['vrfs']['default']['routes']

        print_route(route_list)

        print()

if __name__ == "__main__":
    main()
