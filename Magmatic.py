from pyfiglet import main
from pkg_check import *
from ascii import * 
from args import *
from nmap_methods import *

n = len(sys.argv)

def main():

    mode = check_mode()
    cool_ascii()
    mode_args_help()
    print(nmap_scan('ps',"127.0.0.1"))


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()