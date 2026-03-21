# Assignment Questions for Layer - 3 (Module 6)

---

### Question 1:

### Capture and analyze ARP packets using Wireshark. Inspect the ARP request and reply frames when your device attempts to find the router's MAC address. Discuss the importance of ARP in packet forwarding.

## ARP (Address Resolution Protocol) maps an IP address to a MAC address. When a device knows the IP but needs the MAC to send data on the local network, it sends an ARP request.

---

### We have a network address 10.0.0.0/24 and need to divide it into 4 equal subnets.

The original mask is /24 (255.255.255.0). To get 4 subnets, we borrow 2 bits from the host portion.
2 bits → 2^2 = 4 subnets.

New prefix length = /24 + 2 = /26
Subnet mask = 255.255.255.192

Subnet block size = 256 - 192 = 64 addresses per subnet (including network and broadcast).

| Subnet |    Network    | First Usable | Last Usable | Broadcast  |
| :----: | :-----------: | :----------: | :---------: | :--------: |
|   1    |  10.0.0.0/26  |   10.0.0.1   |  10.0.0.62  | 10.0.0.63  |
|   2    | 10.0.0.64/26  |  10.0.0.65   | 10.0.0.126  | 10.0.0.127 |
|   3    | 10.0.0.128/26 |  10.0.0.129  | 10.0.0.190  | 10.0.0.191 |
|   4    | 10.0.0.192/26 |  10.0.0.193  | 10.0.0.254  | 10.0.0.255 |

---

### Question 4

### You are given three IP addresses: 192.168.10.5, 172.20.15.1, and 8.8.8.8.

- Identify the class of each IP address.
  - 192.168.10.5 → Class C
  - 172.20.15.1 → Class B
  - 8.8.8.8 → Class A

- Determine if it is private or public.
  - 192.168.10.5 → Private
  - 172.20.15.1 → Private
  - 8.8.8.8 → Public

- Explain how NAT would handle a private IP when accessing the internet.
  - NAT translates private IP to public IP.
  - It uses port numbers to distinguish between multiple internal hosts.
  - It enables private networks to access the internet while maintaining security

---
