# FuckAV
## [中文](https://github.com/iframepm/FuckAV/main/README.md) [English](https://github.com/iframepm/FuckAV/blob/main/English_readme.md)

[![Travis](https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.2-red)](1)  [![Travis](https://img.shields.io/badge/Time-9--13-brightgreen)](1)  [![Travis](https://img.shields.io/badge/python-3.6-brightgreen)](1)

农民工写的免杀工具，2021-9-13
 1frame  1046141213@qq.com
## 更新记录
### 时间 2021-9-13 版本：1.2
1. shellcode加载方式由远程加载改为了本地加载，shellcode写死在了exe里面，因为远程加载太麻烦，点开直接上线更方便，现在直接运行shell.exe就能上线
2. 增加了upx压缩，缩小了exe体积
3. 自动更新图标文件的md5，防止图标资源成为查杀的特征码，现在不需要每隔一段时间次就替换图标文件
4. 支持powershell脚本免杀（还没开发的，就这几天弄）
5. 加载器已经被杀软分析透了，得大改才能活下去，开源之后差不多活了两个月，也还算可以了
### 时间 2021-9-23 版本：1.3
1. 去除了upx压缩，压缩率太低，没啥用，画蛇添足
2. 每次都会重置ico还有py的文件名
3. 封装了主main依赖库
##  温馨提示
> 使用之前安装一下python库 pip install -r requirement.txt，出现啥依赖库报错，大家自己解决吧，因为这个每个人的环境不一样，解决个依赖库报错相信不是啥难题

- 脚本采用python3.7编写

- 采用pyinstaller打包，使用之前请安装pyinstaller

- 运行之前先确认一下pip库有没有安装

- 环境实在报错就用fuckav.exe

- 因为开源了嘛，估计要不了半个月就会被加入360豪华套餐了，但是整个程序够简单，被杀了再去改几个特征码照样又可以免杀半个月，反正我自己用了半个月，一直都是国内杀软全过，保持更新，但是频率比较慢，因      为我只是个没用的安服

- 不得不说这个脚本确实有很多地方是在造轮子，但是是有意造的轮子，看似造轮子，实则是为了以后方便魔改（说白了就是菜，因为我是一个没用的安服）

- 因为脚本逻辑实在太过于简单，没啥技术含量，所以大家尽量还是不要把马子上传到云杀箱了吧，为了免杀活更久一点
## 存活动态
- 截止到 2021-8-20，360、火绒、Windows denfend、卡巴静态全过
- 截止到 2021-8-28，360、火绒、Windows denfend、卡巴静态全过  2021-8-28更新
- 截止到 2021-9-13，360、火绒、Windows denfend、静态全过，无法过360动态查杀（约一分钟之后就会报毒，可以再查杀之前选择进程注入。）
- 截止到 2021-9-23，360、火绒、Windows denfend、卡巴动静态全过，更新了一下改了改规则，又能过了....不愧是md5查杀器

![image](https://z3.ax1x.com/2021/08/20/fO7itK.jpg)
![image](https://z3.ax1x.com/2021/08/20/fOqMA1.png)
