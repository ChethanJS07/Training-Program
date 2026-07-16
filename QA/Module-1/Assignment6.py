#!/usr/bin/env python3

import csv
from datetime import datetime

from scapy.all import ARP, Ether, srp


def detect_duplicates(results):
    ip_mac_map = {}
    for entry in results:
        ip = entry["ip"]
        mac = entry["mac"]
        if ip not in ip_mac_map:
            ip_mac_map["ip"] = []
        ip_mac_map["ip"].append(mac)

    return {ip: macs for ip, macs in ip_mac_map.items() if len(macs) > 1}


def save_to_csv(results, duplicates, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"network_discovery_{timestamp}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["IP", "MAC", "Duplicate"])
        writer.writeheader()
        for entry in results:
            ip = entry["ip"]
            mac = entry["mac"]
            dup = "Yes" if ip in duplicates else "No"
            writer.writerow({"IP": ip, "MAC": mac, "Duplicate": dup})
    return filename


def main():
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst="192.168.31.0/24")

    packet = ether / arp

    answered, unanswered = srp(packet, timeout=2, verbose=False)

    results = []

    for sent, received in answered:
        ip = received.psrc
        mac = received.hwsrc
        results.append({"ip": ip, "mac": mac})
        print(f"Found {ip} at {mac}")

    duplicates = detect_duplicates(results)

    if duplicates:
        print("\nDuplicate IPs detected:")
        for ip, macs in duplicates.items():
            print(f"{ip} has multiple MACs: {', '.join(macs)}")
    else:
        print("\nNo duplicate IPs found.")

    csv_file = save_to_csv(results, duplicates)
    print(f"\nResults saved to {csv_file}")


if __name__ == "__main__":
    main()
