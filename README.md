# 北邮疫情防控通自动填报python脚本

## 说明
利用Github提供的Actions完成自动运行脚本的过程
相应文件在`.github/workflow`中
具体请查看相应文档

## 操作说明
1. 将本仓库Fork一份
2. 打开自己Fork的仓库，根据`.github/workflows/main.yml`中的字段，添加环境变量
即
```
env:
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
        AREA: ${{ secrets.AREA }}
        PROVINCE: ${{ secrets.PROVINCE }}
        CITY: ${{ secrets.CITY }}
        SFZX: ${{ secrets.SFZX }}
```
添加`USERNAME`等字段

+ 添加环境变量的方法
点击Settings（在Codes那一行）
找到Secrets
点击右上角添加键值对

在添加完毕后，点击Actions，进入自动操作的提示界面
自动操作的触发条件有二，在`.github/workflows/main.yml`中有说明
```
on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 1 * * *'
```