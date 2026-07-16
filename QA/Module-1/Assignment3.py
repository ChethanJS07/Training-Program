import time

from scapy.all import ICMP, IP, sr1


def ping(host, count=5, timeout=2):

    success = 0
    rtts = []

    print(f"ping {host} ({host}) {count} packets")

    for i in range(count):

        ip = IP(dst=host)
        icmp = ICMP(id=100, seq=i)
        packet = ip / icmp

        start = time.perf_counter()
        reply = sr1(packet, timeout=timeout, verbose=False)
        end = time.perf_counter()

        if reply is not None:
            rtt = (end - start) * 1000
            success += 1
            rtts.append(rtt)
            print(f"Reply from {reply[IP].src}: seq={i}, time={rtt:.2f} ms")
        else:
            print(f"Request timed out: seq={i}")

    loss_percent = (count - success) / count * 100
    if rtts:
        avg_rtt = sum(rtts) / len(rtts)
        print(f"\n---- {host} ping statistics ----")
        print(
            f"{count} packets transmitted, {success} received, {loss_percent:.1f}% packet loss"
        )
        print(f"Average RTT: {avg_rtt:.2f} ms")
    else:
        print(f"\n---- {host} ping statistics ----")
        print(f"{count} packets transmitted, 0 received, 100.0% packet loss")
        print("No replies received, cannot compute average RTT.")


if __name__ == "__main__":
    ping("1.1.1.1", count=5, timeout=2)
