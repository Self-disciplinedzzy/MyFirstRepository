import requests
url = "https://pic.netbian.com/e/member/login/loginjs.php?t=0.7919723524019059"
resp = requests.get(url) 
resp = resp.text
print(resp)