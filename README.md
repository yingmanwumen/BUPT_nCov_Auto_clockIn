# 北邮疫情防控通自动填报python脚本
A python script to automatically post daily report

## 声明
Descript

本项目仅用于学习交流使用，请诚实进行每日填报
This project is only for learning and communication. Please post the daily report honestly.

## 用法
Usage

更改`conf.py`中的学生姓名、密码
Modify the Student Name and the Password in `conf.py`

根据系统的不同执行以下操作
Perform the following steps depending on your PC system

### Linux
使用命令`crontab -e`，在底部添加如下语句：
Use `crontab -e`. Then append the following commands:

```shell
00 00 * * * python3 THE_ROUTE_OF_auto.py >> THE_ROUTE_OF_LOG_MSG
```


`THE_ROUTE_OF_auto.py` 例如：`~/myCommand/clockIn/auto.py`
`THE_ROUTE_OF_auto.py` For example:`~/myCommand/clockIn/auto.py`

`THE_ROUTE_OF_LOG_MSG` 例如：` ~/myCommand/clockIn/auto.log`
`THE_ROUTE_OF_LOG_MSG` For example:` ~/myCommand/clockIn/auto.log`

`00 00 * * *`意思是在每天的00：00自动运行
`00 00 * * *` means run automatically at 00:00 per day

也可以更改为每天早上7：00：`00 07 * * *`
You can change it to 7：00:`00 07 * * *`

使用`sudo /etc/init.d/cron restart`重启cron服务
Use `sudo /etc/init.d/cron restart` to restart the cron service

### Windows
详情参考<a href="https://www.cnblogs.com/wmm-study/p/10039547.html">这篇博客</a>
Loot at <a href="https://www.cnblogs.com/wmm-study/p/10039547.html">This blog</a> for details