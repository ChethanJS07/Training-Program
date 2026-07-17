### TCP Test (Host to Server):

#### Host: iperf3 -c 127.0.0.1 -t 10 # creates the traffic from host to server

```terminal
󰣇 Assignments/QA/Module-2  main  ? ❯ iperf3 -c 127.0.0.1 -t 10  .venv 3.14.6  7:59:50 PM
Connecting to host 127.0.0.1, port 5201
[ 5] local 127.0.0.1 port 34668 connected to 127.0.0.1 port 5201
[ ID] Interval Transfer Bitrate Retr Cwnd
[ 5] 0.00-1.00 sec 549 MBytes 4.60 Gbits/sec 0 639 KBytes
[ 5] 1.00-2.00 sec 476 MBytes 3.99 Gbits/sec 0 639 KBytes
[ 5] 2.00-3.00 sec 414 MBytes 3.47 Gbits/sec 1 639 KBytes
[ 5] 3.00-4.00 sec 630 MBytes 5.29 Gbits/sec 1 639 KBytes
[ 5] 4.00-5.00 sec 515 MBytes 4.32 Gbits/sec 0 639 KBytes
[ 5] 5.00-6.00 sec 581 MBytes 4.88 Gbits/sec 1 639 KBytes
[ 5] 6.00-7.00 sec 472 MBytes 3.96 Gbits/sec 0 639 KBytes
[ 5] 7.00-8.00 sec 428 MBytes 3.59 Gbits/sec 0 639 KBytes
[ 5] 8.00-9.00 sec 470 MBytes 3.95 Gbits/sec 0 639 KBytes
[ 5] 9.00-10.00 sec 439 MBytes 3.68 Gbits/sec 0 639 KBytes

---

[ ID] Interval Transfer Bitrate Retr
[ 5] 0.00-10.00 sec 4.86 GBytes 4.17 Gbits/sec 3 sender
[ 5] 0.00-10.01 sec 4.86 GBytes 4.17 Gbits/sec receiver

iperf Done.
```

#### Server: iperf3 -s # it listens to the traffic from host

```terminal
zen@localhost:~$ iperf3 -s
-----------------------------------------------------------
Server listening on 5201 (test #1)
-----------------------------------------------------------
Accepted connection from ::1, port 40730
[  5] local ::1 port 5201 connected to ::1 port 40732
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec   544 MBytes  4.56 Gbits/sec
[  5]   1.00-2.00   sec   476 MBytes  3.99 Gbits/sec
[  5]   2.00-3.00   sec   415 MBytes  3.48 Gbits/sec
[  5]   3.00-4.00   sec   631 MBytes  5.29 Gbits/sec
[  5]   4.00-5.00   sec   513 MBytes  4.30 Gbits/sec
[  5]   5.00-6.00   sec   582 MBytes  4.88 Gbits/sec
[  5]   6.00-7.00   sec   473 MBytes  3.97 Gbits/sec
[  5]   7.00-8.00   sec   426 MBytes  3.57 Gbits/sec
[  5]   8.00-9.00   sec   472 MBytes  3.96 Gbits/sec
[  5]   9.00-10.00  sec   437 MBytes  3.67 Gbits/sec
[  5]  10.00-10.01  sec  2.23 MBytes  3.76 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.01  sec  4.86 GBytes  4.17 Gbits/sec                  receiver

```

### TCP Test (Reverse):

#### Host: iperf3 -c 127.0.0.1 -t 10 -R # creates the traffic from server to host

```terminal
󰣇 Assignments/QA/Module-2   main  ? ❯ iperf3 -c 127.0.0.1 -t 10 -R                                                                 .venv 3.14.6  8:07:04 PM
Connecting to host 127.0.0.1, port 5201
Reverse mode, remote host 127.0.0.1 is sending
[  5] local 127.0.0.1 port 43402 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec   260 MBytes  2.17 Gbits/sec
[  5]   1.00-2.00   sec   314 MBytes  2.63 Gbits/sec
[  5]   2.00-3.00   sec   238 MBytes  2.00 Gbits/sec
[  5]   3.00-4.00   sec   308 MBytes  2.59 Gbits/sec
[  5]   4.00-5.00   sec   256 MBytes  2.14 Gbits/sec
[  5]   5.00-6.00   sec   278 MBytes  2.33 Gbits/sec
[  5]   6.00-7.00   sec   261 MBytes  2.19 Gbits/sec
[  5]   7.00-8.00   sec   267 MBytes  2.24 Gbits/sec
[  5]   8.00-9.00   sec   284 MBytes  2.38 Gbits/sec
[  5]   9.00-10.00  sec   300 MBytes  2.52 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.71 GBytes  2.33 Gbits/sec    3            sender
[  5]   0.00-10.00  sec  2.70 GBytes  2.32 Gbits/sec                  receiver

iperf Done.

```

