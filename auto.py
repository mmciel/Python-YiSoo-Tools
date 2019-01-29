from urllib import request


url = "http://gslb.miaopai.com/stream/Z7vERUMvdMg36uCHJ1vRZxWhXSzLWnQ-paynhw__.mp4?yx=&refer=weibo_app&vend=weibo&label=mp4_hd&mpflag=8&Expires=1548767462&ssig=dXdKkh5eV3&KID=unistore,video"
# 文件的方式保存下载的图片
response = request.urlopen(url)
#读取返回的内容
img = response.read()
with open('temp.mp4','wb') as f:
    #将图片内容以二进制写入
    f.write(img)