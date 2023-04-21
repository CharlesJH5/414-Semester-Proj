import dns.resolver
import sys
# Subdomain list sourced from https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt


domain = sys.argv[1]
subdomain_file = open(sys.argv[2], "r+")

def main():
    subdomain_store = []
    subdomain_array = []
    
    i = 0
    
    for fileLine in subdomain_file:
        fileLine = fileLine.rstrip()
        subdomain_array[i] = fileLine
        i += 1
    
    
    for subdoms in subdomain_array:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
            if ip_value:
                subdomain_store.append(f'{subdoms}.{domain}')
                if f'{subdoms}.{domain}' in subdomain_store:
                    print(f'{subdoms}.{domain} valid')
                else:
                    pass
        except dns.resolver.NXDOMAIN:
            print("Subdomain not found!")
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()

main()
