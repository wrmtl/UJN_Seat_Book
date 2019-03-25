import json
import threading

def json_file(filename='seat.json'):
    with open(filename, 'r',encoding = "utf-8") as f:
        seats_json = json.load(f)
    return seats_json

def reserve():
    seats = json_file()
    print("--------------------------------------------------------")
    print("all reserve message: ",seats)
    print("--------------------------------------------------------")
    for seat in seats:
        for user in seat['times']:
            message = (user['username'], user['password'],seat['room'],user['begin'],user['end'],seat['seat_num'],user["date"])
            print("reserve message: ",message)
            threading.Thread(target=book,args=message).start()

def book(username,password,room,begin_time,end_time,seat_num,date):
    print(username,date)


reserve()
