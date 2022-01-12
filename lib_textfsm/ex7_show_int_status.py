from pprint import pprint
import textfsm 

template_file = "ex2_port.tpl"

template = open(template_file)

with open("ex1_show_int_status.txt") as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

table_keys = re_table.header
final_list = []

for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    final_list.append(fsm_dict)


pprint(final_list)
print()

