import urllib.request
import urllib.parse


img_url = 'https://w.wallhaven.cc/full/ox/wallhaven-oxlo85.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
request = urllib.request.Request(url=img_url, headers=headers)
response = urllib.request.urlopen(request)
with open('1.jpg', 'wb') as f:
    f.write(response.read())