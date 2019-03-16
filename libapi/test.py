import json
import time

from libapi import *

def json_file(filename='seat.json'):
    with open(filename, 'r') as f:
        seats_json = json.load(f)
    return seats_json

def reserve(date):
    seats = json_file()
    for seat in seats:
        for user in seat['times']:
            p = libapi(user['username'], user['password'])
            room_id = p.getRoomIDbyName(seat['room'])
            resp = p.book(user['begin'], user['end'], room_id, seat['seat_num'], date)
            # handle(resp)


def main():
    p = libapi("20161223105", "212711")
    while len(p.dates()) != 2:
        time.sleep(1)
    reserve(p.dates()[1])

if __name__ == '__main__':
    main()
