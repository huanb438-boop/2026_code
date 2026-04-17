import requests

url = 'https://gs.bigc.edu.cn/yjszs/2025nzs/b092c202e9d44578a9b6614f1ac890f4.htm'
#url = 'https://blog.51cto.com/u_16175472/9441720'
response = requests.get(url)
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())  # 打印解析后的 HTML
download_count_span = soup.find('span', {'class': 'download-count'})


if download_count_span is not None:
    download_count = download_count_span.text
else:
    print("下载计数未找到")
    download_count = None  # 或者其他的默认值

#download_count = soup.find('span', {'class': 'download-count'}).text