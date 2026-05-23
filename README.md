
task1.py is a simple network packet sniffer that captures and displays basic IP packet details using `scapy`.
### Features
- Captures network traffic
- Prints source/destination IP addresses
- Detects TCP/UDP protocol
- Shows first 50 bytes of payload for TCP/UDP packets
- Captures 10 packets by default

### Requirements
- Python 3.x
- `scapy`

### Installation
Install `scapy` with pip:

```bash
pip install scapy
```

### Usage
Run the script with elevated privileges:

```bash
python task1.py
```

### Notes
- Packet capture usually requires administrator/root permissions.
- The script currently stops after capturing 10 packets for demo purposes.
- You can modify `count=10` in `sniff(...)` if you want to capture more packets.
