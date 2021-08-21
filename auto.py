import requests
import time
import datetime
import json
import os
from config import *


class Automatic(object):
	"""
	自动填报脚本
	"""
	def __init__(self, user=[]):
		"""
		Init the object and do some work
		"""
		self.cookies = None
		self.user = user
		self.today = datetime.date.today()
		self.date = "%4d%02d%02d" % (self.today.year, self.today.month,
			self.today.day)
		self.main()


	def authorize(self, username, password):
		"""
		Authorize
		"""
		# send POST request
		data = {
			"username": username,
			"password": password
		}

		try:
			print("Start Authorize for %s..." % username)
			self.cookies = requests.post(url=LOGIN_URL, data=data).cookies

		except Exception as e:
			print("Error Happen when LOGIN:", e)
			raise

		else:
			print("Successfully Authorized\n")


	def post(self):
		"""
		Send POST request and finish
		"""
		data = DATA
		data["created"] = round(time.time())
		data["date"] = self.date
		data["area"] = self.user["area"]
		data["city"] = self.user["city"]
		data["province"] = self.user["province"]
		data["sfzx"] = self.user["sfzx"]

		try:
			print("Cookies:")
			for item in self.cookies:
				print("\t" + item.name + "=",item.value)

			print("\nPost...")
			res = requests.post(url=FORM_URL, data=data, cookies=self.cookies)

		except Exception as e:
			print("Error Happen when POST Msg:", e)
			raise

		else:
			print("Successfully POSTed")
			return json.loads(res.text)


	def main(self):
		"""
		Main func
		"""
		print("==========================")
		print("Date: %4d-%02d-%02d" % (self.today.year,
			self.today.month, self.today.day))

		user = self.user
		print("--------------------------")
		self.authorize(user["username"], user["password"])
		res = self.post()
		print(res['m'] + "\n")



if __name__ == '__main__':
	user = {
		"username" : os.environ["USERNAME"],
		"password" : os.environ["PASSWORD"],
		"area" : os.environ["AREA"],
		"province" : os.environ["PROVINCE"],
		"city" : os.environ["CITY"],
		"sfzx" : os.environ["SFZX"]
	}
	Automatic(user=user)
