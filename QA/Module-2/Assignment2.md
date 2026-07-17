## Network Troubleshooting Scenario – Analysis

### 1. Which tool would you use first and why?

**First tool: Wireshark / tcpdump**

**Why:** Wireshark (or tcpdump for CLI) provides a **real-time, packet-level view** of all traffic. Given the symptoms – slow web pages, freezing video calls, but normal file downloads – a packet capture gives immediate visibility into:

- **TCP retransmissions** (indicates packet loss)
- **TCP window scaling / zero windows** (indicates receiver-side congestion)
- **Jitter and packet loss** for UDP traffic (video calls)
- **Round-trip time (RTT)** and response delays

---

### 2. What information would you collect using each tool?

#### Wireshark / tcpdump

- **TCP retransmissions** (packet loss / congestion)
- **TCP duplicate ACKs** (out-of-order packets)
- **Round-trip time (RTT)** from TCP handshake and subsequent ACKs
- **TCP zero-window events** (receiver buffer full)
- **Packet loss and jitter** for UDP traffic (video calls)
- **DNS query/response times** (slow web pages could be DNS-related)
- **TLS handshake time** (if web traffic is HTTPS)
- **HTTP response times** (server processing delays)
- **ICMP unreachable or redirect messages** (routing issues)
- **Throughput** (calculated from packet size/interval)

#### iPerf (Active Testing)

- **TCP throughput** (bandwidth capacity)
- **UDP throughput, jitter, and packet loss** (simulates real-time traffic)
- **Retransmissions** during TCP test
- **Bidirectional throughput** (to check asymmetry)

#### Additional checks (not tools, but critical)

- **Server-side logs** (web server access/error logs, application logs)
- **Network device logs** (router/switch interface errors, CRC errors)
- **QoS policy status** (prioritization/dropping)
- **Firewall/ACL logs** (dropped packets, throttling)

---

### 3. Three possible root causes

#### Cause 1: Packet Loss / Network Congestion

- **Symptom:** Slow web pages, freezing video calls, but normal file downloads.
- **Explanation:** Web pages and video calls are **interactive** (many small packets) and sensitive to packet loss and jitter. File downloads are **bulk data** (large sequential packets) and can tolerate some loss via TCP retransmission without noticeable impact.
- **Evidence in Wireshark:** High TCP retransmission count, duplicate ACKs, out-of-order packets. iPerf UDP test would show packet loss and jitter.
- **Common reasons:** Oversubscribed uplink, bandwidth throttling, Wi-Fi interference, switch buffer drops.

#### Cause 2: QoS Misconfiguration / Traffic Shaping

- **Symptom:** Web pages slow, video calls freeze, but file downloads are normal.
- **Explanation:** QoS policies may be **prioritising bulk traffic** (e.g., downloads) over interactive and real-time traffic. Or, bandwidth is being **rate-limited** per connection, affecting small-packet applications more than large sequential transfers.
- **Evidence in Wireshark:** Packets may be **delayed** (seen in TCP RTT) or **dropped** selectively. iPerf would show normal throughput for TCP but jitter/loss for UDP.
- **Common reasons:** Misconfigured QoS marking (DSCP), rate-limiting applied to specific ports/protocols (e.g., port 443), or traffic shaper dropping UDP packets.

#### Cause 3: Asymmetric Routing / Path Issues

- **Symptom:** Slow web pages, freezing video calls, normal file downloads.
- **Explanation:** Web and video traffic may be taking a **different return path** (e.g., via a slower satellite link or congested peer) than the forward path. TCP performance is affected by asymmetric delay and loss; bulk downloads may still achieve reasonable speed due to TCP's window growth.
- **Evidence in Wireshark:** TCP RTT may be **high or highly variable**. Traceroute may show different paths for forward and reverse. iPerf in reverse mode would show lower throughput than forward.
- **Common reasons:** BGP routing issues, ISP peering congestion, policy-based routing misconfiguration.

---

### 4. How to conclude whether the issue is network-related or application-related?

| Step                                      | Network-Related Evidence                                                                           | Application-Related Evidence                                                                                          |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **1. Packet Capture (Wireshark/tcpdump)** | High retransmissions, duplicate ACKs, zero-window events, packet loss, high RTT, ICMP unreachable. | Normal TCP behaviour, low RTT, zero loss, but HTTP/TLS handshake delays, high server response time, slow DNS queries. |
| **2. iPerf Test**                         | TCP throughput below expected, UDP loss/jitter high, retransmissions >1%.                          | TCP/UDP throughput normal, no loss/jitter.                                                                            |
| **3. Server Logs**                        | Not applicable (logs won't show network issues).                                                   | High response times, 5xx errors, slow database queries, high concurrent connections.                                  |
| **4. Server CPU/Memory**                  | Not applicable (issue is on network).                                                              | CPU/memory spikes correlate with slowdowns.                                                                           |
| **5. Traceroute / MTR**                   | Packet loss at certain hops, high latency at specific routers.                                     | No packet loss, consistent latency.                                                                                   |

#### Decision Matrix:

- **If** Wireshark shows **retransmissions, packet loss, zero-window events, or high RTT**, and iPerf confirms **throughput degradation or loss/jitter** → **Network-related**.
- **If** Wireshark shows **normal TCP behaviour** (no loss, low RTT) but **HTTP/TLS delays, slow DNS, or server-side ACK delays**, and iPerf shows **normal throughput** → **Application-related**.
- **If** Wireshark shows **both** network issues and application delays → **Network-related causing application degradation**.

#### Specific Test to Conclude:

1. **Run iPerf TCP and UDP tests** between client and server – if throughput is low / loss is high → **network issue**.
2. **Run the same iPerf tests locally on the server** (client on server itself) – if performance is normal → **network issue**; if still slow → **application/server issue**.
3. **Check TCP RTT and retransmissions** in Wireshark for a single HTTP request – if RTT is high or retransmissions occur → **network issue**; if RTT is low and no retransmissions but HTTP response is slow → **application issue**.

---

### Summary

| Step | Action                                                                    | Expected Outcome                             |
| ---- | ------------------------------------------------------------------------- | -------------------------------------------- |
| 1    | Run tcpdump/Wireshark on the client and server during a slow web session. | Identify retransmissions, zero-windows, RTT. |
| 2    | Run iPerf TCP/UDP tests between client and server.                        | Confirm throughput, loss, jitter.            |
| 3    | Check server logs and CPU/memory.                                         | Rule out application slowness.               |
| 4    | Run traceroute/mtr to check path and latency.                             | Identify congestion points.                  |
| 5    | Compare metrics: if retransmissions >1% or UDP loss >1% → network issue.  | Network-related.                             |

---
