import requests
url= "https://movie.douban.com/j/search_subjects?"


head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
}

resp = requests.get(url, headers=head)
print(resp.text)
resp.close()