#### Server: iperf3 -s # -R flag sends traffic in reverse direction

```terminal
-----------------------------------------------------------
Server listening on 5201 (test #2)
-----------------------------------------------------------
Accepted connection from ::1, port 39930
[  5] local ::1 port 5201 connected to ::1 port 39936
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]   0.00-1.00   sec   269 MBytes  2.25 Gbits/sec    1   3.06 MBytes
[  5]   1.00-2.00   sec   315 MBytes  2.64 Gbits/sec    0   3.06 MBytes
[  5]   2.00-3.00   sec   238 MBytes  1.99 Gbits/sec    1   3.06 MBytes
[  5]   3.00-4.00   sec   309 MBytes  2.59 Gbits/sec    0   3.06 MBytes
[  5]   4.00-5.00   sec   256 MBytes  2.15 Gbits/sec    0   3.06 MBytes
[  5]   5.00-6.00   sec   276 MBytes  2.32 Gbits/sec    1   3.06 MBytes
[  5]   6.00-7.00   sec   262 MBytes  2.20 Gbits/sec    0   3.06 MBytes
[  5]   7.00-8.00   sec   266 MBytes  2.23 Gbits/sec    0   3.06 MBytes
[  5]   8.00-9.00   sec   285 MBytes  2.39 Gbits/sec    0   3.06 MBytes
[  5]   9.00-10.00  sec   300 MBytes  2.52 Gbits/sec    0   3.06 MBytes
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  2.71 GBytes  2.33 Gbits/sec    3             sender

```

### UDP Test:

#### Host: iperf3 -c 127.0.0.1 -u -b 100M -t 10

```terminal
󰣇 Assignments/QA/Module-2   main  ? ❯ iperf3 -c 127.0.0.1 -u -b 100M -t 10
Connecting to host 127.0.0.1, port 5201
[  5] local 127.0.0.1 port 43265 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bitrate         Total Datagrams
[  5]   0.00-1.00   sec  11.9 MBytes   100 Mbits/sec  382
[  5]   1.00-2.00   sec  11.9 MBytes  99.9 Mbits/sec  381
[  5]   2.00-3.00   sec  11.9 MBytes   100 Mbits/sec  382
[  5]   3.00-4.00   sec  11.9 MBytes  99.9 Mbits/sec  381
[  5]   4.00-5.00   sec  11.9 MBytes   100 Mbits/sec  382
[  5]   5.00-6.00   sec  11.9 MBytes  99.9 Mbits/sec  381
[  5]   6.00-7.00   sec  11.9 MBytes   100 Mbits/sec  382
[  5]   7.00-8.00   sec  11.9 MBytes  99.9 Mbits/sec  381
[  5]   8.00-9.00   sec  11.9 MBytes  99.9 Mbits/sec  381
[  5]   9.00-10.00  sec  11.9 MBytes   100 Mbits/sec  382
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datas
[  5]   0.00-10.00  sec   119 MBytes   100 Mbits/sec  0.000 ms  0/3815 (0%)  ser
[  5]   0.00-10.00  sec   119 MBytes   100 Mbits/sec  0.053 ms  0/3815 (0%)  rer

iperf Done.

```

#### Server: iperf -s

