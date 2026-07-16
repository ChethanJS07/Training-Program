from scapy.all import ARP, DNS, DNSQR, ICMP, IP, TCP, UDP, Ether, Raw

# ICMP packet (ping)
ping = IP(dst="8.8.8.8") / ICMP()

# TCP syn packet
tcp_syn = IP(dst="8.8.8.8") / TCP(dport=80, flags="S")

# UDP packet with payload
udp_payload = (
    IP(dst="1.1.1.1") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="google.com"))
)

# Ethernet frame with ARP request
ethernet_arp = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.0/24")

# Custom data
custom_packet = IP(dst="1.1.1.1") / TCP(dport=12345) / Raw(load="hello world")

# set specific fields
custom_ip = IP(src="1.2.3.4", dst="1.1.1.1", ttl=64) / ICMP(type=8, code=0)
