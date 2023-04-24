#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
from scapy.all import *
import concurrent.futures
import nmap
from utils import ip_list_generator

# Define una funci¢n para enviar trazas ICMP a una direcci¢n IP
def send_ping(ip):
    # Construye un paquete ICMP con la direcci¢n IP de destino
    packet = IP(dst=ip)/ICMP()

    # Env¡a el paquete ICMP y espera la respuesta
    reply = sr1(packet, timeout=1, verbose=0)

    # Si la respuesta es recibida, devuelve True
    if reply:
        return True

# Define una funci¢n para verificar si un puerto est  abierto en una direcci¢n IP
def check_port(ip, port):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=ip, arguments='-p {}'.format(port))
    if result['scan'][ip]['tcp'][port]['state'] == 'open':
        return True
    else:
        return False


# Define una lista de direcciones IP
ip_list = ip_list_generator()

# Crea un ThreadPoolExecutor con hasta 10 hilos
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Env¡a trazas ICMP a todas las direcciones IP en la lista
    future_to_ip = {executor.submit(send_ping, ip): ip for ip in ip_list}

    # Imprime la lista de direcciones IP con tags verdes para los que devolvieron trazas ICMP y tienen el puerto 80 abierto
    for future in concurrent.futures.as_completed(future_to_ip):
        ips_ok = [] 
        ip = future_to_ip[future]
        if future.result() and check_port(ip, 80):
            with open("ips_ok.txt", "a") as file:
                file.write(ip + "\n")
            print(ip + " \033[1;32;40m [OK] \033[0m")
        else:
            print(ip)

        