# Wi-Fi Training Program

## Module-2 - Assignment Questions

---

### Question 1: Brief about SplitMAC architecture and how it improves the AP’s performance.

#### SplitMAC:

In a traditional AP, all the traffic is handled in a single layer of the AP itself. In SplitMAC architecture, the MAC layer is
split between the AP and the Wireless LAN Controller (WLC).

- Real time MAC functions: Handled by the AP
- Non-Real time MAC functions: Handled by the Wireless LAN Controller (WLC)

This improves AP performance by:

- Reducing AP processing overhead (simpler hardware)
- Enabling centralized RF optimization (dynamic channel/power)
- Accelerating client roaming via controller coordination
- Allowing scalable, cost-effective deployments
- Simplifying maintenance (centralized firmware/configuration)

---

### Question 2: Describe about CAPWAP, explain the flow between AP and Controller.

#### CAPWAP:

CAPWAP (Control and Provisioning of Wireless Access Points) is a standard protocol that enables a Wireless LAN Controller (WLC) to manage lightweight APs.
It operates over UDP (control: 5246, data: 5247).

Flow sequence:

The flow follows a discovery, join, configuration, and run sequence:

AP WLC
|---- Discovery ----->|
|<--- Discovery Resp---|
|----- Join Req ------>|
|<---- Join Resp ------|
|--- Config Status Req->|
|<-- Config Status Resp-|
|==== Control (UDP 5246) ====|
|==== Data (UDP 5247) ====|
|-- Echo Req (keepalive)|
|--- Echo Resp ---------|

---

### Question 3: Where does CAPWAP fit in the OSI model, what are the two tunnels in CAPWAP and their purpose?

CAPWAP is a tunneling protocol that operates primarily at Layer 4 (Transport) and above, but it encapsulates Layer 2 (802.11) frames.

Two tunnels in CAPWAP:

- Control tunnel (UDP 5246) – Carries management and control messages (AP join, config, keepalives, RF commands, client association responses). Ensures AP can be centrally managed.

- Data tunnel (UDP 5247) – Carries user data frames encapsulated from wireless clients. Forwards client traffic between AP and WLC.

---

### Question 4: What is the difference between Lightweight APs and Cloud-based APs?

- Controller location: On-premise (LAP) vs. Cloud (Cloud AP).

- Management: Local IP/CLI vs. Web dashboard anywhere.

- Protocol: CAPWAP vs. proprietary cloud tunnel.

- Cost: Upfront hardware+licenses vs. recurring subscription.

- Failure impact: WLC failure can disrupt network; cloud outage loses management but data keeps flowing.

- Best for: LAPs for large secure campuses; Cloud APs for distributed sites, retail, SMBs.

---

### Question 5: How is the CAPWAP tunnel maintained between AP and controller?

The CAPWAP tunnel is maintained primarily through periodic keepalive (Echo) messages exchanged over the control tunnel (UDP 5246).
The AP sends an Echo Request to the WLC every 30 seconds (configurable), and the WLC must reply with an Echo Response.
If the AP misses several consecutive responses (e.g., 3), it declares the tunnel dead and enters discovery mode to rejoin the same or backup WLC.

---

### Question 6: What is the difference between Sniffer and monitor mode, use case for each mode?

- Monitor mode:
  Monitor mode is a capability of a Wi-Fi adapter (laptop or USB) that allows it to passively listen to all 802.11 frames on a channel without associating to any AP.
  It is used for local packet capture, troubleshooting, site surveys, and security auditing.

- Sniffer mode:
  Sniffer mode is a dedicated role for an enterprise AP (managed by a WLC) where the AP stops serving clients and instead captures all frames on a channel, forwarding them to a central analyzer (e.g., via CAPWAP).
  It is used for remote, distributed packet capture across large networks without physical access to each AP.

---

### Question 7: If WLC deployed in WAN, which AP mode is best for local network and how?

#### Why FlexConnect is best for WLC in WAN:

1. Data traffic stays local – Client internet/LAN traffic does not traverse the WAN, avoiding latency and bandwidth issues.

2. Resilient to WAN failure – AP can continue serving clients (with local switching and local authentication) even if the WAN link drops. When WAN returns, it syncs with WLC.

3. Control traffic minimal – Only management and occasional roaming updates go over WAN.

4. Supports local VLAN mapping – AP can map SSIDs to local VLANs at the branch.

---

### Question 8: What are challenges if deploying autonomous APs (more than 50) in a large network like a university?

1. No central configuration – Each AP must be configured individually; changing an SSID or security setting requires touching every AP.

2. No seamless roaming – Clients re-associate and re-authenticate when moving between APs, causing delays and dropouts.

3. Manual RF management – Channel and power must be manually planned and adjusted; 2.4 GHz channel overlap is unavoidable.

4. No load balancing – Clients may overload one AP while another remains idle.

5. No centralized monitoring – Troubleshooting requires logging into each AP individually.

6. Firmware upgrades are impractical – Updating 50+ APs manually is error-prone and time-consuming.

7. Security inconsistency – Ensuring identical RADIUS settings, ACLs, and VLANs across all APs is difficult.

8. No rogue AP detection – Cannot cooperatively identify fake APs.

---

### Question 9: What happens on wireless client connected to Lightweight AP in local mode if WLC goes down?

- Existing clients – Since client data is typically tunnelled to the WLC (central switching), data traffic stops immediately. The AP cannot forward client frames because it lacks the necessary switching intelligence.

- New clients – Cannot associate or authenticate because these functions require the WLC.

- Roaming – Disabled.

- AP behavior – The AP continues broadcasting beacons (SSID visible) but cannot serve data. It repeatedly attempts to rediscover and rejoin the same or backup WLC.

- Recovery – When the WLC is restored, the AP re-establishes the CAPWAP tunnel, and clients must reconnect (or may automatically recover if they were in a waiting state).

---
