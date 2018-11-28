#!/usr/bin/env python
import argparse
import modules.pingsweep as ps
import modules.traceroute as tr
import modules.portscan as ports

def pingsweep(args):
    ps.pingsweep(args.ip)  

def traceroute(args):
    tr.traceroute(args.target)

def portscan(args):
    ports.portscan(args.host)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "Network Survival Kit", description = "Command line netwok toolkit")

    # parser.add_argument("ip", nargs = 1, default = "127.0.0.1", help = "Target IP address")
    # parser.add_argument("--port", "-p", type = int)
    # parser.add_argument("--protocol", "-P", nargs = "?", default = "tcp", choices = ["tcp", "udp", "icmp"])
    parser.add_argument("--output", "-o", nargs = 1, help = "File name to write results")
    
    subparsers = parser.add_subparsers(help = "Module specific utilities")

    parser_pingsweep = subparsers.add_parser("pingsweep", help = "Perform network ping sweep")
    parser_pingsweep.add_argument("ip", nargs = "+", help = "Target IP address")
    # parser_pingsweep.add_argument("--range", "-r", nargs = 2, help = "Range between two IP addresses (10.0.0.1 10.0.0.5")
    parser_pingsweep.set_defaults(func = pingsweep)

    parser_traceroute = subparsers.add_parser("traceroute", help = "Track hops from host to target")
    parser_traceroute.add_argument("target", nargs = 1, help = "Target host to trace path")
    parser_traceroute.set_defaults(func = traceroute)

    parser_portscan = subparsers.add_parser("portscan", help = "Scan for open ports")
    parser_portscan.add_argument("host", nargs = 1, help = "Target host to scan")
    # parser_portscan.add_argument("ports", nargs = 1, help = "Target ports to scan")
    parser_portscan.set_defaults(func = portscan)

    args = parser.parse_args()
    args.func(args)
    print("Arguments: {}".format(args))

