# Wi-Fi Training Program

## Module-6 - Assignment Questions

---

### Question 1: What are the pillars of Wi-Fi Security?

#### Wi-Fi Security is built on _three_ main pillars:

- Authentication: Verifies the identity of the device/user.
- Encryption: Protecting data confidentiality over the air.
- Integrity: Ensuring data is not altered during transmission.

---

### Question 2: Explain the difference between Authentication and Encryption in Wi-Fi Security.

|                   | Authentication                                          | Encryption                                                                   |
| ----------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| _Purpose_         | Providing identity                                      | Protecting data                                                              |
| _When it happens_ | Before allowing network access, during connection setup | After Authentication                                                         |
| _How it works_    | Client and Access point exchange credentials            | Using algorithms like RC4, AES etc                                           |
| _Outcome_         | If Authentication fails, client is rejected             | Even if packets are leaked, attackers can't decrypt without encryption keys. |

---

### Question 3: Explain the differences between WEP, WPA, WPA2 and WPA3.

|    Feature     |     WEP      |         WPA         |      WPA2       |        WPA3        |
| :------------: | :----------: | :-----------------: | :-------------: | :----------------: |
|   Encryption   | RC4 (static) | RC4 (TKIP, Dynamic) |    AES-CCMP     | AES-CCMP/ AES-GCMP |
|   Integrity    |    CRC-32    |         MIC         |       CCM       |        AEAD        |
| Key Management |    Manual    |   4-Way handshake   | 4-Way handshake |        SAE         |

---

### Question 4: Why is WEP considered insecure compared to WPA2 or WPA3?

WEP is considered insecure compared to WPA2 and WPA3 for the following reasons:

- WEP uses a weak RC4 encryption algorithm, with small initialization vectors (IV), static shared keys.
- WPA2 and WPA3 uses AES encryption, dynamic per-session keys, strong Integrity, and manual authentication.
- These flaws make WEP vulnerable from freely available tools.

---

### Question 5: Why was WPA2 introduced?

- #### Why WPA was introduced:
  - WEP was broken as its RC4 encryption was proved to be not as effective as it used to be
  - So WPA was introduced as an intermediate solution, adding TKIP along with the RC4 encryption
  - But, as it still used RC4 as its core, it eventually became vulnerable
  - So, a newer WEP2 with a stronger AES encryption was introduced with CCMP intergrity while being backwards compatible even with older devices

---

### Question 6: What is the role of the Pairwise Master Key (PMK) in the 4-way handshake?

The Pairwise Master Key (PMK) is a shared secret between the client and the access point. It is never transmitted over the air.

- #### Role of PMK in the handshake:
  - The 4-way handshake used the PMK to generate temporary session keys for encryption/intergrity, and to prove both sides have the same PMK
  - It is the root secret from which all session keys are derived
  - Without correct PMK, the client cannot compute the correct PTK (Pairwise Transient key), so MIC (Message Integrity Check) fails, so handshake fails
  - Ensures that only the devices that know the PMK can join the network
  - If the attackers get the PMK, they can decrypt past recorded traffic

---

### Question 7: How does the 4-way handshake ensure mutual authentication between the client and the access point?

- The mutual handshake signifies that both the client and the server proves their identity to each other.
  - The client proves to the AP that it knows the correct PMK
  - The AP proves to the client that it also knows the correct PMK

- The 4-Way handshake achieves this:
  - Message 1 (AP --> Client): AP sends the client a ANonce number.
  - Message 2 (Client --> AP): Client sends the AP a SNonce + MIC by deriving it from the existing PMK.
  - Message 3 (AP --> Client): AP sends GTK + MIC encrypted and integrity-protected, using keys derived from PMK + both nonces.
  - Message 4 (Client --> AP): Client sends confirmation MIC. After final verification, both install keys.

---

### Question 8: What will happen if we put a wrong passphrase during a 4-way handshake?

When the client puts a wrong passphrase during a 4-way handshake, the MIC verification fails in the AP's side, and the handshake fails, and the device
will not be able to connect to the Wi-Fi network.

The AP rejects the handshake and the Client device will be disassociated from the Network and will be prompted to re-enter the correct passphrase.

---

### Question 9: What problem does 802.1X solve in a network?

- 802.1X solves the problem of per-user/device authentication and centralized access control in networks.
- Before 802.1X, shared passwords (like WPA2-PSK) provided no individual identity, making it hard to revoke access for one user or assign different privileges.
- 802.1X introduces a framework where each user or device authenticates independently against a central RADIUS server, using unique credentials (e.g., username/password or certificates).
- This enables dynamic per-user key derivation, individual revocation, and granular network policies (VLAN, ACLs) – solving scalability and security limitations of shared secrets.

---

### Question 10: How does 802.1X enhance security over wireless networks?

- 802.1X enhances security over wireless networks by providing per-user/device authentication with unique credentials, eliminating the shared passphrase problem of WPA2-Personal.
- It enables mutual authentication (client verifies the network via RADIUS server certificates), preventing rogue AP attacks.
- Offline dictionary attacks become impractical, especially with certificate-based EAP-TLS.
- Each session gets unique encryption keys, so one user cannot decrypt another's traffic.
- Centralized RADIUS servers allow instant revocation, granular policy enforcement (VLAN/ACL), and audit trails – all of which are impossible with PSK-based security.
- This makes 802.1X essential for enterprise, government, and high-security wireless deployments.

---
