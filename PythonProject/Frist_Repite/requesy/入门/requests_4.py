import requests
'''
url = "https://erebor.douban.com/?unit=dale_movie_chart_bottom_banner&bid=cm7X1hC2f2M&crtr=3%3A%2Fchart&ts=1665926978578&callback=erebor_487A6E1A59C749E28DD8224CDF16AA7A&failback_count=1"
url = "https://fundin.douban.com/piwik?action_name=%E8%B1%86%E7%93%A3%E7%94%B5%E5%BD%B1%E6%8E%92%E8%A1%8C%E6%A6%9C&idsite=100001&rec=1&r=478816&h=21&m=47&s=41&url=https%3A%2F%2Fmovie.douban.com%2Fchart&urlref=https%3A%2F%2Fmovie.douban.com%2F&_id=407640df3ea52a74&_idts=1665901237&_idvc=3&_idn=0&_refts=1665926916&_viewts=1665919360&_ref=https%3A%2F%2Fwww.douban.com%2F&cookie=1&res=1620x2160&gt_ms=904"
url = "https://fanyi.baidu.com/langdetect"
'''
url = "https://movie.douban.com/chart"

# 请求头
head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6,2 Safari/605.1.15"
}

resp = requests.get(url, headers=head)
print(resp.text)
resp.close()
print("over")