from secret_keys import google_maps_api_key
from requests import get

def get_place_id(formatted_address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={formatted_address}&key={google_maps_api_key}" 
    request = get(url)
    response = request.json()["results"]
    if response != []:
        place_id =  response[0]["place_id"]
    else:
        place_id = None
    return place_id