import subprocess
import ipaddress

def pingsweep(ip_address):
        if "/" in str(ip_address):
                target_ip = str(ip_address).strip("[']")
                cidr = ipaddress.ip_network(target_ip)
                for x in cidr:
                        y = "fping -a -C 5 -q " + str(x)
                        print(subprocess.getstatusoutput(y))
        else:
                first_ip = ip_address[0]
                second_ip = ip_address[1]
                start_ip = ipaddress.IPv4Address(first_ip)
                end_ip = ipaddress.IPv4Address(second_ip)
                for ip_int in range(int(start_ip), int(end_ip)):
                        ip = ipaddress.IPv4Address(ip_int)
                        ip_is_str = str(ip)
                        command = subprocess.Popen(["fping", "-a", "-C 5", "-q", ip_is_str], stderr = subprocess.PIPE, stdout = subprocess.PIPE)
                        output = command.stderr.read()
                        the_ip_address = output.decode().split(" : ")[0]
                        the_response = output.decode().split(" : ")[1]
                        print(the_ip_address + " : " + the_response)
        
    

