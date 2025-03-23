import requests

API_KEY = '70dd5539145ffcfbd5654debe98d90b6'

def fetch_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)  # Debugging ke liye

    if data.get('main'):
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['description']
        }
    else:
        return None
