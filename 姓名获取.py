import requests
import re

url = 'http://www.resgain.net/xmdq.html'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

html = requests.get(url=url,headers=header).text
reg = r'<a class="btn btn2" href="(.*?)" title="	.*?姓名字大全共有.*?姓名字.*?个\
">.*?姓名字大全</a>'
reg = re.compile(reg)
name_url_divdeby_xings = re.findall(reg,html)
for name_url_divdeby_xing in name_url_divdeby_xings:
    url = 'http:' + name_url_divdeby_xing
    url_list = url.split('')