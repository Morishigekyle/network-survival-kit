import subprocess

def macchange(mac_address):
    if (mac_address.random):
        subprocess.call(["ifconfig", "eth0", "down"])
        random = subprocess.call(["macchanger", "-r", "eth0"])
        subprocess.call(["ifconfig", "eth0", "up"])
        subprocess.call(["ifconfig", "eth0"])
    else:
        subprocess.call(["ifconfig", "eth0", "down"])
        change_address = subprocess.call(["macchanger", "-m", mac_address.mac, "eth0"])
        subprocess.call(["ifconfig", "eth0", "up"])
        subprocess.call(["ifconfig", "eth0"])
