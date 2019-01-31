import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}



def download_video(url):
    """根据已知回答地址求真实可下载视频地址"""
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    pattern = re.compile(r"https://www.zhihu.com/video/[0-9]{10,}")
    ok = pattern.search(r.text)
    line2 = ok.group(0)
    pattern = re.compile(r"[0-9]{10,}")
    ok = pattern.search(line2)
    str = ok.group(0)
    str = 'https://lens.zhihu.com/api/v4/videos/' + str
    mp4_url = str
    rmp4 = requests.get(mp4_url, headers=headers)
    k = rmp4.text
    km = dict(rmp4.json())
    return km['playlist']['LD']['play_url']
    pass



if __name__ == "__main__":
    while True:
        temp_url = input("请输入知乎回答地址：")
        download_url = download_video(temp_url)
        print(download_url)
        pass
    pass