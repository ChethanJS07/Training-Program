# Network Training Program - Module 3&4

### Output Drive link - [Google Drive](https://drive.google.com/drive/folders/1xBKeRVyEhNCJzfyFXOgQ2QRq96xuRf28?usp=sharing)

---

### Question 5: Research the Linux kernel's handling of Ethernet devices and network interfaces. Write a short report on how the Linux kernel supports Ethernet communication (referencing kernel.org documentation).

### Report:

## Linux Kernel's Handling of Ethernet Devices

- #### Introduction:

The Linux Kenel handles Ethernet Communication through a Layered Architecture. Data passes through multiple kernel Subsystems before reaching the application.

|     Linux Ethernet Communication     |
| :----------------------------------: |
|           User Application           |
|                  ↓↑                  |
| Socket Layer (sys calls: send, recv) |
|                  ↓↑                  |
|     Protocol Stack (TCP/IP, ARP)     |
|                  ↓↑                  |
|       Network Device Subsystem       |
|                  ↓↑                  |
|  Device Driver (e.g. e1000, r8169)   |
|                  ↓↑                  |
|        Physical NIC Hardware         |

- #### Network Device Drivers:

Every Ethernet NIC needs a kernel driver to function. The driver:

-> Registers the device with the kernel using `register_netdev()`
-> Handles hardware interrupts when packets arrive
-> Translates between kernel data structures and hardware operations

Every network interface (eth0, eth1 etc.) is represented inside the kernel as a net_device struct.

```c
struct net_device {
    char name[IFNAMSIZ];                      // interface name e.g. "eth0"
    unsigned char dev_addr[];                 // MAC address
    unsigned int mtu;                         // Maximum Transmission Unit
    const struct net_device_ops \*netdev_ops; // function pointers
};
```

When we run `ipconfig` or `ip link show`, we are reading data from this struct.

- #### sk_buff — The Packet Container:

Every packet in the kernel is stored in an **sk_buff** (socket buffer) structure. It's a smart buffer that:

--> Holds the packet data (headers + payload)
--> Tracks which layer the packet is at
--> Allows adding/removing headers without copying data

```
sk_buff journey for outgoing packet:
Application writes data
      ↓
TCP adds header → sk_buff
      ↓
IP adds header → sk_buff
      ↓
Ethernet adds header → sk_buff
      ↓
Driver sends sk_buff to NIC hardware
```

#### - ARP in the Kernel:

When an Ethernet frame needs to be sent, the kernel must resolve the destination IP to a MAC address. This is handled by the ARP subsystem:

1. Checks the ARP cache first
2. If not found → sends ARP broadcast
3. Stores result in cache for future use
4. We can view this with `arp -n` or `ip neigh show`

---

### Question 6: Describe how you would configure a basic LAN interface using the ip command in Linux (kernel.org).

```bash
zen@localhost:~$ ip link show

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens3:

zen@localhost:~$ ip addr show

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: ens3:

zen@localhost:~$ sudo ip link add dummy0 type dummy
[sudo] password for zen:

zen@localhost:~$ sudo ip link show dummy0

3: dummy0: <BROADCAST,NOARP> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
    link/ether c2:cc:f1:5d:9a:ad brd ff:ff:ff:ff:ff:ff

zen@localhost:~$ sudo ip addr add 192.168.1.10/24 dev dummy0

zen@localhost:~$ sudo ip link set dummy0 up

zen@localhost:~$ ip addr show dummy0

3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether c2:cc:f1:5d:9a:ad brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 scope global dummy0
       valid_lft forever preferred_lft forever
    inet6 fe80::c0cc:f1ff:fe5d:9aad/64 scope link
       valid_lft forever preferred_lft forever

```

---
