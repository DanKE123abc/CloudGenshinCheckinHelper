import os
import json
import time
import sys

#时间：2022/10/14
#作者：蛋壳
#备注：一个在Python上极简的日志管理模块

version = "0.1.0"
logsfile = "logs.kilog"


def WriteLog(message):
    if os.path.exists(logsfile) == False:
        new = {
            "KiLogsVersion": "KiLogs "+version,
            "CreationTime":time.strftime('%Y-%m-%d %H:%M:%S')
        }
        newlogs = json.dumps(new)
        f = open(logsfile, 'w')
        f.write(newlogs)
        f.close()
    with open(logsfile, 'r') as f:
        logs = json.load(f)
    now = str(int(time.time()))
    msg = {now:message}
    logs.update(msg)
    with open(logsfile, 'w') as f:
        json.dump(logs, f)

def LoadLog(timestamp):
    try:
        timestamp = str(timestamp)
        with open(logsfile, "r") as f:
            logs = json.load(f)
        returnlog = logs[timestamp]
    except:
        returnlog = "LogNotFound"
    return returnlog

def Delete():
    os.remove(logsfile)
    os.remove("warning.kilog")

def info(message , iswrite=False , prefix=True):#info类型：可选记录(默认关闭)，可关闭前缀(默认打开)
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    print("[ "+ back_filename +": info]"+message)
    if iswrite==True:
        if prefix==True:
            WriteLog("[ "+ back_filename +": info]"+message)
        elif prefix==False:
            WriteLog(message)

def warning(message):#warning类型：必须记录，必须打开前缀，单独添加记录到warning.kilog
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    back_funcname = back_frame.f_code.co_name
    back_lineno = str(back_frame.f_lineno)
    print("[ "+ back_filename +": warning]"+message)
    WriteLog("[ "+ back_filename +": warning]"+message)
    with open("warning.kilog", 'a+') as f:
        f.write("---------WARNING---------" + '\n')
        f.write("---" + time.strftime('%Y-%m-%d %H:%M:%S') + "---"+'\n')
        f.write("Warning:"+message+"\n")
        f.write("FileName:"+back_filename+"\n")
        f.write("FuncName:"+back_funcname+"\n")
        f.write("Lineno:"+back_lineno+"\n")
        f.write("-----------end-----------"+'\n'+'\n')
        f.close()

def error(message , prefix=True):#error类型：必须记录，可关闭前缀(默认打开)
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    back_funcname = back_frame.f_code.co_name
    back_lineno = str(back_frame.f_lineno)
    print("[ "+ back_filename +": error]"+message+"\n"+"ErrorFuncName:"+back_funcname+"\n"+"ErrorLineno:"+back_lineno)#记录附加
    if prefix==True:
        WriteLog("[ "+ back_filename +": error]"+message)
    elif prefix==False:
        WriteLog(message)

def critical(message,iswrite=True):#critical类型：可选记录(默认打开)，必须打开前缀
    back_frame = sys._getframe().f_back
    back_filename = os.path.basename(back_frame.f_code.co_filename)
    back_funcname = back_frame.f_code.co_name
    back_lineno = str(back_frame.f_lineno)
    print("[ "+ back_filename +": critical]"+message+"\n"+"CriticalFuncName:"+back_funcname+"\n"+"CriticalLineno:"+back_lineno)#记录附加
    if iswrite==True:
        WriteLog("[ "+ back_filename +": critical]"+message)
    
def help():
    print("Hello KiLog "+version+"!")
    print(" ____  __.__.____         ")         
    print("|    |/ _|__|    |    ____   ____  ")
    print("|      < |  |    |   /  _ \ / ___\ ")
    print("|    |  \|  |    |__(  <_> ) /_/  >")
    print("|____|__ \__|_______ \____/\___  / ")
    print("        \/          \/    /_____/  ")
    print("A minimalist log management module for python")
    print("Github: http://github.com/DanKE123abc/KiLog")
    print("Another: DanKe (http://github.com/DanKE123abc)")
    print("LICENSE: MIT")
    print("-------------------------------------------------------------------------")
    print("./logs.kilog")
    print("        自动生成，日志文件统一目录，本质上时json文件，可读性差")
    print("./warning.kilog")
    print("        自动生成，Warning的专用日志，可读性好")
    print("./kilog.py")
    print("    info(message , iswrite=False , prefix=True)")
    print("        info类型：可选记录(默认关闭)，可关闭前缀(默认打开)")
    print("    warning(message)")
    print("        warning类型：必须记录，必须打开前缀，详细记录单独添加到warning.kilog")
    print("    error(message , prefix=True)")
    print("        error类型：必须记录，可关闭前缀(默认打开),输出时带有函数名和行数")
    print("    critical(message,iswrite=True)")
    print("        critical类型：可选记录(默认打开)，必须打开前缀,输出时带有函数名和行数")
    print("    WriteLog(message)")
    print("        记录信息函数，记录格式【时间戳:内容】")
    print("    LoadLog(timestamp)")
    print("        用时间戳查找内容，有则返回内容，没有则返回'LogNotFound'")
    print("    Delete()")
    print("        删除所有日志")
    print("-------------------------------------------------------------------------")
    

if __name__ == '__main__':
    help()