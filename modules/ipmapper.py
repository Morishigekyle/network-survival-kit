import socket

def ipmapper(domain):
    print("The IP address of target is: " + socket.gethostbyname(domain[0]))