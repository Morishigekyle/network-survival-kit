import subprocess

def portscan(host_address):
    open_ports = subprocess.call(["nmap", host_address[0]])

