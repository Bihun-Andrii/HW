import requests
import random

sites = ['https://google.com/', 'https://facebook.com/', 'https://twitter.com/', 'https://amazon.com/',
         'https://apple.com/']

site = random.choice(sites)

res = requests.get(site)
status_code = res.status_code
site_name = site
html_length = len(res.text)

print(f"Site: {site_name}")
print(f"Status code: {status_code}")
print(f"HTML length: {html_length}")
