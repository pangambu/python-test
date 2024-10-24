import re
#import csv

url  = input("URL: ").strip()


#username = re.sub("^(https?://)?(www\.)?twitter\.com/","",url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(a-z0-9_)", url, re.IGNORECASE):
     print(f"Username: ",matches.group(1))
    

