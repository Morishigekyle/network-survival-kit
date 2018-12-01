import socket

def sysinfo(sys_info):
    print("The hostname is: " + socket.gethostname())
