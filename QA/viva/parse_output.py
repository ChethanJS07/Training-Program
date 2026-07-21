import re

output = """
Connecting to R1... 
Connection Successful 
 
Connecting to R2... 
Authentication Failed 
 
Connecting to R3... 
Timed Out 
 
Connecting to R4... 
Connection Successful
"""

pattern = re.compile(r"Connecting to (R\d+)")
devices = pattern.findall(output)

pattern_status = re.compile(r"(Connection Successful|Authentication Failed|Timed Out)")
statuses = pattern_status.findall(output)

result = {"success": set(), "authentication_error": set(), "timed_out": set()}

for device, status in zip(devices, statuses):
    if status == "Connection Successful":
        result["success"].add(device)
    elif status == "Authentication Failed":
        result["authentication_error"].add(device)
    else:
        result["timed_out"].add(device)

print(result)