```terminal
zen@localhost:~$ iperf3 -s
-----------------------------------------------------------
Server listening on 5201 (test #1)
-----------------------------------------------------------
Accepted connection from 127.0.0.1, port 59438
[  5] local 127.0.0.1 port 5201 connected to 127.0.0.1 port 43265
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-1.00   sec  11.9 MBytes   100 Mbits/sec  0.014 ms  0/382 (0%)
[  5]   1.00-2.00   sec  11.9 MBytes  99.9 Mbits/sec  0.006 ms  0/381 (0%)
[  5]   2.00-3.00   sec  11.9 MBytes   100 Mbits/sec  0.019 ms  0/382 (0%)
[  5]   3.00-4.00   sec  11.9 MBytes  99.9 Mbits/sec  0.015 ms  0/381 (0%)
[  5]   4.00-5.00   sec  11.9 MBytes   100 Mbits/sec  0.005 ms  0/382 (0%)
[  5]   5.00-6.00   sec  11.9 MBytes  99.9 Mbits/sec  0.036 ms  0/381 (0%)
[  5]   6.00-7.00   sec  11.9 MBytes   100 Mbits/sec  0.042 ms  0/382 (0%)
[  5]   7.00-8.00   sec  11.9 MBytes  99.9 Mbits/sec  0.029 ms  0/381 (0%)
[  5]   8.00-9.00   sec  11.9 MBytes  99.9 Mbits/sec  0.039 ms  0/381 (0%)
[  5]   9.00-10.00  sec  11.9 MBytes   100 Mbits/sec  0.053 ms  0/382 (0%)
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate         Jitter    Lost/Total Datagrams
[  5]   0.00-10.00  sec   119 MBytes   100 Mbits/sec  0.053 ms  0/3815 (0%)  receiver

```

---

## iPerf Performance Benchmark: TCP vs UDP

### 1. Test Environment

- **Server**: Ubuntu VM (QEMU) with SSH forwarding on localhost:2222.
- **Client**: Ubuntu host.
- **Network**: Local loopback (127.0.0.1) via SSH tunnel.

---

### 2. TCP Throughput Results

| Direction | Average Bitrate | Retransmissions |
| --------- | --------------- | --------------- |
| Host → VM | 4.17 Gbps       | 3               |
| VM → Host | 2.33 Gbps       | 3               |

**Observation**: TCP achieves high throughput and adapts to network conditions. Retransmissions are minimal (3 total), indicating a stable link. The asymmetry may be due to VM CPU/IO overhead in the reverse path.

---

### 3. UDP Throughput Results

| Send Rate | Received Bitrate | Jitter (ms) | Packet Loss |
| --------- | ---------------- | ----------- | ----------- |
| 100 Mbps  | 100 Mbps         | 0.053       | 0%          |

**Observation**: At 100 Mbps, UDP achieves perfect delivery with zero loss and very low jitter. This indicates the link can easily handle the load. Testing at higher rates (500 Mbps, 1 Gbps) would likely show increased loss and jitter as the link approaches saturation.

---

### 4. Key Metrics

| Metric              | TCP                                                                                                               | UDP                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Throughput**      | Maximises bandwidth usage; adapts to congestion. Achieved **4.17 Gbps** and **2.33 Gbps** depending on direction. | Sends at a fixed rate (**100 Mbps**). Received bitrate matches sent (100 Mbps) when no loss occurs. |
| **Jitter**          | Not reported (TCP smoothes delay).                                                                                | **0.053 ms** – very low, indicating stable network conditions.                                      |
| **Packet Loss**     | Zero (TCP retransmits lost packets). Retransmissions: **3** total, which is negligible.                           | **0%** loss at 100 Mbps – all 3815 datagrams delivered.                                             |
| **Retransmissions** | **3** retransmissions across ~4.8 GB transferred – excellent performance.                                         | Not applicable (UDP does not retransmit).                                                           |

---

### 5. Differences Observed

- **TCP** uses flow control and retransmission to ensure reliability. It achieves higher throughput by dynamically adjusting to available capacity. The small number of retransmissions (3) shows the link is clean.
- **UDP** is simpler and faster, but provides no reliability. At 100 Mbps, it performs perfectly with zero loss and minimal jitter. If the send rate exceeded the link capacity, loss and jitter would increase.
- **Jitter** is a UDP‑only metric – it measures delay variation. The **0.053 ms** jitter is excellent for real‑time applications.

---

### 6. Sample Test Output Summary

| Test | Direction | Avg Bitrate | Retransmits | Jitter  | Loss % |
| ---- | --------- | ----------- | ----------- | ------- | ------ |
| TCP  | Host → VM | 4.17 Gbps   | 3           | N/A     | 0%     |
| TCP  | VM → Host | 2.33 Gbps   | 3           | N/A     | 0%     |
| UDP  | Host → VM | 100 Mbps    | N/A         | 0.053ms | 0%     |

---
