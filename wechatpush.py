import requests
import setting

#时间：2022/9/16
#作者：蛋壳
#备注：微信测试号token

class AccessToken(object):
    APPID = setting.APPID
    APPSECRET = setting.APPSECRET
    
    def __init__(self, app_id=APPID, app_secret=APPSECRET) -> None:
        self.app_id = app_id
        self.app_secret = app_secret

    def get_access_token(self) -> str:

       # 获取access_token凭证
       # :return: access_token
        
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)
