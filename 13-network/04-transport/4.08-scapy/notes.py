#!/usr/bin/env python3
# https://python3.info/network/transport/scapy.html


# %% Transport scapy
# %%



# %% Installation
# %%



# %% Running
# %%



# %% Basic usage
# %%



# %% Displays all available protocols
# %%



# %% Lists all command functions
# %%



# %% Reading PCAP files
# - Read packets from a *pcap* file
# - Write packets to a *pcap* file.
# %%



# %% Graphical dumps (PDF, PS)
# %%



# %% Generating sets of packets
# %%



# %% List of possible fields
# %%



# %% IP packages
# - Packets are constructed as layers of protocols, loosely analogous to the *OSI* model, which can be manipulated independently or glued together.
# - IP() object represents an *IPv4* header.
# %%



# %% Create package
# %%



# %% Modify package
# %%



# %% Show package
# %%



# %% TCP Package
# %%



# %% Add TCP layer to IP package
# - Add a layer for protocol by using the division operator
# %%



# %% Ethernet frames
# %%



# %% Sending packets
# %%



# %% OSI layer three
# - send() function if transmitting at layer three (i.e. without a layer two header)
# %%



# %% OSI layer two
# - sendp() function if transmitting at layer two
# - Values for blank fields, such as the source and destination addresses in the Ethernet header, are populated automatically by scapy where possible.
# %%



# %% Send and Receive
# - scapy has the ability to listen for responses to packets it sends, such as *ICMP* echo requests (pings).
# %%



# %% One packet
# - Build an *IP* packet carrying an *ICMP* header
# - Use the sr() (send/receive) function to transmit the packet and record any response
# %%



# %% Many packets
# - Send and listen for responses to multiple copies of the same packet
# - Use the srloop() function and specify a count of packets to send
# %%



# %% SYN Scans
# - SA or SYN-ACK flags indicating an open port.
# %%



# %% Scan one port
# %%



# %% Scan port range
# %%



# %% Advanced examples
# - https://scapy.readthedocs.io/en/latest/usage.html
# %%



