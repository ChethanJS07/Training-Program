# Wi-Fi Training Program

## Module-1 - Assignment Questions

---

### Question 1: In which OSI layer does the Wi-Fi standard/protocol fit?

The Wi-Fi standard (IEEE 802.11) fits in Layer 1 (Physical layer) and Layer 2 (Data Link layer – MAC sublayer) of the OSI model.

---

### Question 2: Can you share the Wi-Fi devices that you are using day to day life, share that device's wireless capability/properties after connecting to network.

### Match your device to corresponding Wi-Fi Generations based on properties.

Device: Laptop with Realtek RTL8822CE 802.11ac PCIe adapter.
Properties after connecting: freq 2452 MHz (2.4 GHz), tx bitrate 270 Mbps MCS 15 40MHz, signal -42 dBm.
Wi-Fi generation: Wi-Fi 4 (802.11n).
Adapter capability: Wi-Fi 5 (802.11ac) on 5 GHz.

```
󰣇 ~ ❯ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
link/ether 30:03:c8:83:9a:b1 brd ff:ff:ff:ff:ff:ff
altname wlp1s0
altname wlx3003c8839ab1

󰣇 ~ ❯ iw dev wlo1 link
Connected to 44:fb:5a:96:84:2a (on wlo1)
SSID: Subramanyam
freq: 2452.0
RX: 852065841 bytes (727019 packets)
TX: 18546855 bytes (100453 packets)
signal: -42 dBm
rx bitrate: 130.0 MBit/s MCS 15
tx bitrate: 270.0 MBit/s MCS 15 40MHz
bss flags: short-slot-time
dtim period: 1
beacon int: 100

󰣇 ~ ❯ lspci | grep -i network
01:00.0 Network controller: Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter
```

---

### Question 3: What is BSS and ESS?

BSS (Basic Service Set) is the smallest Wi-Fi network unit, consisting of a single Access Point (AP) and the client devices associated with it.
It is identified by the AP's MAC address (BSSID).

ESS (Extended Service Set) is a set of two or more BSSs connected by a distribution system (wired or wireless backbone), all sharing the same SSID.
It allows clients to roam seamlessly between APs without disconnecting or re-authenticating

---

### Question 4: What are the basic functionalities of a Wi-Fi Access Point?

1. Beacon transmission – announces the network’s presence and capabilities.

2. Authentication and association – manages client connections.

3. Wireless-to-wired bridging – forwards traffic between Wi-Fi and Ethernet.

4. Frame relaying – delivers data between clients and the wired network.

5. Security enforcement – handles encryption, authentication, and key management.

6. Channel management – selects and operates on a radio channel.

7. Power save support – buffers traffic for sleeping clients.

8. MAC coordination (CSMA/CA) – controls medium access and sends acknowledgements.

---

### Question 5: Difference between Bridge mode and Repeater mode.

Bridge mode connects two separate wired networks over a wireless link without accepting wireless clients.
It acts as a transparent Layer 2 bridge, typically for point-to-point links (e.g., between buildings).

Repeater mode extends the range of an existing Wi-Fi network by receiving the signal from a root AP and retransmitting it to wireless clients, using the same SSID.
It accepts clients but halves throughput because it uses the same channel for both receiving and transmitting.

---

### Question 6: What are the differences between 802.11a and 802.11b?

- The main differences between 802.11a and 802.11b are:
  - Frequency: 802.11a uses 5 GHz; 802.11b uses 2.4 GHz.
  - Maximum speed: 802.11a supports up to 54 Mbps; 802.11b supports only up to 11 Mbps.
  - Modulation: 802.11a uses OFDM; 802.11b uses DSSS/CCK.
  - Range: 802.11b has longer range due to lower frequency; 802.11a has shorter range but less interference.
  - Interference: 802.11b operates in the crowded 2.4 GHz band (microwaves, Bluetooth); 802.11a in the cleaner 5 GHz band.
  - Cost: 802.11b devices were cheaper and more common in homes; 802.11a was initially more expensive and enterprise-focused.

---

### Question 8: What is the difference between IEEE and WFA?

The IEEE (Institute of Electrical and Electronics Engineers) develops the technical 802.11 standards that define how Wi-Fi works at the physical and MAC layers (e.g., 802.11ac, 802.11ax).

The Wi-Fi Alliance (WFA) is an industry consortium that tests and certifies Wi-Fi products for interoperability. It also creates simplified branding names like "Wi-Fi 6" (for 802.11ax) and security protocols like WPA, WPA2, WPA3.

---

### Question 10: List down the Wi-Fi topologies and use cases of each one.

1. Infrastructure (BSS/ESS) – Clients connect via AP(s). Use case: Home, office, campus Wi-Fi.
2. Ad-Hoc (IBSS) – Direct peer-to-peer without AP. Use case: Temporary file sharing, emergency networks.
3. Mesh – Multiple APs wirelessly interconnecting, self-healing. Use case: Large homes, smart cities, rural broadband.
4. Repeater/Extender – Wireless device retransmits AP signal. Use case: Extending coverage to dead zones.
5. Bridge (PtP/PtMP) – Connects separate wired networks wirelessly. Use case: Linking buildings, surveillance backhaul.
6. Controller-based (CAPWAP) – Lightweight APs with central controller. Use case: Large enterprises, hospitals, universities.
7. Wi-Fi Direct – Direct device-to-device with security. Use case: Wireless printing, file sharing, screen mirroring.

---
