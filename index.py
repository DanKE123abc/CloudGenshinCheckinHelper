import setting
import requests
import json
import time
from wechatpush import AccessToken

host = setting.host
headers = setting.headers


def dankepush(openid,message):#微信推送
    access_token = AccessToken().get_access_token()
    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    result = response.json()
    print(result)


def buildHearders(token,device_id,device_name,device_model):#更改headers
        headers["x-rpc-combo_token"] = token
        headers["x-rpc-device_id"] = device_id
        headers["x-rpc-device_name"] = device_name
        headers["x-rpc-device_model"] = device_model


def sign():#签到
    rsp = requests.post(f'{host}/hk4e_cg_cn/gamer/api/login', headers=headers)
    return json.loads(rsp.text)


def getInfo():#签到时长检测
    rsp = requests.get(f'{host}/hk4e_cg_cn/wallet/wallet/get', headers=headers)
    return rsp.json()


def getRewards():
    rsp = requests.get(f'{host}/hk4e_cg_cn/gamer/api/listNotifications?status=NotificationStatusUnread'
                       f'&type=NotificationTypePopup&is_sort=true', headers=headers)
    rewards = rsp.json()['data']['list']
    for reward in rewards:
        reward_id = reward['id']
        reward_msg = reward['msg']
        rsp = requests.post(f'{host}/hk4e_cg_cn/gamer/api/ackNotification',
                            json={
                                "id": reward_id
                            },
                            headers=headers)
    return len(rewards)


def writeMsg():#签到和编辑信息
        #签到
        signResult = sign()
        #游戏信息
        gameInfo = getInfo()
        coins = gameInfo['data']['coin']
        free_times = gameInfo['data']['free_time']
        total_time = gameInfo['data']['total_time']
        rewards = getRewards()
        message = '''⏰当前时间：{} 
忘记领云原神免费时长了吗？已经帮您完成了！
####################
米云币：{}个
免费时长：{}分钟
总时长：{}分钟
💻签到结果：{}
🎁额外奖励：{}个
####################
祝您过上美好的一天！
                        ——by DanKe'''.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 28800)),
                               coins['coin_num'],
                               free_times['free_time'],
                               total_time,
                               signResult['message'],
                               rewards)
        return message
        

def handler(event, context):#这里是阿里云的入口，腾讯云要改成main_handler
    config_path = "config.json"
    with open(config_path, "r") as f:
        row_data = json.load(f)
    for user in row_data:
        token = user['Token']
        device_id = user['ID']
        device_name = user['NAME']
        device_model = user['MODEL']
        pushid = user['pushid']
        try:
            buildHearders(token,device_id,device_name,device_model)
            msg =  writeMsg()
        except:
            msg = '签到失败，headers可能发送错误'
        #print(msg)
        dankepush(pushid, msg)




if __name__ == '__main__':
    handler(None, None)
