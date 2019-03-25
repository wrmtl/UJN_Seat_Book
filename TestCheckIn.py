import datetime
import time
import json
import schedule
from libapi import *


checkList = []

def get_people():
	with open("people.json","r") as f:
		people = json.load(f)
	return people

def change_date(date):
	date = date.split("-")
	new_date = date[0]
	for x in date[1:]:
		if x.__len__()<2:
			new_date = new_date + "-0" + x
		else:new_date = new_date + "-" +x
	return new_date

def checkMode(username,password):
	p = libapi(username,password)
	for x in p.history()["data"]["reservations"]:
		date = change_date(x["date"])
		if date == p.dates()[0]:
			if x["stat"] == "RESERVE":
				return [True,x["begin"]]
	return [False]

def all_check_time(people):
	global checkList
	for person in people:
		Mode = checkMode(person["username"],person["password"])
		if(Mode[0]):
			print(person,Mode)
			checkList.append({"username":person["username"],"password":person["password"],"time":Mode[1]})
		else:
			print(person,"No RESERVE")
		print("---------------------------------------")


def check_can():
		global checkList
		time = datetime.datetime.now()
		pan_time = time.hour*60+time.minute
		for user in checkList:
				user_times = [int(x) for x in user["time"].split(":")]
				user_time = user_times[0]*60+user_times[1]
				if user_time <= pan_time+43:
						MycheckIn(user["username"],user["password"])
						checkList.remove(user)

def MycheckIn(username,password):
		p = libapi(username,password)
		c = p.checkIn()
		print(datetime.datetime.now(),username,c)
		print("-------------------------------------")

def first_check():
	all_check_time(get_people())
	check_can()

def main():
	c1 = schedule.every().day.at("10:36").do(all_check_time,get_people())
	print(c1)
	print("-------------------------------------")
	c2 = schedule.every(10).seconds.do(check_can)
	print(c2)
	print("-------------------------------------")
	first_check()
	while True:
		schedule.run_pending()
		time.sleep(1)


if __name__ == '__main__':
	main()
