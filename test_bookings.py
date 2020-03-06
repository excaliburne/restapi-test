from logic import rest_action
from assertpy import assert_that

def test_bookings_anna():
    resp = rest_action.generate_booking('Anna')
    assert_that(resp.ok, 'HTTP Request OK').is_true()
    for booking in resp.json():
        assert_that(resp.ok, 'HTTP Request OK').is_true()
        resp2 = rest_action.describe_booking(booking['bookingid'])
        assert_that(resp2.json()["firstname"], 'Firstname').contains('Anna')

def test_addbooking():
    resp = rest_action.add_random_booking()
    print(resp.json())
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_updatebooking():
    auth_token = rest_action.get_token()
    new_booking = rest_action.add_random_booking().json()['bookingid']
    resp = rest_action.update_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()


def test_removebooking():
    auth_token = rest_action.get_token()
    new_booking = rest_action.add_random_booking().json()['bookingid']
    resp = rest_action.remove_booking(new_booking, auth_token)
    assert_that(resp.ok, 'HTTP Request OK').is_true()