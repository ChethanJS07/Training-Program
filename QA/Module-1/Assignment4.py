#!/usr/bin/env python3

import re
from datetime import datetime

LOG_FILE = "compliance_audio.log"


def read_config_file(filename="running_config.txt"):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None


def check_snmp(config):
    pattern = re.compile(r"^snmp-server community (\S+)", re.IGNORECASE | re.MULTILINE)
    communities = pattern.findall(config)
    if not communities:
        return "PASS: SNMP disabled (no communities found)"
    insecure = [c for c in communities if c.lower() in ("public", "private")]
    if insecure:
        return f"FAIL: Insecure communities found: {', '.join(insecure)}"
    else:
        return f"REVIEW: SNMP enabled with custom communities: {', '.join(communities)}"


def check_telnet(config):
    pattern = re.compile(r"transport input\s+(.*)", re.IGNORECASE)
    matches = pattern.findall(config)
    if not matches:
        return "PASS: No transport input found (Telnet disabled)"
    for line in matches:
        if "telnet" in line.lower():
            return f"FAIL: Telnet enabled on line: {line}"
    return "PASS: Telnet not found in transport input lines"


def check_ssh(config):
    pattern = re.compile(r"transport input\s+(.*)", re.IGNORECASE)
    transports = pattern.findall(config)
    ssh_enabled = any("ssh" in line.lower() for line in transports)

    version_pattern = re.compile(r"ip ssh version 2", re.IGNORECASE)
    version_set = bool(version_pattern.search(config))

    if not ssh_enabled:
        return "FAIL: SSH not enabled on VTY lines"
    if not version_set:
        return "REVIEW: SSH enabled, but version 2 not configured"
    return "PASS: SSH enabled with version 2"


def check_banner(config):
    pattern = re.compile(r"banner motd \^C\n(.*?)\n\^C", re.DOTALL | re.IGNORECASE)
    match = pattern.search(config)
    if not match:
        return "FAIL: No MOTD banner configured"
    banner_text = match.group(1)
    keywords = ["unauthorized", "monitored", "prohibited", "warning", "legal"]
    found = [kw for kw in keywords if kw in banner_text.lower()]
    if found:
        return f"PASS: Banner contains warnings: {', '.join(found)}"
    return "REVIEW: Banner exists but missing security warnings"


def main():
    config = read_config_file()
    if config is None:
        return

    results = {
        "SNMP": check_snmp(config),
        "Telnet": check_telnet(config),
        "SSH": check_ssh(config),
        "Banner": check_banner(config),
    }

    print("\n--- Compliance Check Results ---")
    for check, result in results.items():
        print(f"{check}: {result}")

    report = "=" * 80 + "\n"
    report += "COMPLIANCE CHECK REPORT\n"
    report += f"Generated: {datetime.now().isoformat()}\n"
    report += "=" * 80 + "\n\n"
    for check, result in results.items():
        report += f"{check}: {result}\n"
    report += "\n" + "=" * 80 + "\n"

    with open(LOG_FILE, "w") as f:
        f.write(report)

    print(f"\nResults saved to {LOG_FILE}")


if __name__ == "__main__":
    main()
