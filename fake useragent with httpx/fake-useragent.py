import httpx
from random import randint

SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

def get_user_agent_list():
    with httpx.Client() as client:
        response = client.get(f'http://headers.scrapeops.io/v1/user-agents?api_key={SCRAPEOPS_API_KEY}')
        json_response = response.json()
        return json_response.get('result', [])

def get_random_user_agent(user_agent_list):
    random_index = randint(0, len(user_agent_list) - 1)
    return user_agent_list[random_index]

## Retrieve User-Agent List From ScrapeOps
user_agent_list = get_user_agent_list()

url_list = [
  'https://example.com/1',
  'https://example.com/2',
  'https://example.com/3',
]

for url in url_list:

  ## Add Random User-Agent To Headers
  headers = {'User-Agent': get_random_user_agent(user_agent_list)}

  ## Make Requests
  with httpx.Client() as client:
      r = client.get(url=url, headers=headers)
      print(r.text)