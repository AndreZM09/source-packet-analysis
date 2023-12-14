from scapy.all import sniff
from pyx import *

def packet_callback(packet):
    print(packet.show())
    
# sniff(filter="tcp", prn=packet_callback,count=1)

p=sniff(prn=packet_callback,count=1)
# print(p.show())
print(p.hexdump())
p.pdfdump("prueba.pdf")
print(pyxinfo)

