import requests
import re
from urllib import request
music = "分享李荣浩的单曲《年少有为》: http://music.163.com/song/1293886117/?userid=495697406 (来自@网易云音乐)"
#pattern = re.compile(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)")
pattern = re.compile(r"song/[0-9]{2,}")
ok = pattern.findall(music)
lennum = len(ok)
data = ok[0]
music_num = data[5:]

pattern2 = re.compile(r"《(.*)》")
ok = pattern2.findall(music)
musicname = ok[0]+".mp3"

#print(music_num)
url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_num)
print(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
r = requests.get(url,headers=headers)



#print(r.url)
download_url = r.url

mp3 = request.urlopen(download_url)
img = mp3.read()
with open(musicname,'wb') as f:
    #将图片内容以二进制写入
    f.write(img)

