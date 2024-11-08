def packet_callback(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        payload = packet['Raw'].load if packet.haslayer('Raw') else "No payload"
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Payload: {payload}")
