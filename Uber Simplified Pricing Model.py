import geopy.distance
from geopy.geocoders import Nominatim

def get_distance(location_1,location_2):
  distance = geopy.distance.distance(location_1,location_2).km
  return distance

def get_price_km(hour):
  if(hour > 8) & (hour < 11):
    price_km = 20
  elif(hour > 18) & (hour < 21):
    price_km = 15
  else:
    price_km = 10

  return price_km


def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent="city_location_finder")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def Final_price(pickup_location,drop_location, booking_hour):
  total_price = get_distance(pickup_location, drop_location)
  actual_price = get_price_km(booking_hour)

  final_Price = round(total_price * actual_price,2)
  return final_Price

pickup_city = input("Enter the pickup city name: ")
drop_city = input("Enter the drop city name: ")
booking_hour = int(input("Enter the booking hour (0-23): "))

pickup_location_coords = get_lat_lon(pickup_city)
drop_location_coords = get_lat_lon(drop_city)

final_calculated_price = Final_price(pickup_location_coords, drop_location_coords, booking_hour)

final_calculated_price
