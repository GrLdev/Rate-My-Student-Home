from secret_keys import google_maps_api_key
from requests import get
from app.forms import ValidationError

# Gets the place_id for a given address, checks if the address is in Cardiff and is a street address
def get_coords(formatted_address):
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={formatted_address}&key={google_maps_api_key}" 
        request = get(url)
        response = request.json()

        if response["status"] == "OK" and request.status_code == 200:
            result = response["results"][0]
            lat = result["geometry"]["location"]["lat"]
            lng = result["geometry"]["location"]["lng"]

            in_cardiff = any("Cardiff" in address_component["long_name"] for address_component in result["address_components"])
            is_street_address_or_premise = "street_address" in result["types"] or "premise" in result["types"]

            if not in_cardiff:
                raise Exception(f"Address is not in Cardiff: {formatted_address}")
            if not is_street_address_or_premise:
                raise Exception(f"Address is not a street address: {formatted_address}")
            return lat, lng
        
        else:
            raise Exception(f"Geocoding failed: {response['status']}")

    except Exception as e:
        return f"An error occurred: {str(e)}"

