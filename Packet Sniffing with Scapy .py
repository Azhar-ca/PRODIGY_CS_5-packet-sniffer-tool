#python
from scapy.all import sniff

# Callback function to process each packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

# Start sniffing on the network
sniff(prn=packet_callback, count=10)  # capture 10 packets for testing

#This captures packets and prints the source IP, destination IP, and protocol number.
