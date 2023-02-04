from geopy.geocoders import Nominatim


def convertCityToLocation(city_name):
    geolocator = Nominatim(user_agent="MyApp")  # Initialize Nominatim API
    location = geolocator.geocode(city_name)  # get location
    # print("$$$$$$$$$$$$$$$$$$$ The latitude of the location is: ", location.latitude)
    # print("$$$$$$$$$$$$$$$$$$$ The longitude of the location is: ", location.longitude)
    return location.latitude, location.longitude


def getExactCityName(city_name):
    geolocator = Nominatim(user_agent="MyApp")  # Initialize Nominatim API
    location = geolocator.geocode(city_name)  # get location
    return location
