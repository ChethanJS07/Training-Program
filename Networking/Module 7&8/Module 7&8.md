# Networking Training Program - Module 7 and 8 Assignment Questions

## Output: [Drive Link](https://drive.google.com/drive/folders/1xBKeRVyEhNCJzfyFXOgQ2QRq96xuRf28?usp=sharing)

---

### Question 1:

### Try Test-Connection and nslookup commands for below websites:

- www.google.com
- www.facebook.com
- www.amazon.com
- www.github.com
- www.cisco.com

```bash
#!/usr/bin/env bash

echo '===Google==='
ping -c 4 www.google.com
nslookup www.google.com
echo -e "------------\n"

echo '===Facebook==='
ping -c 4 www.facebook.com
nslookup www.facebook.com
echo -e "------------\n"

echo '===Amazon==='
ping -c 4 www.amazon.com
nslookup www.amazon.com
echo -e "------------\n"

echo '===Github==='
ping -c 4 www.github.com
nslookup www.github.com
echo -e "------------\n"

echo '===Cisco==='
ping -c 4 www.cisco.com
nslookup www.cisco.com
echo -e "------------\n"
```

---

### Question 3:

### Explore traceroute/tracert for different websites (e.g., google.com) and analyze the parameters in the output and explore different options for traceroute command.

```bash
root@localhost:/mnt/shared# traceroute google.com

traceroute to google.com (142.251.43.142), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.540 ms  0.488 ms  0.464 ms
 2  192.168.1.1 (192.168.1.1)  2.480 ms  6.990 ms  6.967 ms
 3  212.96.115.1.hathway.com (115.96.212.1)  6.946 ms  6.924 ms  6.903 ms
 4  185.18.210.89.hathway.com (210.18.185.89)  11.353 ms  11.329 ms  11.309 ms
 5  185.18.210.34.hathway.com (210.18.185.34)  6.815 ms  11.265 ms  11.243 ms
 6  185.18.210.33.hathway.com (210.18.185.33)  11.222 ms  13.175 ms  9.552 ms
 7  * * *
 8  * * *
 9  * * *
10  216.239.56.70 (216.239.56.70)  15.849 ms 216.239.47.142 (216.239.47.142)  15.827 ms 216.239.43.238 (216.239.43.238)  11.087 ms
11  172.253.71.132 (172.253.71.132)  10.899 ms 172.253.71.2 (172.253.71.2)  15.759 ms 142.251.55.121 (142.251.55.121)  10.855 ms
12  142.250.63.173 (142.250.63.173)  15.670 ms bkk03s01-in-f14.1e100.net (142.251.43.142)  13.030 ms  12.948 ms

# options
root@localhost:/mnt/shared# traceroute -n google.com # Numeric only (No DNS lookups) - faster

traceroute to google.com (142.251.43.142), 30 hops max, 60 byte packets
 1  10.0.2.2  0.137 ms  0.085 ms  0.083 ms
 2  192.168.1.1  2.679 ms  2.626 ms  3.086 ms
 3  115.96.212.1  7.304 ms  7.283 ms  7.257 ms
 4  210.18.185.89  12.124 ms  12.102 ms  12.078 ms
 5  210.18.185.34  7.166 ms  12.033 ms  7.122 ms
 6  210.18.185.33  11.989 ms  11.865 ms  11.800 ms
 7  * * *
 8  * * *
 9  * * *
10  142.251.55.238  12.327 ms 142.250.233.142  7.245 ms 142.251.55.216  12.171 ms
11  142.251.230.52  12.148 ms 142.251.230.70  12.125 ms 142.251.55.121  7.634 ms
12  142.250.208.153  12.082 ms 142.251.43.142  18.376 ms  13.396 ms

root@localhost:/mnt/shared# traceroute -I google.com # ICMP Echo requests instead of UDP

traceroute to google.com (142.251.43.142), 30 hops max, 60 byte packets
 1  lcmaaa-aq-in-f14.1e100.net (142.251.43.142)  108.213 ms  108.166 ms  108.158 ms

root@localhost:/mnt/shared# traceroute -T google.com # TCP requests are sent instead of UDP

traceroute to google.com (142.251.223.174), 30 hops max, 60 byte packets
 1  lcmaaa-am-in-f14.1e100.net (142.251.223.174)  9.321 ms  9.256 ms  9.691 ms

root@localhost:/mnt/shared# traceroute -m 10 google.com # Max hops is set to 10

traceroute to google.com (142.251.223.174), 10 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.217 ms  0.162 ms  0.148 ms
 2  192.168.1.1 (192.168.1.1)  2.294 ms  7.054 ms  7.032 ms
 3  212.96.115.1.hathway.com (115.96.212.1)  11.212 ms  11.184 ms  11.158 ms
 4  185.18.210.89.hathway.com (210.18.185.89)  11.133 ms  11.108 ms  11.084 ms
 5  185.18.210.34.hathway.com (210.18.185.34)  6.857 ms  6.829 ms  6.803 ms
 6  185.18.210.33.hathway.com (210.18.185.33)  15.078 ms  9.784 ms  13.789 ms
 7  * * *
 8  * * *
 9  * * *
10  209.85.253.84 (209.85.253.84)  13.828 ms 209.85.247.250 (209.85.247.250)  10.310 ms 142.251.55.60 (142.251.55.60)  9.918 ms

root@localhost:/mnt/shared# traceroute google.com 100 # packets size is set to 100

traceroute to google.com (172.217.24.206), 30 hops max, 100 byte packets
 1  _gateway (10.0.2.2)  0.504 ms  0.474 ms  0.475 ms
 2  192.168.1.1 (192.168.1.1)  3.789 ms  3.777 ms  4.211 ms
 3  212.96.115.1.hathway.com (115.96.212.1)  8.409 ms  8.391 ms  8.378 ms
 4  185.18.210.89.hathway.com (210.18.185.89)  12.859 ms  12.848 ms  12.838 ms
 5  * * *
 6  185.18.210.33.hathway.com (210.18.185.33)  12.796 ms  11.727 ms  11.701 ms
 7  * * *
 8  * * *
 9  * * *
10  216.239.54.196 (216.239.54.196)  14.466 ms 108.170.231.128 (108.170.231.128)  14.454 ms 142.251.55.88 (142.251.55.88)  10.266 ms
11  142.250.208.230 (142.250.208.230)  10.492 ms 209.85.142.247 (209.85.142.247)  72.172 ms  72.095 ms
12  142.251.230.71 (142.251.230.71)  76.284 ms 172.253.71.3 (172.253.71.3)  76.155 ms 172.253.75.15 (172.253.75.15)  76.128 ms
13  pnmaaa-at-in-f14.1e100.net (172.217.24.206)  76.074 ms  71.833 ms 209.85.142.247 (209.85.142.247)  71.812 ms
```

---
