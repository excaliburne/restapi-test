from random import choice

def BookingGenerator():
    firstname = choice(['Mark','Erik','John','Sarah','Lea','Bart'])
    lastname = choice(['Smith','Hill','Ramirez','Rudzik','Keyes'])
    price = choice([250,450,200,150,600,1000,565])
    deposit = choice([True,False])
    checkin = choice(['2017-07-04','2018-07-11','2019-04-01','2019-05-01','2020-01-02'])
    checkout = choice(['2017-07-09','2018-07-18','2019-04-15','2019-05-08','2020-01-06'])
    addneeds = choice(['Water','Lunch','Sandwich','Beer','Wine'])

    return({
        'firstname': firstname,
        'lastname': lastname,
        'totalprice': price,
        'depositpaid': deposit,
        'bookingdates':{
            'checkin': checkin,
            'checkout':checkout
        },
        'additionalneeds': addneeds
    })