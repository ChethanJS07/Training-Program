#!/usr/bin/env python3

import csv
import os
import time
from datetime import datetime

from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoAuthenticationException, NetMikoTimeoutException

netmiko_exceptions = (NetMikoTimeoutException, NetMikoAuthenticationException)

CSV_FILE = "devices.csv"
LOG_DIR = "device_logs"
RETRY_DELAY = 2
RETRY_COUNT = 3

os.makedirs("device_logs", exist_ok=True)


COMMANDS = {
    "cisco_ios": ["show version", "show ip interface brief"],
    "linux": ["whoami", "hostnamectl"],
}


def save_command_output(host, command, output):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_cmd = command.replace(" ", "_")
    filename = f"{LOG_DIR}/{host}_{safe_cmd}_{timestamp}.log"
    with open(filename, "w") as f:
        f.write(f"Command: {command}\n")
        f.write(f"Device: {host}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("-" * 80 + "\n\n")
        f.write(output)
    return filename


def connect_with_retry(device):
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            return ConnectHandler(**device), None
        except netmiko_exceptions as e:
            if attempt == RETRY_COUNT:
                return None, str(e)
            time.sleep(RETRY_DELAY)
        except Exception as e:
            return None, f"Unexpected error: {e}"
    return None, "Max retries exceeded"


def main():
    start_time = time.time()
    success_list = []
    failed_list = []

    try:
        with open(CSV_FILE, "r") as file:
            devices = list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found.")
        return

    for device in devices:
        host = device.get("host")
        device_type = device.get("device_type", "linux")
        commands = COMMANDS.get(device_type, [])

        if not commands:
            failed_list.append({"host": host, "reason": "No commands defined"})
            continue

        print(f"\nConnecting to {host} (type: {device_type})...")
        connection, error = connect_with_retry(device)
        if connection is None:
            print(f"Connection failed: {error}")
            failed_list.append({"host": host, "reason": error})
            continue


        log_files = []
        for cmd in commands:
            try:
                output = connection.send_command(cmd)
                log_file = save_command_output(host, cmd, output)
                log_files.append(log_file)
                print(f"{cmd} → saved")
            except Exception as e:
                print(f"Command '{cmd}' failed: {e}")
                log_files.append(None)
        connection.disconnect()
        success_list.append({"host": host, "log_files": log_files})

    elapsed = time.time() - start_time
    report_file = f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, "w") as f:
        f.write("=" * 80 + "\n")
        f.write("DEVICE HEALTH COLLECTOR – SUMMARY REPORT\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Total execution time: {elapsed:.2f} seconds\n")
        f.write("-" * 80 + "\n")
        f.write(f"Total devices: {len(devices)}\n")
        f.write(f"Successful: {len(success_list)}\n")
        f.write(f"Failed: {len(failed_list)}\n\n")
        if failed_list:
            f.write("FAILED CONNECTIONS:\n")
            for entry in failed_list:
                f.write(f"  - {entry['host']}: {entry['reason']}\n")
            f.write("\n")
        if success_list:
            f.write("SUCCESSFUL CONNECTIONS:\n")
            for entry in success_list:
                f.write(f"  - {entry['host']}\n")
                if entry["log_files"]:
                    for log in entry["log_files"]:
                        if log:
                            f.write(f"      • {os.path.basename(log)}\n")
                f.write("\n")
        f.write("=" * 80 + "\n")
        f.write(f"All logs stored in: {LOG_DIR}/\n")

    print(f"\nSummary report saved to {report_file}")


if __name__ == "__main__":
    main()
