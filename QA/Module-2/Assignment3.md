### Assignment 3 – Packet Analysis

---

### Capture or download a sample Wireshark capture file.

### Identify and explain:

####  One TCP 3-way handshake.

```text
Client                               Server
  |                                    |
  |            SYN (Seq=X)             |
  |----------------------------------->|
  |                                    |
  |        SYN-ACK (Seq=Y, Ack=X+1)    |
  |<-----------------------------------|
  |                                    |
  |            ACK (Ack=Y+1)           |
  |----------------------------------->|
  |                                    |
```

- TCP SYN: (Seq No. = 0)
  ![TCP SYN](~/embedUR/Assignments/QA/Module-2/tcp_syn.png)

- TCP SYN-ACK: (Seq No. = 0, Ack No. = 1)
  ![TCP SYN-ACK](~/embedUR/Assignments/QA/Module-2/tcp_syn_ack.png)

- TCP ACK: (Seq No. = 1, Ack No. = 1)
  ![TCP ACK](~/embedUR/Assignments/QA/Module-2/tcp_ack.png)

---

####  One DNS query and response.

- DNS Query:
  ![DNS Query](~/embedUR/Assignments/QA/Module-2/dns_query.png)

- DNS Response:
  ![DNS Response](~/embedUR/Assignments/QA/Module-2/dns_response.png)

---

####  One HTTP or HTTPS transaction.

- HTTPS Client Hello:
  ![HTTPS Client Hello](~/embedUR/Assignments/QA/Module-2/tcp_client.png)

- HTTPS Server Hello:
  ![HTTPS Server Hello](~/embedUR/Assignments/QA/Module-2/tcp_server.png)

---

####  Any retransmissions or duplicate ACKs observed.

None, since the HTTPS handshake was clean.

- Wireshark Filters:
  - Retransmissions: tcp.analysis.retransmission
  - Duplicate ACK: tcp.analysis.duplicate_ack

---

####  Overall health of the communication.

| Aspect                           | Observation                                                             |
| -------------------------------- | ----------------------------------------------------------------------- |
| TCP handshake                    | Completed in ~0.098 seconds, no retransmissions.                        |
| DNS response                     | Successful resolution of `embedur.ai` to two IPv4 addresses (No error). |
| TLS handshake                    | TLS 1.3, completed in one round‑trip (Client Hello → Server Hello).     |
| Retransmissions / Duplicate ACKs | None observed.                                                          |
| Throughput / errors              | No RST packets, no ICMP errors, no zero‑window events.                  |

**Conclusion**:
The communication was **healthy** – low latency, no loss, and a fast TLS handshake. The connection performed well, indicating no network issues at the time of capture.

---
