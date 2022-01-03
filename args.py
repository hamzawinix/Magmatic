import sys
def check_mode():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == help :
            mode_args_help()
    else:
        mode = 'i'
    return mode

def mode_args_help():
    print("Magmatic [option]")
    print("For advanced list of options see help")
    print("Args:")
    print("     q, quite")
    print("     i, interactive(default)")
    print("     CD, check_dependencies")

def nmap_args_help():
    print("Magmatic [option]")
    print("For advanced list of options see help")
    print("Args:")
    print('''
            os, os_detection,
            vd, version_detection,
            tp, top_ports,
            db, dns_brute,
            fs, fin_scan,
            is, idle_scan,
            ps, ping_scan,
            sc, syn_scan,
            ts, tcp_scan,
            us, udp_scan
            ''')