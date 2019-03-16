import json
import time
import datetime
import threading
import schedule
from libapi import *

def json_file(filename='seat.json'):
    with open(filename, 'r') as f:
        seats_json = json.load(f)
    return seats_json

def reserve(date):
    seats = json_file()
    for seat in seats:
        for user in seat['times']:
            message = (user['username'], user['password'],seat['room'],user['begin'],user['end'],seat['seat_num'],date)
            threading.Thread(target=book_seat_one,args=message).start()

def book_seat_one(username,password,room,begin_time,end_time,seat_num,date):
    p = libapi(username,password)
    room_id = p.getRoomIDbyName(room)
    resp = p.book(begin_time,end_time,room_id,seat_num,date)
    print(datetime.datetime.now())
    print(username)
    print(resp)
    print("-------------------------------------------------------")


def job1():
    while True:
        try:
            p = libapi("############", "######")        #you should put your own usename and password in this line
            reserve(p.dates()[1])
            break
        except:
            pass
        
def main():
    c = schedule.every().day.at("05:00").do(job1)       #you can set the time for the procedure to retrieve information
    print(c)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
