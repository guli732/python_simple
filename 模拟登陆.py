import urllib.parse
import urllib.request
import http.cookiejar


cj = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(handler)

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201962711971'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
formdata = {
    'captcha_type': 'web_login',
    'domain': 'renren.com',
    'email': '18406597900',
    'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DF7lJUFCGjc-_-sV4jUwq-gNJKxP3RM9S5m7mUKN-mZC%26wd%3D%26eqid%3Ded1348b20058ac62000000035d2d0a50',
    'icode': '',
    'key_id': '1',
    'origURL': 'http://www.renren.com/home',
    'password': '36563b0374683b573c92eee54ab0675a91c86e861b648c650222402aaa677029',
    'rkey': '2f2945d175992b452b23fcbc2033c9c2',
}
formdata = urllib.parse.urlencode(formdata).encode()
request = urllib.request.Request(url=post_url, headers=headers)
response = opener.open(request, data=formdata)
print(response.read().decode())
print('*' * 50)
get_url = 'http://www.renren.com/971499782/profile'
request = urllib.request.Request(url=get_url, headers=headers)
response = opener.open(request)
with open('模拟登录人人网.html', 'wb') as f:
    f.write(response.read())
print("模拟登录人人网.html导出成功...")