from typing import cast

import nmap

import args

'''
os detect : os  
version detect : vd

'''

def custom_arg(ip,arg):
   nmap = nmap3.Nmap()
   results = nmap.scan_top_ports(ip, arg)

def nmap_scan(scan_option,ip):
    nm =  nmap3.Nmap()
    ns = nmap3.NmapScanTechniques()
    try:
        return {
            'default' : args.nmap_args_help,
            'os': nm.nmap_os_detection(ip),
            'vd': nm.nmap_version_detection(ip),
            'tp': nm.scan_top_ports(ip),
            'db': nm.nmap_dns_brute_script(ip),
            'fs': ns.nmap_fin_scan(ip),
            'is': ns.nmap_idle_scan(ip),
            'ps': ns.nmap_ping_scan(ip),
            'sc': ns.nmap_syn_scan(ip),
            'ts': ns.nmap_tcp_scan(ip),
            'us': ns.nmap_udp_scan(ip)

        }[scan_option]
    except KeyError:
        return 'default'
    

 
    
    


    
    