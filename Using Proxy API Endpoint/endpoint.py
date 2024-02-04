import httpx
from urllib.parse import urlencode

payload = {'api_key': 'APIKEY', 'url': 'https://httpbin.org/ip'}
r = httpx.get('https://proxy.scrapeops.io/v1/', params=urlencode(payload))
print (r.text)