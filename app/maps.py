from secret_keys import google_maps_api_key
from requests import get
from app.forms import ValidationError

# Gets the place_id for a given address, checks if the address is in Cardiff and is a street address
def get_place_id(formatted_address):
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={formatted_address}&key={google_maps_api_key}" 
        request = get(url)
        response = request.json()

        if response["status"] == "OK" and request.status_code == 200:
            result = response["results"][0]
            place_id =  result["place_id"]

            in_cardiff = any("Cardiff" in address_component["long_name"] for address_component in result["address_components"])
            is_street_address = "street_address" in result["types"]

            if not in_cardiff:
                raise ValidationError(f"Address is not in Cardiff: {formatted_address}")
            if not is_street_address:
                raise ValidationError(f"Address is not a street address: {formatted_address}")
            return place_id
        
        else:
            raise ValidationError(f"Geocoding failed: {response['status']}")

    except Exception as e:
        raise ValidationError(f"An error occurred: {e}")

