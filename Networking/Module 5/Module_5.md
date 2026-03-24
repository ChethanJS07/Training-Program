# Network Training Program - Module 5 (Layer 3)

### Output Drive link - [Google Drive](https://drive.google.com/drive/folders/1xBKeRVyEhNCJzfyFXOgQ2QRq96xuRf28?usp=sharing)

---

### Question 1: Capture and Analyze ARP Packets

- #### Capture ARP request and reply packets using Wireshark and analyze the sender's IP and MAC address fields.

During an ARP request, the sender includes its own IP address and MAC address so that the intended target can respond directly to them. It broadcasts this message
to all the devices in the local network because it doesn't know which device has which IP. When the target responds to the sender with its own MAC address, the reply from the
target is only to the sender, not broadcasted, the sender updates the ARP table with IP:MAC address entry, and in the future it will just lookup that ARP table to forward packets in the local network.

---

### Question 4: Use Wireshark to Capture DHCP Discover, Offer, Request, and Acknowledge Messages and Explain the Process

- DHCP (Dynamic Host Configuration Protocol) is used to dynamically assign IP address to local network devices so that they can communicate with devices outside the local network.
- There are 4 steps:
  - Discover: The new device broadcasts itself to DHCP servers
  - Offer: The DHCP server assigns a new existing IP address
  - Request: The device requests the new IP address
  - ACK: Server confirms and provides configuration

---

### Question 5: Subnetting 192.168.1.0/24 into 4 Subnets

- Given Network address: 192.168.10/24
  - Subnet Mask: /24 => Subnet: 255.255.255.0

- No of bits to borrow => 2^n >= 4 => n=2
  - New Subnet mask => /24 + 2 = /26
  - New Subnet = 255.255.255.192

- Block Size = 256-192 = 64 (each subnet has 64 IP's and 62 usable IP's)

| Subnet | Network Address | First Usable  | Last Usable   | Broadcast Address |
| ------ | --------------- | ------------- | ------------- | ----------------- |
| 1      | 192.168.1.0     | 192.168.1.1   | 192.168.1.62  | 192.168.1.63      |
| 2      | 192.168.1.64    | 192.168.1.65  | 192.168.1.126 | 192.168.1.127     |
| 3      | 192.168.1.128   | 192.168.1.129 | 192.168.1.190 | 192.168.1.191     |
| 4      | 192.168.1.192   | 192.168.1.193 | 192.168.1.254 | 192.168.1.255     |

---

### Question 6: IP Address Classification

Given IP Addresses:

| IP Address  | Class | Default Subnet Mask | Private/Public | Class Range |
| ----------- | ----- | ------------------- | -------------- | ----------- |
| 10.1.1.1    | A     | 255.0.0.0           | Private        | 1-126       |
| 172.16.5.10 | B     | 255.255.0.0         | Private        | 128-191     |
| 192.168.1.5 | C     | 255.255.255.0       | Private        | 192-223     |

---
