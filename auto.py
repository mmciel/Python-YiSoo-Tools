from urllib import request
url = "https://vdn1.vzuu.com/LD/2ccbcdf0-1648-11e9-9501-0a580a44a47f.mp4?disable_local_cache=1&bu=com&expiration=1548426897&auth_key=1548426897-0-0-2a87fbf3f91d376820027a7b02df914a&f=mp4&v=hw"
# 文件的方式保存下载的图片
response = request.urlopen(url)
#读取返回的内容
img = response.read()
with open('temp.mp4','wb') as f:
    #将图片内容以二进制写入
    f.write(img)