import pkg_resources
import subprocess
import sys
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
