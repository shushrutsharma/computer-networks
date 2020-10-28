import scapy.all as scapy
import os

def scan(ip):
    arp_req_frame = scapy.ARP(pdst = ip)
    print(scapy.ls(scapy.ARP()))

    broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        client_dict = {"ip" : answered_list[i][1].psrc, "mac" : answered_list[i][1].hwsrc}
        result.append(client_dict)

    return result

ip = ""

while ip != "exit":
    ip = input("\nEnter IP address [or exit]: ")
    if ip == "exit":
        continue
    os.system("ping {}".format(ip))
    msg = input("\nRetrieve MAC address? [y/n]: ")
    if msg == "n":
        continue
    print("\nSending request:")
    result = scan(ip)
    if result != []:
        print("\nMAC address for {0} is {1}".format(ip, result[0]['mac']))
    else:
        print("Couldn't retreive hwdst")
print("\nExiting")