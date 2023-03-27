import requests
import random

sites = ['http://google.com', 'http://facebook.com', 'http://twitter.com', 'http://amazon.com', 'http://apple.com']
site = random.choice(sites)

response = requests.get(site)
status_code = response.status_code
site_name = site
html_length = len(response.text)
print(f"Site: {site_name}")
print(f"Status code: {status_code}")
print(f"HTML length: {html_length}")