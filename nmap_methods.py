from typing import cast

import nmap3

import args

'''
os detect : os  
version detect : vd

'''
# def os_detection(ip):
#     nmap = nmap3.Nmap()
#     os_results = nmap.nmap_os_detection(ip)
#     return os_detection

# def version_detection(ip):
#     nmap = nmap3.Nmap()
#     version_result = nmap.nmap_version_detection(ip)

# def top_ports(ip):
#     nmap = nmap3.Nmap()
#     results = nmap.scan_top_ports(ip)

# def dns_brute(ip):
#     nmap = nmap3.Nmap()
#     results = nmap.nmap_dns_brute_script(ip)

# def fin_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.nmap_fin_scan(ip)

# def idle_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.map_idle_scan(ip)

# def ping_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.nmap_ping_scan(ip)

# def syn_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.nmap_syn_scan(ip)

# def tcp_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.nmap_tcp_scan(ip)

# def udp_scan(ip):
#     nmap = nmap3.NmapScanTechniques()
#     result = nmap.nmap_udp_scan(ip)

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
    

 
    
    


    
    