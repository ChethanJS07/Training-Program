show_ip_interface_brief = """
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet1           192.168.1.1     YES NVRAM  up                    up      
GigabitEthernet2           unassigned      YES NVRAM  administratively down down    
Loopback0                  10.255.255.1    YES NVRAM  up                    up      
"""

lines = show_ip_interface_brief.strip().splitlines()
header = lines[0].split()
dictionary = {}

for line in lines[1:]:
    if not line.strip():
        continue

    parts = line.split()

    if len(parts) == len(header):
        values = parts

    elif len(parts) > len(header):
        values = parts[:4] + [" ".join(parts[4:-1])] + [parts[-1]]
    else:
        continue

    dictionary[values[0]] = dict(zip(header[1:], values[1:]))

print(dictionary)
