# Wi-Fi Training Program

## Module-3 - Assignment Questions

---

### Question 1: What are the different 802.11 PHY layer standards? Compare their characteristics.

The major 802.11 PHY layer standards with their characteristics:

| Standard           | Band        | Max Rate | Modulation              | Channel Width    | MIMO             |
| ------------------ | ----------- | -------- | ----------------------- | ---------------- | ---------------- |
| 802.11b            | 2.4 GHz     | 11 Mbps  | DSSS (CCK)              | 22 MHz           | No               |
| 802.11a/g          | 5 / 2.4 GHz | 54 Mbps  | OFDM                    | 20 MHz           | No               |
| 802.11n (Wi-Fi 4)  | 2.4/5 GHz   | 600 Mbps | OFDM with MIMO          | 20/40 MHz        | Up to 4 streams  |
| 802.11ac (Wi-Fi 5) | 5 GHz       | 6.9 Gbps | OFDM + MU-MIMO (DL)     | 20/40/80/160 MHz | Up to 8 streams  |
| 802.11ax (Wi-Fi 6) | 2.4/5/6 GHz | 9.6 Gbps | OFDMA + MU-MIMO (DL/UL) | 20/40/80/160 MHz | Up to 8 streams  |
| 802.11be (Wi-Fi 7) | 2.4/5/6 GHz | 46 Gbps  | OFDMA (16 streams)      | Up to 320 MHz    | Up to 16 streams |

Key comparisons:

1. Data rate increases with each generation (2 Mbps → 46 Gbps).

2. Band evolved from only 2.4 GHz to include 5 GHz (802.11a), then 6 GHz (802.11ax/be).

3. Modulation progressed from DSSS to OFDM to OFDMA, improving spectral efficiency.

4. Channel width expanded from 20 MHz to up to 320 MHz (Wi-Fi 7).

5. MIMO introduced in 802.11n, with MU-MIMO in 802.11ac/ax enabling multi-user concurrency.

---

### Question 2: What are DSSS and FHSS? How do they work?

1. DSSS (Direct Sequence Spread Spectrum): spreads each data bit across a wide frequency band by XORing it with a higher-rate chipping sequence (e.g., Barker code in 802.11). The receiver uses the same code to despread and recover the original data. This provides processing gain against interference and multipath. In 802.11b, DSSS with CCK achieved up to 11 Mbps.

2. FHSS (Frequency Hopping Spread Spectrum): rapidly switches carrier frequencies in a pseudo-random sequence known to both transmitter and receiver. It dwells on each frequency for a short time (e.g., 100 hops/sec). This avoids narrowband interference by "hopping away" and offers inherent obfuscation.

- Key difference: DSSS transmits continuously across a wide band; FHSS hops between narrow frequencies over time. Both are spread spectrum methods, but FHSS is limited to low data rates (2 Mbps) and is obsolete in modern Wi-Fi, while DSSS enabled 11 Mbps in 802.11b before being replaced by OFDM.

---

### Question 3: How do modulation schemes work in the PHY layer? Compare different modulation schemes and their performance across various Wi-Fi standards.

Modulation schemes encode digital bits onto analog radio waves by varying amplitude and/or phase. In Wi-Fi, higher-order QAM (e.g., 256-QAM, 1024-QAM) increases data rate but demands better SNR and shorter range.

Comparison across standards:

1. 802.11b used DSSS with BPSK/QPSK and CCK (max 11 Mbps).

2. 802.11a/g introduced OFDM with BPSK to 64-QAM (54 Mbps).

3. 802.11n kept 64-QAM but added MIMO (up to 4 streams, 600 Mbps).

4. 802.11ac added 256-QAM (8 bits/symbol) and wider channels (6.9 Gbps).

5. 802.11ax supports 1024-QAM (10 bits/symbol) plus OFDMA for efficiency.

6. 802.11be adds 4096-QAM (12 bits/symbol) and 16 streams.

Performance trade-off: BPSK is most robust (longest range, low throughput); 1024-QAM gives highest throughput but only near the AP with excellent signal. Wi-Fi dynamically adapts modulation based on real-time channel conditions.

---

### Question 4: What is the significance of OFDM in WLAN? How does it improve performance?

Significance of OFDM in WLAN: OFDM (Orthogonal Frequency Division Multiplexing) resolves the multipath fading problem that plagued earlier DSSS-based Wi-Fi.
By splitting a high-rate data stream into many parallel low-rate sub-streams transmitted on orthogonal, overlapping sub-carriers, OFDM makes each symbol period much longer than the channel's delay spread, eliminating inter-symbol interference (ISI) with the help of a Guard Interval.

How it improves performance:

- Increases data rates – Enables QAM modulation on hundreds of sub-carriers, achieving up to 54 Mbps (802.11a/g) and beyond with wider channels and more sub-carriers.

- Enhances robustness – Multipath reflections cause frequency-selective fading, but because each sub-carrier is narrow, simple equalization recovers data efficiently.

- Improves spectral efficiency – Overlapping sub-carriers without guard bands maximize bandwidth utilization.

- Supports scalability – Channel width (20/40/80/160/320 MHz) scales by adding more sub-carriers, enabling multi-gigabit speeds in 802.11ac/ax/be.

OFDM is foundational to all modern Wi-Fi standards (802.11a/g/n/ac/ax/be), enabling reliable, high-throughput indoor wireless communication.

---

### Question 5: How are frequency bands divided for Wi-Fi? Explain different bands and their channels.

Wi-Fi frequency bands are divided into channels of specific widths (20/40/80/160/320 MHz) to organize transmissions and avoid interference.

2.4 GHz band (2.400–2.4835 GHz): 20 MHz channels numbered 1–11 (US). Only three non-overlapping channels (1, 6, 11) exist. Supports 20 or 40 MHz widths. Long range but crowded.

5 GHz band (5.150–5.825 GHz): Many 20 MHz channels (e.g., 36, 40, 44, 48, 52, 56, 60, 64, 100–144, 149–165). Supports 20/40/80/160 MHz widths. DFS channels require radar detection. Less interference, higher throughput, shorter range.

6 GHz band (5.925–7.125 GHz): New with Wi-Fi 6E, offering 59+ 20 MHz channels. Supports up to 320 MHz channels (Wi-Fi 7). No legacy interference, very high speeds, short range.

Channel bonding combines adjacent 20 MHz channels (e.g., 80 MHz = 4×20 MHz) to increase data rates, but consumes more spectrum and increases interference probability.

---
