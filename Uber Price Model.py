import geopy.distance
from geopy.geocoders import Nominatim

def get_lat_lon(city_name):
  geolocator = Nominatim(user_agent="city_location_finder")
  location = geolocator.geocode(city_name)
  if location:
    return (location.latitude, location.longitude)
  else:
    return None

def get_distance(location_1, location_2):
  #Calculates the distance in kilometers between two coordinate
  distance = geopy.distance.distance(location_1, location_2).km
  return distance

def get_price_km(hour):
  # Determines the price per kilometer based on the booking hour.
  if 8 <= hour < 11:  # Peak morning hours
    price_km = 20
  elif 18 <= hour < 21: # Peak evening hours
    price_km = 15
  else: # Off-peak hours
    price_km = 10
  return price_km

def final_price(pickup_coords, drop_coords, booking_hour):
  # Calculates the final ride price
  total_distance = get_distance(pickup_coords, drop_coords)
  price_per_km = get_price_km(booking_hour)
  
  final_ride_price = round(total_distance * price_per_km, 2)
  return final_ride_price

# Main Program Execution

print("---- Uber Fare Calculator ----")
pickup_city = input("Enter the pickup city name: ")
drop_city = input("Enter the drop city name: ")
booking_hour = int(input("Enter the booking hour (0-23): "))

# Get coordinates for the cities
pickup_location_coords = get_lat_lon(pickup_city)
drop_location_coords = get_lat_lon(drop_city)

# Directly calculate and display the final price
calculated_price = final_price(pickup_location_coords, drop_location_coords, booking_hour)

print("\n------------------------------------")
print(f"✅ The estimated fare is: ₹{calculated_price}")
print("------------------------------------")
