import csv
from geopy.geocoders import Nominatim

f = open('city_temperatures.csv')
csv_f = csv.reader(f)
Geo_Location = list(csv_f)
Temp_Loc = []
print(len(Geo_Location))
Geo_Location[0].extend(['latitude'])
Geo_Location[0].extend(['longitude'])
for i in range(1,len(Geo_Location)):
  #print(Geo_Location[i])

  address=Geo_Location[i][0:2]
  geolocator = Nominatim(user_agent="Ian_Unson")
  location = geolocator.geocode(address)
  print(location.address)
  print((location.latitude, location.longitude))
  Geo_Location[i].extend([location.latitude])
  Geo_Location[i].extend([location.longitude])

with open('city_temperatures_location.csv', 'w', newline="") as g:
  # using csv.writer method from CSV package
  write = csv.writer(g)
  write.writerows(Geo_Location)

print(Geo_Location)
print(Geo_Location[1][0:2])
# print(Geo_Location[0])
# print(Temp_Loc)