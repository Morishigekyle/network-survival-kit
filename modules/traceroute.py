import subprocess

def traceroute(host_name):
    the_host = str(host_name).strip("[']")
    host = subprocess.call(["traceroute", the_host])
    print(host)
    