import web
import requests
import re
import json
import time

urls = (
    '/hello/(.*)', 'hello',
    '/zhihu','ok'
)

app = web.application(urls, globals())
# url='https://www.zhihu.com/answer/571159853?1066866516753981440'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
def get_mp4(url):
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    pattern = re.compile(r"https://www.zhihu.com/video/[0-9]{10,}")
    ok = pattern.search(r.text)
    line2 = ok.group(0)
    pattern = re.compile(r"[0-9]{10,}")
    ok = pattern.search(line2)
    str = ok.group(0)
    # print(str)
    str = 'https://lens.zhihu.com/api/v4/videos/' + str

    mp4_url = str
    # print(mp4_url)
    rmp4 = requests.get(mp4_url, headers=headers)
    # print(rmp4.text)
    # print(rmp4.json())
    k = rmp4.text
    # print(rmp4.json())
    km = dict(rmp4.json())
    # print(km)
    # print("=================")
    # print(km['playlist']['LD']['play_url'])
    download_url = km['playlist']['LD']['play_url']
    return download_url
    pass
def set_log(url):
    file = r'下载日志.txt'
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(file,'a+') as f:
        f.write("time:"+ timestr+";url:"+url+'\n')
class hello:
    def GET(self, data):
        if not data:
            return
        # 获取正常链接
        url = data
        set_log(url)
        link = get_mp4(url)
        # print(link)
        # return str(link)
        str = '<html><head></head><body><h1><a href="'+link+'">open video</a> </h1></body></html>'
        return str

class ok:
    def GET(self):
        htmlf=open('index.html','r',encoding="utf-8")
        htmlcont=htmlf.read()
        # print(type(htmlcont))
        return htmlcont
if __name__ == "__main__":
    app.run()