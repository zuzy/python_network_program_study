README
===========================
halo协议测试小工具

****
	
|Author|朱彤|
|---|---
|E-mail|zhutong@nbhope.cn


****
## 目录
- [README](#readme)
  - [目录](#%E7%9B%AE%E5%BD%95)
  - [测试过程](#%E6%B5%8B%E8%AF%95%E8%BF%87%E7%A8%8B)
  - [测试命令](#%E6%B5%8B%E8%AF%95%E5%91%BD%E4%BB%A4)
      - [dev_info](#devinfo)
      - [exit](#exit)
      - [index](#index)
      - [info](#info)
      - [mode](#mode)
      - [mute](#mute)
      - [next](#next)
      - [opertunnel](#opertunnel)
      - [pause](#pause)
      - [play](#play)
      - [power](#power)
      - [prev](#prev)
      - [querysong](#querysong)
      - [songlist](#songlist)
      - [source](#source)
      - [specify](#specify)
      - [voice_oper](#voiceoper)
      - [voice_speak](#voicespeak)
      - [vol](#vol)
  - [帮助命令](#%E5%B8%AE%E5%8A%A9%E5%91%BD%E4%BB%A4)
  - [智能家居配置](#%E6%99%BA%E8%83%BD%E5%AE%B6%E5%B1%85%E9%85%8D%E7%BD%AE)


## 测试过程
1. 执行halotest首先发送组播消息, 汇总所有组播回复内容后打印发现的设备列表
2. 根据目标的`类型`, `ip`, `mac`信息选择需要连接的设备, 键入对应的id建立连接
3. 接受到设备端发送的智能家居信息请求, 根据dev_db目录中的信息回复`设备`,`情景`,`楼层`,`房间`信息
4. 维持halo长连接, 接收键入的[测试命令](#测试命令)进行测试
5. 键入`Ctrl + c`退出测试
***

## 测试命令

#### dev_info
    参数:   无
    描述:   返回设备的基础信息
    用例:   
#### exit
    参数:   无
    描述:   退出连接, 退出测试
    用例:   
#### index
    参数:   歌曲id
    描述:   本地歌曲播放
    用例:   index:1
#### info
    参数:   无
    描述:   查询设备信息, 包含播放器和播放信息
    用例:

#### mode
    参数:   random(随机)/single(单曲)/cycle(全部)/list(顺序)
    描述:   设置播放模式
    用例:   mode:single

#### mute
    参数:   y(静音)/n(取消静音)
    描述:   静音
    用例:   mute:y
#### next
    参数:   无
    描述:   播放下一曲
    用例
#### opertunnel
    参数:   无
    描述:   分区控制, 暂时不支持
    用例
#### pause
    参数:   无
    描述:   暂停
    用例
#### play
    参数:   无
    描述:   播放
    用例
#### power
    参数:   y(关机)/n(开机)
    描述:   关机功能 (熄灭屏幕 + 暂停播放)
            开机功能 (点亮屏幕)
    用例:   power:y
#### prev
    参数:   无
    描述:   上一首
    用例:
#### querysong
    参数:   无
    描述:   暂时 halo 协议不支持
    用例:
#### songlist
    参数:   pageindex
    描述:   获取本地歌曲列表, 以2首为一页, 插叙第x页歌曲
    用例:   songlist:1
#### source
    参数:   local(本地)/bluetooth(蓝牙)/linein(外音)
    描述:   切换音源, 外音暂时不支持
    用例:   source:local

#### specify
    参数:   index
    描述:   指定播放一个本地铃声
    用例:   specify:1
#### voice_oper
    参数:   语音控制口令
    描述:   与语音控制相同, 使用文字模拟语音控制
    用例:   voice_oper:播放周杰伦的歌
#### voice_speak
    参数:   文字
    描述:   文字转语音
    用例:   voice_speak:欢迎光临
#### vol
    参数:   num(数字 0-15)/inc(提高)/dec(降低)
    描述:   音量控制
    用例:   vol:inc
***

## 帮助命令
`help` 命令: 列出所有命令<br>
`help: xxx` 查询指定命令的用法
***

## 智能家居配置
默认dev_db目录中文件为模拟的本地`场景/设备/楼层/房间`信息,编辑params内容
***




