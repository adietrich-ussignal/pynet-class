import yaml



def function1(filename="arista.yml"):

    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading the YAML file failed")

def function2(arp_list):
    for arp_entry in arp_list:
        mac_address = arp_entry['hwAddress']
        ip_address = arp_entry['address']
        print ()

        print('{}  -->> {}'.format(mac_address, ip_address))

        print ()

def print_route(route_list):

    for prefix, route_dict in route_list.items():
        route_type = route_dict["routeType"]
        print()
        print(prefix)
        print(route_type)
        print(route_dict["vias"][0]["interface"])
        if route_type == "static":
            print(route_dict["vias"][0]["nexthopAddr"])
        print() 
