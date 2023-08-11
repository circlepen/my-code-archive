from bs4 import BeautifulSoup
import requests
import shutil
keyword = input('關鍵字？')
response = requests.get(
    f'https://www.google.com/search?q={keyword}&sxsrf=ALeKk00A5k-jgd_HsveNZlrbNfcuZf8x2Q:1607744304588&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0maihwsftAhWwGqYKHUohC6sQ_AUoAXoECAUQAw&biw=1366&bih=625')
soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.find_all('img')
tag
# 在當前目錄開一個檔案,
# (檔名, 開啟模式 w,r,a)

count = 0
Newimg = Image.new('RGB', (512, 1024), (255, 255, 255))
x = 0
y = 0
for i in tag[1:]:
    # print(i['src'])
    count += 1
    url = i['src']
    response = requests.get(url, stream=True)
    # 讀取圖片

    img = Image.open(response.raw)

    size = (128, 256)
    img.thumbnail(size)
    Newimg.paste(img, (x, y))
    x += 128
    if x >= 512:
        y += 128
        x = 0

Newimg
