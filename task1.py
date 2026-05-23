from scapy.all import sniff, IP, TCP, UDP

# Function to process each captured packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        # Identify protocol type
        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        else:
            protocol = str(proto)

        print(f"\n[+] Packet Captured:")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")

        # Show payload if available
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
            if payload:
                print(f"Payload: {payload[:50]}...")  # Show first 50 bytes

# Start sniffing (requires admin/root privileges)
print("Starting packet capture... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=10)  # Capture 10 packets for demo
