import os
import re

def clean_url(url):
    # Remove http://, https://, www. and anything after the first /
    url = re.sub(r'https?://(www\.)?', '', url)
    url = url.split('/')[0]
    return url.strip()

def filter_unique_links():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.normpath(os.path.join(script_dir, 'MSlinks.txt'))
    store_path = os.path.normpath(os.path.join(script_dir, 'store.txt'))
    
    # Read stored links
    stored_links = set()
    if os.path.exists(store_path):
        with open(store_path, 'r') as file:
            stored_links = set(line.strip() for line in file)
    
    # Read and clean new links
    with open(input_path, 'r') as file:
        links = [clean_url(link.strip()) for link in file.readlines()]
    
    # Get unique links
    unique_links = set(links) - stored_links
    
    # Print unique links to console
    if unique_links:
        print("New unique links found:")
        for link in unique_links:
            print(link)
    else:
        print("No new unique links found")

if __name__ == "__main__":
    filter_unique_links()
