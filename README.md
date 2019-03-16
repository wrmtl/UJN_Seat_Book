## 库依赖
#### 本程序使用的python解释器为python3
#### 请保证已将python的路径添加进入系统环境变量Path
#### 代码使用到了requests、schedule库，分别用于http请求和定时任务管理
#### pip install requests schedule

## 系统依赖
#### 所有文件编码格式为utf-8
#### Windows系统、Linux系统测试正常工作

## 程序功能介绍
#### TestBook.py 预约
#### 需要根据自身情况修改配置文件 seat.json
#### 配置文件的阅览室信息、座号、用户信息
#### 在实际情况允许范围内,在不同时间内可以使用不同账号预约同一座位
#### TestCheckIn.py 签到
#### 程序需要根据自身情况修改配置文件 people.json
#### 配置文件填入需要签到的用户的用户名和密码
#### 程序将每天定时检索用户的预约信息,并在预约开始时间完成签到

## 特别说明
#### 程序中使用libapi库,是预约、签到和信息查询的底层API
#### libapi库来自[Zephyr](https://github.com/iozephyr/UJN-Lib-Seat-API/blob/master/README.md)
#### 他的帮助给我很大的启发,在此郑重感谢