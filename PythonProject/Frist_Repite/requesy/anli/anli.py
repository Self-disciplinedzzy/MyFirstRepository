import re
import requests

url = "https://www.iqiyi.com/ranks1/1/0"
head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
}
man = re.compile(r'</i>.*?div class="rvi titi" data-v-03e11944>(?P<name>.*?)</div>.*?<span>', re.S)

resp = requests.get(url, headers=head)
resp_content = resp.text

result = man.finditer(resp_content)

for i in result:
    print(result.group("name"))
resp.close()
print("over")
