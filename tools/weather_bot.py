import requests
from pprint import pprint
from django.http import JsonResponse
from matplotlib.pyplot as plt
import pandas as pd

API_KEY = 'API KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(request):
    city = request.GET.get('city', 'Tampa')
    units = request.GET.get('units', 'imperial')  # 'imperial' for F, 'metric' for C
    unit_symbol = "°F" if units == 'imperial' else "°C"

try:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': units
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        alerts = []

        # Alerts logic
        if units == 'imperial':
            if temp > 90:
                alerts.append("⚠️ Heat Alert: Stay hydrated!")
            elif temp < 32:
                alerts.append("❄️ Cold Alert: Bundle up!")
        else:
            if temp > 32:
                alerts.append("⚠️ Heat Alert: Stay hydrated!")
            elif temp < 0:
                alerts.append("❄️ Cold Alert: Bundle up!")

        if condition in ['Thunderstorm', 'Rain', 'Snow']:
            alerts.append(f"⚠️ Weather Alert: {condition} expected!")

        # Final JSON Response
return JsonResponse({
            'city': city,
            'temperature': f"{temp}{unit_symbol}",
            'condition': condition,
            'alerts': alerts
        })
    
df = pd.read_csv('weather_data.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Temperature'], label='Temperature (°C)')
plt.plot(df['Date'], df['Humidity'], label='Humidity (%)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily Temperature and Humidity Trends')
plt.legend()
plt.grid(True)
plt.show()


