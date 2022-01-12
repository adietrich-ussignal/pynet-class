import pyeapi
from pprint import pprint
from getpass import getpass
import yaml
from my_funcs import function1, function2, print_route
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def main():
    
    devices = function1("arista_ex4.yml")
    password = getpass()

 
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template_file = "ex4.j2"

    my_devices = devices["my_devices"]

    eapi_devices = []

    for device_name in my_devices: 
        device_dict = devices[device_name]
        
        device_dict["password"] = password
        
        j2_vars = device_dict.pop("data")
        template = env.get_template(template_file)
        cfg_lines = template.render(**j2_vars)
        cfg_lines = cfg_lines.strip()
        cfg_lines = cfg_lines.splitlines()


        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        eapi_devices.append(device)
        output = device.config(cfg_lines)
        print(output)
        print()
    
    for device in eapi_devices:

        output = device.enable("show ip interface brief")
        print()
        print(output[0]['result']['output'].rstrip())
        print()



if __name__ == "__main__":
    main()
