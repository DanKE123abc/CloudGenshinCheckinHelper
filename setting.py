

#--------------------推送设置-----------------------

WechatPush= True
APPID = ""
APPSECRET = ""



#--------------------云原神设置---------------------

app_version = "3.3.0"#云原神版本号
sys_version = "11"#安卓版本号
app_id = '1953439974'#好像是固定的，不用变
host = 'https://api-cloudgame.mihoyo.com'
okhttp_version = "4.9.0"





#--------------------以下非特殊情况不要动---------------------
headers = {
    "x-rpc-combo_token": '',
    "x-rpc-client_type": "2",
    "x-rpc-app_version": app_version,
    "x-rpc-sys_version": sys_version,
    "x-rpc-channel": "mihoyo",
    "x-rpc-device_id": '',
    "x-rpc-device_name": '',
    "x-rpc-device_model": '',
    "x-rpc-app_id": app_id,
    "Referer": "https://app.mihoyo.com",
    "Host": "api-cloudgame.mihoyo.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/"+okhttp_version
}
