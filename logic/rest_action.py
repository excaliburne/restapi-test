import requests as req 
from logic.generate_booking import BookingGenerator

def _url(path):
    return "https://restful-booker.herokuapp.com" + path 

def generate_booking(firstname="", lastname="", checkin="", checkout=""):
    payload = {}
    if firstname:
        payload['firstname'] = firstname 
    if lastname:
        payload['lastname'] = lastname 
    if checkin: 
        payload['checkin'] = checkin 
    if checkout:
        payload['checkout'] = checkout
    
    if payload:
        return req.get(_url('/booking/'), params=payload)
    else:
        return req.get(_url('/booking/'))

def describe_booking(booking_id):
    return req.get(_url('/booking/{:d}/'/format(booking_id)))

def add_random_booking():
    return add_booking(BookingGenerator())

def add_booking(booking):
    return req.post(_url('/booking/'), json=booking)

def remove_booking(booking_id, auth_token):
    return req.delete(_url('/booking/{:d}/'.format(booking_id)), cookies={
        "token": auth_token
    })

def update_booking(booking_id, auth_token, firstname='John', lastname='Cena', price = 345, deposit = True, checkin = '2019-01-01', checkout = '2019-01-06', addneeds = 'Blanket'):
    return req.put(_url('/booking/{:d}/'.format(booking_id)), json={
        'firstname': firstname,
        'lastname': lastname,
        'totalprice': price,
        'depositpaid': deposit,
        'bookingdates':{
            'checkin': checkin,
            'checkout':checkout
        },
        'additionalneeds': addneeds
    }, cookies={
        'token': auth_token
    })

def get_token(username='admin', password='password123'):
    url = _url('/auth')
    return req.post(url, json={
        'username': username,
        'password': password
    }).json()['token']
