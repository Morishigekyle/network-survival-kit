import subprocess

def portscan(host_address):
    if host_address.tcpport:
        tcp_ports = subprocess.call(["nmap", "-p", "1-65535", "-sV", "-sS", "-T4", host_address.host])
    else:
        open_ports = subprocess.call(["nmap", host_address.host])

