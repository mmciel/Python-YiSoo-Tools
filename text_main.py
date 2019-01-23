import requests
import re
import json

# 随便找一个测试的链接
url = 'https://www.zhihu.com/answer/571159853?1066866516753981440'
# 构造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# 发送get请求并设置编码为utf-8
r = requests.get(url, headers=headers)
r.encoding = "utf-8"
# 编译一个正则表达式
pattern = re.compile(r"https://www.zhihu.com/video/[0-9]{10,}")
# 在get到的页面中匹配正则（只要有视频这个是百分百被匹配的）
ok = pattern.search(r.text)
# 获取匹配结果
line2 = ok.group(0)
# 再次编译一个正则
pattern = re.compile(r"[0-9]{10,}")
ok = pattern.search(line2)
str = ok.group(0)
# print(str)
# 此时的str获取了需要被下载视频的编号
# 通过抓包分析得到真实的视频地址被跳转到如下
str = 'https://lens.zhihu.com/api/v4/videos/'+str

# 向真实地址发送请求
mp4_url = str
# print(mp4_url)
rmp4 = requests.get(mp4_url,headers = headers)
# print(rmp4.text)
# print(rmp4.json())
k = rmp4.text
# print(rmp4.json())
# 获取其中的json数据包，转化为字典
km = dict(rmp4.json())
# print(km)
# print("=================")
# print(km['playlist']['LD']['play_url'])
# 得到视频的播放地址，可通过任意浏览器进行下载
download_url = km['playlist']['LD']['play_url']


print("下载地址为：")
print(download_url)