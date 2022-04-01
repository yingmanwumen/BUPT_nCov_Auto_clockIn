import os

os.environ['USERNAME'] = '' # 学号
os.environ['PASSWORD'] = '' # 信息门户密码
os.environ['AREA'] = ''     # '省+市+县'
os.environ['PROVINCE'] = '' # 省
os.environ['CITY'] = ''     # 市
os.environ['SFZX'] = '0'

os.system('python auto.py')

