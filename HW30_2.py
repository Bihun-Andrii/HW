import requests
city = input("Enter city name: ")

response = requests.get(f'https://api.open-meteo.com/v1/coords?q={city}')
json_data = response.json()
lat = json_data[0]['lat']
lon = json_data[0]['lon']

response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}')
json_data = response.json()
current = json_data['current_weather']

print(f"City: {city}")
print(f"Temperature: {current['temperature']}°C")
print(f"Humidity: {current['humidity']}%")
print(f"Pressure: {current['pressure']} hPa")



