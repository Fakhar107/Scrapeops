import httpx

retry_strategy = httpx.Retry(
    total=3,  # Total number of retries (including the initial request)
    status_forcelist=[500, 502, 503, 504],  # HTTP status codes to retry
    backoff_factor=0.5,  # Factor by which the delay increases after each retry
    method_whitelist=["GET"],  # HTTP methods to retry
)

def make_request():
    url = "http://quotes.toscrape.com/"
    with httpx.Client() as client:
        response = client.get(url, retry=retry_strategy)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Make request
data = make_request()
if data is not None:
    print(data)
else:
    print("Request failed after retries.")