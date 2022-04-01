# 北邮每日填报自动化

北邮 自动填报 疫情填报

## Modified
1. 重写了 `auto.py`, 使其更易读，并改进了日志输出方式;删除了 `config.py`，添加了 `test.py`。我宣布不分场合的面向对象就是一坨屎，不仅痛苦了自己，更痛苦了自己。
2. 修复了每日填报改用`CAS`认证之后无法填报的问题。
3. 现在需要将`AREA`写作`省+市+县`的形式，例如 `福建省+莆田市+仙游县`。暂时没有进一步完善脚本的想法。每日填报已经是一坨屎了，我没有必要在这上面恶心自己更多时间。
4. 自己用得爽就行了，憋捅到导员那里, 用填报省下来的心情好好学习，考离柏油吧

## History
1. 原来设置的时间是UTC时间的每日1:00 AM，即China Time的9:00 AM，但是因为近期Actions出现波动，导致很多人没打上卡，现在增加UTC时间的17:00(China Time次日1:00)
2. 改进README使用说明

## 说明
利用Github提供的Actions完成自动运行脚本的过程
在`.github/workflow`中有一个YAML文件，打开后即可查看自动运行的相关细节
具体请查看相应文档

## 操作说明
1. 将本仓库Fork一份
2. 打开自己Fork的仓库，根据`.github/workflows/main.yml`中的字段，添加环境变量
即
```
env:
        USERNAME: ${{ secrets.USERNAME }}       # 学号
        PASSWORD: ${{ secrets.PASSWORD }}       # 信息门户用户名
        AREA: ${{ secrets.AREA }}               # 所在地区，例如"北京市+海淀区'
        PROVINCE: ${{ secrets.PROVINCE }}       # 所在省份，例如"北京市"
        CITY: ${{ secrets.CITY }}               # 所在城市，例如"北京市"
        SFZX: ${{ secrets.SFZX }}               # 是否在校，填"1"表示在校
```

添加`USERNAME`等字段
上述注释中示例均不需要添加双引号

+ 添加环境变量的方法
点击Settings（在Codes那一行）
找到Secrets
点击右上角添加键值对

在添加完毕后，点击Actions，进入自动操作的提示界面，开启Workflow
自动操作的触发条件有二，在`.github/workflows/main.yml`中有说明

```
on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 1 * * *'
    - cron: '0 17 * * *'
```
其一是`main`函数自动更新时触发，其二是UTC时间的1:00、17:00整点触发
