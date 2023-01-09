import requests
import json
from IPython import embed
import pytest

headers = {
    "Content-Type": "*/*",
    "accept": "*/*",
}

payload_post  = json.dumps({
                    "RTE": "",
                    "dailyCheckInRestriction": "",
                    "paymentRestriction": "Paid",
                    "calendarRestriction": "Monday2",
                    "slots": 10,
                    "checkInOptions": "Require no check in",
                    "cancellationRestriction": "",
                    "paymentAmount": "",
                    "checkInAndOutHealthRestriction": False,
                    "dailyCheckInAndOutRestriction": "",
                    "dedicateSlots": 2,
                    "service": "Parking",
                    "week": 1,
                    "earliestDateRestriction": "",
                    "gcashNumber": "",
                    "parkingAddress": "world",
                    "checkInHealthRestriction": False,
                    "parkingStatus": False,
                    "parkingArea": "BGC",
                    })

payload_patch = json.dumps({
                    "parkingArea": "GTP",
                    "calendarRestriction": "Monday2",
                    "updateKey": "RTE",
                    "updateValue": "pauljohansen"
                    })

payload_delete = json.dumps({
                    "parkingArea": "GTP",
                    "calendarRestriction": "Monday2"
                    })

url = "http://localhost:3000"
url_api_gateway = "https://zh66xn42vk.execute-api.ap-southeast-1.amazonaws.com/stage/parkingarea"
url_all_parking = "https://zh66xn42vk.execute-api.ap-southeast-1.amazonaws.com/stage/parkingareas"


# def test_get_index():
#     response = requests.get(url + "/", headers = headers)
#     print(response.status_code)
#     assert response.ok

# def test_get_landingPage():
#     response = requests.get(url + "/landingPage", headers = headers)
#     print(response.status_code)
#     assert response.ok 

# # def test_get_setupChecklist():
# #     response = requests.get(url + "/setupChecklist", headers = headers)
# #     print(response.status_code)
# #     assert response.ok

def test_get_parkingAreas():
    response = requests.get(url_all_parking, headers= headers)
    print(response.text)
    embed()
    assert response.ok

def test_post_parkingArea():
    response = requests.post(url_api_gateway, headers = headers, data = payload_post)
    print(response.status_code)
    # embed()
    assert response.ok

def test_patch_parkingArea():
    response = requests.patch(url_api_gateway, headers = headers, data = payload_patch)
    print(response.text)
    # embed()
    assert response.ok

def test_delete_parkingArea():
    response = requests.delete(url_api_gateway, headers = headers, data = payload_delete)
    print(response.text)
    # embed()
    assert response.ok