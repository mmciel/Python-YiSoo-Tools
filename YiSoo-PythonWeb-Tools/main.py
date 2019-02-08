# coding=utf-8

"""
    name:YiSoo Python Tools
    author:mmciel
    time:2019年1月30日12:45:52
    version：V1.0

    基于Flask构建的一个轻量级服务器；
    功能：
        实现知乎视频的下载
        实现微博视频的下载
        实现网易云音乐的下载
"""
import json
import time
from flask import Flask, render_template, request
import requests
import re
app = Flask(__name__)

'''
    请求：主页面
    返回值：index页面
'''
@app.route('/')
def index():
    return render_template('index.html')

'''
    请求：知乎下载功能
    返回值：
'''
@app.route('/zhihu')
def zhihu():
    return render_template('zhihu.html')

'''
    请求：微博下载功能
    返回值：
'''
@app.route('/weibo')
def weibo():
    return render_template('weibo.html')

'''
    请求：网易云音乐下载功能
    返回值：
'''
@app.route('/yunmusic')
def yunmusic():
    return render_template('yunmusic.html')

'''
    请求：
    返回值：
'''
def set_log(url,file,user):
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(file,'a+',encoding="utf-8") as f:
        f.write("time:"+ timestr+";    url:"+url+";    user:"+user+'\n')

@app.route("/zhihu_data",methods=['POST'])
def zhihu_data():
    zhihu_url_data = request.form.get('zhihu_url_data')
    zhihu_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}
    zhihu_r = requests.get(zhihu_url_data, headers=zhihu_headers)
    zhihu_r.encoding = "utf-8"
    zhihu_pattern = re.compile(r"https://www.zhihu.com/video/[0-9]{10,}")
    ok = zhihu_pattern.search(zhihu_r.text)
    line2 = ok.group(0)
    zhihu_pattern2 = re.compile(r"[0-9]{10,}")
    ok = zhihu_pattern2.search(line2)
    mp4_url = 'https://lens.zhihu.com/api/v4/videos/' + ok.group(0)
    rmp4 = requests.get(mp4_url, headers=zhihu_headers)
    km = dict(rmp4.json())
    download_url =  km['playlist']['LD']['play_url']
    mua = "<script>window.location.href='"+ download_url +"'</script>"
    set_log(zhihu_url_data,r"zhihu_log.txt",request.remote_addr)
    return mua


@app.route("/weibo_data",methods=['POST'])
def weibo_data():
    weibo_url_data = request.form.get('weibo_url_data')
    weibo_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    weibo_r = requests.get(weibo_url_data,headers = weibo_headers)
    weibo_context = weibo_r.text
    weibo_pattern = re.compile(r"\"mp4_hd_mp4\": \".*\"")
    ok = weibo_pattern.findall(weibo_context)
    data = '{' + ok[0] + '}'
    data_dict = json.loads(data)
    download_url = data_dict['mp4_hd_mp4']
    mua = "<script>window.location.href='" + download_url +"'</script>"
    set_log(weibo_url_data, r"weibo_log.txt", request.remote_addr)
    return mua


@app.route("/yun_data",methods=['POST'])
def yun_data():
    yun_url_data = request.form.get('yun_url_data')
    music = yun_url_data
    yun_pattern = re.compile(r"song/[0-9]{2,}")
    ok = yun_pattern.findall(music)
    data = ok[0]
    music_num = data[5:]
    yun_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_num)
    yun_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    yun_r = requests.get(yun_url, headers=yun_headers)
    download_url = yun_r.url
    mua = "<script>window.location.href='" + download_url +"'</script>"
    set_log(yun_url_data, "yunmusic_log.txt", request.remote_addr)
    return mua


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
