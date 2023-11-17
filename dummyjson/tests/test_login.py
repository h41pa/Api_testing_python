from time import sleep
from dummyjson.pages.requets_dummy_json import RequestDummyJSon


def test_login_status():
    dummy = RequestDummyJSon()
    response = dummy.login()
    sleep(2)
    expected_status = 200
    actual_status = response.status_code
    assert expected_status == actual_status, "Error, unexpected status code!"
