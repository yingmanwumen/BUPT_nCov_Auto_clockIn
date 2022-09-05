import os

os.environ['USERNAME'] = '' # 学号
os.environ['PASSWORD'] = '' # 信息门户密码
os.environ['AREA'] = '北京市+海淀区'     # '省+市+县'
os.environ['PROVINCE'] = '北京市' # 省
os.environ['CITY'] = '北京市'     # 市
os.environ['SFZX'] = '1'        # 是否在校
os.environ['PUSHDEER_KEY'] = '' # PushDeer Key

os.system('python auto.py')

