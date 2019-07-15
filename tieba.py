import os
import urllib.parse
import urllib.request


def main():

    while True:
        tieba_url = 'http://tieba.baidu.com/f?'
        name = input("请输入贴吧的名称(输入q退出):")
        if name == 'q':
            break
        else:
            num = int(input("请输入要爬取的页数:"))
            page = 1
            for i in range(num):
                data = {
                    'kw': name,
                    'ie': 'utf-8',
                    'pn': (page - 1) * 50
                }
                data = urllib.parse.urlencode(data)
                tieba_url = tieba_url + data
                response = urllib.request.urlopen(tieba_url)
                if not os.path.exists(name):
                    os.mkdir(name)
                print("开始爬取第%d页..." % page)
                with open(name + '/' + name + '_' + str(page) + '.html', 'wb') as f:
                    f.write(response.read())
                page += 1
    

if __name__ == "__main__":
    main()