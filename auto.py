import requests
import os
import time
import datetime
import json
from config import *
from conf import USERNAME, PASSWORD


class Automatic(object):
	"""
	自动填报脚本
	"""
	def __init__(self, username=[], password=[]):
		"""
		Init the object and do some work
		"""
		self.cookies = None
		self.username = username
		self.password = password
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
		data["area"] = AREA
		data["city"] = CITY
		data["province"] = PROVINCE

		try:
			# print("Form:")
			# for item in data:
			# 	print("\t" + item + ":", data[item])

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

		for i in range(len(self.username)):
			print("--------------------------")
			self.authorize(self.username[i], self.password[i])  # get cookies
			res = self.post()
			print(res['m'] + "\n")



if __name__ == '__main__':
	Automatic(username=USERNAME, password=PASSWORD)