import json
import time
import datetime
import threading
import schedule
from libapi import *

def json_file(filename='seatmonment.json'):
    with open(filename, 'r',encoding = "utf-8") as f:
        seats_json = json.load(f)
    return seats_json

def reserve():
    seats = json_file()
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
    print("note(%s->%s):"%(username,resp["status"]))
    print(resp)
if __name__ == '__main__':
    reserve()
