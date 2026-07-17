#!/usr/bin/env python3

import json
import subprocess
import sys

cmd = ["iperf3", "-c", "127.0.0.1", "-t", "5", "-J"]
JSON_OUTPUT = "iperf3_output.json"
THRESHOLD = 800.0


def main():
    server = cmd[2]
    print(f"Running iperf3 on {server}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("[CRITICAL ERROR] iPerf3 execution failed!")
        print(f"Details: {result.stderr.strip()}")
        sys.exit(1)

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("[CRITICAL ERROR] Failed to decode iPerf3 JSON payload output.")
        sys.exit(1)

    with open(JSON_OUTPUT, "w") as f:
        json.dump(data, f)

    avg_bandwidth = data["end"]["sum_sent"]["bits_per_second"] / 1000000
    test_duration = data["end"]["sum_sent"]["seconds"]
    retransmissons = data["end"]["sum_sent"]["retransmits"]

    print("Average Bandwidth: ", avg_bandwidth, "Mbps")
    print("Test Duration: ", test_duration, "sec")
    print("Retransmissions: ", retransmissons)

    print(f"Json Output saved in {JSON_OUTPUT} file...")

    print("=" * 50)
    if avg_bandwidth < THRESHOLD:
        print(
            f"[FAIL] Performance SLA Breach! Throughput dropped below {THRESHOLD} Mbps."
        )
        print("=" * 50)
        sys.exit(1)
    else:
        print("[PASS] Performance meets SLA metrics criteria.")
    print("=" * 50)


if __name__ == "__main__":
    main()
