#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys


def run_iperf(server, port=5201, duration=10, reverse=False):
    cmd = ["iperf3", "-c", server, "-p", str(port), "-t", str(duration), "-J"]
    if reverse:
        cmd.append("-R")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"iPerf3 error: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("iperf3 not found. Please install iperf3.")
        sys.exit(1)


def extract_metrics(data):
    end = data.get("end", {})
    summary = end.get("sum_sent") or end.get("sum_received")
    if not summary:
        raise ValueError("No summary found in iPerf output")
    avg_bps = summary.get("bits_per_second", 0)
    retransmits = summary.get("retransmits", 0)
    duration_secs = summary.get("seconds", 0)
    return avg_bps, retransmits, duration_secs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("server", help="iPerf3 server IP or hostname")
    parser.add_argument("-p", "--port", type=int, default=5201)
    parser.add_argument("-t", "--duration", type=int, default=10)
    parser.add_argument("-R", "--reverse", action="store_true")
    parser.add_argument(
        "--threshold", type=float, default=800, help="Threshold in Mbps"
    )
    args = parser.parse_args()

    data = run_iperf(args.server, args.port, args.duration, args.reverse)
    avg_bps, retransmits, duration = extract_metrics(data)
    avg_mbps = avg_bps / 1e6

    print(f"Test duration: {duration:.2f} seconds")
    print(f"Average bandwidth: {avg_mbps:.2f} Mbps")
    print(f"Total retransmissions: {retransmits}")

    if avg_mbps >= args.threshold:
        print(f"✅ PASS – bandwidth ({avg_mbps:.2f} Mbps) >= {args.threshold} Mbps")
        sys.exit(0)
    else:
        print(f"❌ FAIL – bandwidth ({avg_mbps:.2f} Mbps) < {args.threshold} Mbps")
        sys.exit(1)


if __name__ == "__main__":
    main()
