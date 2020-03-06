# Introduction
Testing the REST API functionality of https://restful-booker.herokuapp.com with the help of python3, the "requests" library and "assertpy" for assertions.

## How to run it
Prerequisites: Python & pip <br>
`git clone https://github.com/excaliburne/Rest-api-test.git` <br>
`pip3 install -r requirements.txt` <br>
`pytest ./test_bookings.py` <br>

## API details
JSON example:
```
curl -X POST \
  https://restful-booker.herokuapp.com/booking \
  -H 'Content-Type: application/json' \
  -d '{
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}'
```

### Resources
- https://realpython.com/api-integration-in-python/
- https://restful-booker.herokuapp.com/apidoc/index.html 
