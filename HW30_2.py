import requests
city = input("Назва міста: ")

res = requests.get(f'https://api.open-meteo.com/v1/coords?q={city}')
json_data = res.json()
lat = json_data[0]['lat']
lon = json_data[0]['lon']

res2 = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}')
json_data = res2.json()
current = json_data['current_weather']

print(f"Місто: {city}")
print(f"Температура: {current['temperature']}°C")
print(f"Вологість: {current['humidity']}%")
print(f"Тиск: {current['pressure']} hPa")