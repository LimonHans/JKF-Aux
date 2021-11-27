###############################
#  HansLimon & dixiatielu at  #
#         2021/11/26.         #
#                             #
# Only for educational usage. #
#                             #
#     CopyLEFT Mongrokey®     #
###############################
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from win32api import GetSystemMetrics
from datetime import datetime
import ctypes

systemwidth = GetSystemMetrics(0)
systemheight = GetSystemMetrics(1)
delta_date = 0
try:
    for i in str(datetime(2021, 12, 27) - datetime.now()):
        if i == ' ': break
        else: delta_date = delta_date*10 + int(i)
except: delta_date = 0

image = Image.open("OriginalPIC.png")
image = image.resize((systemwidth, systemheight))
iwidth, iheight = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('simhei.ttf', 148)
file = open("slogan.txt", "r", encoding='utf-8')
nowtext = file.read()
if nowtext[-1] == "\n": nowtext = nowtext[:-1]
file.close()
file = open("config.txt", "r", encoding='utf-8')
divers_1, divers_2 = file.read().split()
file.close()
file = open("color.txt", "r", encoding='utf-8')
textcolor = file.read()
while textcolor[-1] == "\n": textcolor = textcolor[:-1]
file.close()
divers_1 = int(divers_1)
divers_2 = int(divers_2)
print(divers_1)
print(divers_2)
fwidth, fheight = draw.textsize(nowtext, font)
fontx = (iwidth - fwidth - font.getoffset(nowtext)[0])/2
fonty = (iheight - fheight - font.getoffset(nowtext)[1])/2 - iheight/divers_1
draw.text((fontx, fonty), nowtext, textcolor, font)

font = ImageFont.truetype('consola.ttf', 338)
#font = ImageFont.truetype('simsun.ttc', 148)
nowtext = str(delta_date)
fwidth, fheight = draw.textsize(nowtext, font)
fontx = (iwidth - fwidth - font.getoffset(nowtext)[0])/2
fonty = (iheight - fheight - font.getoffset(nowtext)[1])/2 + iheight/divers_2
draw.text((fontx, fonty), nowtext, textcolor, font)

image.save("timer.png")

ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\\HansLimon\\timer.png", 0)