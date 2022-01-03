import pkg_resources
import subprocess
import sys
from pyfiglet import Figlet

def check_pkg():
    required_pkg =['nmap','pyfiglet','random2']
    notinstalled =[]
    for package in required_pkg:
        try:
            dist = pkg_resources.get_distribution(package)
            
            
            print('{} ({}) is installed'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{} is NOT installed'.format(package))
            notinstalled.append(package)

    for pkg in notinstalled:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

def cool_ascii():
    art = ["Magmatic"]
    fonts = []
    custom_fig = Figlet(random.choice(fonts))
    print(custom_fig.renderText(art[0]))

check_pkg()
cool_ascii()
# for i in required:

#     try:
#         import i
#         print("module "+i" is installed")
#     except ModuleNotFoundError:
#         print("module 'mutagen' is not installed")
#         # or
#         install("mutagen") # the install function from the ques


# import sys as s

# mod = s.modules.keys()
# for i in mod.modules:
#     if i ==

# nmap_scan = nmap.PortScanner()
# nmap_scan.scan("10.10.137.236","0-1000")
# 
