# CloudGenshinCheckHelper

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)

云原神自动签到，每天自动白嫖15分钟免费时长，使用微信订阅号推送信息。

### 起因

上学没时间玩游戏，没时间签到云原神，导致假期又不够时间玩，嗯，就这样。

### 安装教程

#### *关注微信公众号“蛋壳的窝”回复【云原神签到】领取教程*
#### *3分钟教你搭建云原神自动签到 [视频教程](https://www.bilibili.com/video/BV1ge4y127EL)*

在./setting.py里修改基础配置信息

在./config.json里修改用户信息

```
[
    {
      "Token":"这里是x-rpc-combo_token",
      "ID":"这里是x-rpc-device_id",
      "NAME":"这里是x-rpc-device_name",
      "MODEL":"这里是x-rpc-device_model",
      "pushid":"这里是要推送的微信关注者标识"
    },
    {
      "Token":"用户2",
      "ID":"用户2",
      "NAME":"用户2",
      "MODEL":"用户2",
      "pushid":"用户2"
    }
]
```

### 待续

todo
