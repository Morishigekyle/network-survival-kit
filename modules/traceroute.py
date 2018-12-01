import subprocess

def traceroute(host_name):
    if (host_name.tcproute):
        tcp_route = subprocess.call(["traceroute", "-T", "-p", "80", host_name.target])
    else:
        host = subprocess.call(["traceroute", host_name.target])
        
    