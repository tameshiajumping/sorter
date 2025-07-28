import dns.resolver
import sys

def check_mx_records(domain, microsoft_patterns):
    try:
        resolver = dns.resolver.Resolver()
        mx_records = resolver.resolve(domain, 'MX')
        
        for mx in mx_records:
            mx_host = str(mx.exchange).lower().rstrip('.')
            for pattern in microsoft_patterns:
                if pattern in mx_host:
                    print(f"✓ Found Microsoft pattern in {domain}: {mx_host}")
                    return True
        return False
    except Exception as e:
        print(f"× Failed to check MX records for {domain}: {str(e)}")
        return False

def main():
    microsoft_patterns = [
        'outlook.com', 'office365.com', 'microsoft.com', 'microsoftonline.com',
        'hotmail.com', 'msn.com', 'exchange.microsoft.com', 'sharepoint.com',
        'azure.com', 'onmicrosoft.com', 'skype.com', 'teams.microsoft.com',
        'mail.protection.outlook.com', 'protection.outlook.com', 'mail.microsoft.com',
        'outbound.protection.outlook.com', 'cloudapp.net', 'trafficmanager.net',
        'windows.net', 'azureedge.net', 'msecnd.net'
    ]

    microsoft_domains = []  # List to collect Microsoft domains
    
    print("Starting Microsoft domain check...")
    try:
        with open('unsorted.txt', 'r') as f:
            domains = f.read().strip().split()
            
        print(f"Found {len(domains)} domains to check\n")
        
        for domain in domains:
            if check_mx_records(domain, microsoft_patterns):
                print(f"✓ {domain} uses Microsoft services\n")
                microsoft_domains.append(domain)
            else:
                print(f"× {domain} does not use Microsoft services\n")
        
        # Display summary at end
        if microsoft_domains:
            print("\n=== MICROSOFT AFFILIATED DOMAINS ===")
            for domain in microsoft_domains:
                print(domain)
            print("================================")
        else:
            print("\nNo Microsoft affiliated domains found.")
                
    except FileNotFoundError:
        print("Error: unsorted.txt not found in current directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
