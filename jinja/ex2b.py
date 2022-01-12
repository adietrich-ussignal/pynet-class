from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment 

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


int_vars = {
    'intf': 'Ethernet1/1',
    'ip_address': ['10.1.100.1', '10.1.100.2'],
    'netmask': '24',
    'local_as': '22',
    'peer_ip': ['10.1.100.2', '10.1.100.1']
}

template_file = "ex2b.j2"
template = env.get_template(template_file)
output = template.render(**int_vars)

print(output)
