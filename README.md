# CloudGenshinCheckinHelper

![Language](https://img.shields.io/badge/Language-Python-yellow)![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-red)![Author](https://img.shields.io/badge/Author-DanKe-blue)

云原神自动签到，每天自动白嫖15分钟免费时长，使用微信订阅号推送信息。

```
                #LICENSE_add
                该项目附加协议
​                   2022/11/4

  在 GPLv3协议（GNU GENERAL PUBLIC LICENSE Version 3）基础上，您需要遵守以下协议：
  （如果本协议与 GPLv3协议 相冲突，请以本协议为准！）

  1.绝对禁止使用本项目进行盈利。
  2.禁止使用本项目名字进行宣传活动。
  3.使用本项目造成的任何后果，该项目所用奉献者与仓库所有者不承担任何法律责任。
  4.当您将本项目代码上传到其他网站向公众发表时，请标注本项目开源地址。
  5.如果本项目侵害到您的权利，请及时联系项目所有者对相关部分进行删除。
  6.如果您使用本项目出现问题时，项目奉献者和仓库所有者有权利不对您进行帮助。
  7.项目所有者有权利对项目内任何部分进行删除。
```



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
