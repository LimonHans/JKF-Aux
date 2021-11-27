###############################
#  HansLimon & dixiatielu at  #
#         2021/11/26.         #
#                             #
# Only for educational usage. #
#                             #
#     CopyLEFT Mongrokey®     #
###############################
import requests as req
import json
from io import BytesIO
from PIL import Image

j = req.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
url = 'https://cn.bing.com/' + json.loads(j.content)['images'][0]['url']
OriginalPIC = req.get(url).content

bytes_stream = BytesIO(OriginalPIC)
roiimg = Image.open(bytes_stream)

imgByteArr = BytesIO()
roiimg.save(imgByteArr,format('PNG'))
imgByteArr = imgByteArr.getvalue()

with open('OriginalPIC.png', 'wb') as fp:
    fp.write(imgByteArr)