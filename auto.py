from datetime import time
import os
import time
import requests
import logging
from lxml import etree

###############################################################################
# 常量设置
###############################################################################

# 登陆URL
LOGIN_URL = 'https://auth.bupt.edu.cn/authserver/login'

# 填报URL
FORM_URL = "https://app.bupt.edu.cn/ncov/wap/default/save"

# 重要: CAS认证的跳转地址记录
SERVICE = 'https://app.bupt.edu.cn/a_bupt/api/sso/cas'#?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&from=wap'

# 模拟浏览器信息
USER_AGENT = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'

# Execution信息的xpath
EXECUTION_XPATH = '/html/body/div[1]/div/form/div[5]/input[2]/@value'

# 表单信息
# 吐槽一下，写柏油的教务系统和疫情填报的前端程序员都tm煞笔
DATA = {
	"area":       "北京市+海淀区",
	"bztcyy":     "",           # 不合前一天同城原因
	"city":       "北京市",
	"created":    "1608086660", # 时间戳
	"csmjry":     "0",          # 近14日内本人/共同居住者是否去过疫情发生场所
	"date":       "20201216",   # 填报日期
	"fjsj":       "20200830",   # 返京时间
	"fxyy":       "",           # 返校原因
	"glksrq":     "",           # 观测开始实际
	"gllx":       "",           # 观察场所
	"gtjzzfjsj":  "",           # 共同居住者返京时间
	"gwszdd":     "",           # 未给出
	"ismoved":    "0",          # 当前地点是否与上次在同一城市
	"jcbhlx":     "",           # 接触人群类型
	"jcbhrq":     "",           # 接触时间
	"jchbryfs":   "",           # 接触方式
	"jcjgqr":     "0",          # 属于正常情况
	"jcjg":       "",           # 未解释
	"jcqzrq":     "",           # 未解释
	"jcwhryfs":   "",           # 接触方式
	"jhfjhbcc":   "",           # 计划返京航班班次/车次
	"jhfjjtgj":   "",           # 计划返京交通工具
	"jhfjrq":     "",           # 计划返京时间
	"jhfjsftjhb": "0",          # 未给出
	"jhfjsftjwh": "0",          # 未给出
	"jrsfqzfy":   "",           # 未给出
	"jrsfqzys":   "",           # 未给出
	"mjry":       "0",          # 密切接触人员
	"province":   "北京市",
	"qksm":       "",           # 情况说明
	"remark":     "",           # 其他信息
	"sfcxtz":     "0",          # 今日是否出现发热，咽痛，干咳，咳痰，乏力，呕吐，腹泻，嗅觉异常，味觉异常
	"sfcxzysx":   "0",          # 是否有任何与疫情相关的， 值得注意的情况
	"sfcyglq":    "0",          # 是否处于观察期
	"sfjcbh":     "0",          # 今日是否接触无症状感染/疑似/确诊人群
	"sfjchbry":   "0",          # 今日是否接触过近14日内在湖北其他地区（除武汉）活动过的人员
	"sfjcqz":     "",           # 未解释
	"sfjcwhry":   "0",          # 是否接触武汉人员
	"sfsfbh":     "0",          # 未给出
	"sfsqhzjkk":  "0",          # 未给出
	"sftjhb":     "0",          # 今日是否到过或者经停湖北其他地区(除武汉)
	"sftjwh":     "0",          # 今日是否经停武汉
	"sfxk":       "0",          # 未解释
	"sfygtjzzfj": "0",          # 家中是否有共同居住者返京
	"sfyqjzgc":   "",           # 未给出
	"sfyyjc":     "0",          # 是否到相关医院或门诊检查
	"sfzx":       "1",          # 是否在校
	"sqhzjkkys":  "",           # 未给出
	"szcs":       "",           # 所在地区
	"szgj":       "",           # 所在国家
	"szsqsfybl":  "0",          # 所在社区是否有确诊病例
	"tw":         "2",          # 体温范围
	"xjzd":       "",           # 现居住地
	"xkqq":       "",           # 未解释
	"xwxgymjzqk": "3",          # 疫苗接种情况：3针
	"zgfxdq":     "0",          # 中高风险地区
}

###############################################################################
# 设置Log信息
###############################################################################

# 设置debug等级
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

###############################################################################
# 环境变量获取
###############################################################################

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
AREA     = os.environ['AREA']       # 使用 `+` 连接省、市、县
PROVINCE = os.environ['PROVINCE']
CITY     = os.environ['CITY']
SFZX     = os.environ['SFZX']

###############################################################################
# 进行CAS认证, 获取cookie
###############################################################################

logging.info('Ready to authorize for %s', USERNAME)

try:
	# 设置连接
	session = requests.Session()

	# 发送请求，设置cookies
	headers = { "User-Agent": USER_AGENT }
	params = { "service": SERVICE }
	responce = session.get(url=LOGIN_URL, headers=headers, params=params)
	logging.debug('Get: %s %s', LOGIN_URL, responce)

	# 获取execution
	html = etree.HTML(responce.content)
	execution = html.xpath(EXECUTION_XPATH)[0]
	logging.debug('execution: %s', execution)

	# 构造表单数据
	data = {
		'username': USERNAME,
		'password': PASSWORD,
		'submit': "登录",
		'type': 'username_password',
		'execution': execution,
		'_eventId': "submit"
	}
	logging.debug(data)

	# 登录到疫情防控通
	responce = session.post(url=LOGIN_URL, headers=headers, data=data)
	logging.debug('Post %s, responce: %s', LOGIN_URL, responce)


	logging.info('Authorize successed')

###############################################################################
# 进行填报
###############################################################################

	# 设置表单数据
	data = DATA
	data['created'] = str(round(time.time()))
	data["area"] = AREA
	data["city"] = CITY
	data["province"] = PROVINCE
	data["sfzx"] = SFZX

	logging.info('Form: area: %s, is in university: %s', AREA ,bool(SFZX))
	logging.debug(data)

	# 填报
	responce = session.post(url=FORM_URL, headers=headers, data=data)
	logging.debug('Post %s, responce: %s', FORM_URL, responce)
	logging.info('Responce: %s', responce)

except Exception as e:
	logging.error(e)
	raise e
