import requests
import re
import json
from urllib import request

'''测试用的url'''
# url = "https://m.weibo.cn/status/4333134420427531?#&video"
url = "https://m.weibo.cn/1949112803/4333794821577074"
# url = "https://m.weibo.cn/s/video/index?object_id=1034:4335969856590352&segment_id=&blog_mid=4335973183689317"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
r = requests.get(url)

'''获取页面数据'''
t = r.text
'''分析页面可以得到关于视频资源的列表'''
pattern = re.compile(r"\"mp4_hd_mp4\": \".*\"")
ok = pattern.findall(t)
data = '{'+ok[0]+'}'
data_dict = json.loads(data)
# print(data_dict)
s = data_dict['mp4_hd_mp4']
print(s)
# 文件的方式保存
response = request.urlopen(s)
# 读取返回的内容
img = response.read()
with open('temp.mp4','wb') as f:
    # 将图片内容以二进制写入
    f.write(img)