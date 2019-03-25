import json
import time
import datetime
import threading
import schedule
from libapi import *

def get_seats(weekday=[1,3,4,5,6,7]):
    with open("seats.json",'r',encoding="utf-8") as f:
        weekday_str = ""
        for x in weekday:
            weekday_str = weekday_str + str(x) + ","
        weekday_str = weekday_str[:-1]
        seats = json.load(f)[weekday_str]
    return seats

def test_connect():
    pass

def reserve(weekday):
    seats = get_seats(weekday)
    print("------------------------------------------------------------------")
    print("all reserve message:",seats)
    print("------------------------------------------------------------------")
    for seat in seats:
        for user in seat["times"]:
            message = (user['username'], user['password'],seat['room'],user['begin'],user['end'],seat['seat_num'],user["date"])
            threading.Thread(target=book_seat_one,args=message).start()

def book_seat_one(username,password,room,begin_time,end_time,seat_num,date):
    p = libapi(username,password)
    room_id = p.getRoomIDbyName(room)
    reserve_date = p.dates()[int(date)]
    resp = p.book(begin_time,end_time,room_id,seat_num,reserve_date)
    print("note:")
    print(resp)
    print("-----------------------------------------------------------------")

def job():
    today = datetime.datetime.now().isoweekday()
    while True:
        try:
            test_connect()
            if today == 2:
                reserve([2])
            else:
                reserve([1,3,4,5,6,7])
            break
        except:
            pass

def main():
    c = schedule.every().day.at("05:00").do(job)
    print(c)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    print(get_seats())
    print("------------------------------------------------------------------")
    main()
