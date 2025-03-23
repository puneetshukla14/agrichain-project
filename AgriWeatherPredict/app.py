from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Crop Suggestion Page
@app.route('/crop')
def crop():
    return render_template('crop.html')

# Crop Suggestion Logic (POST)
@app.route('/suggest', methods=['POST'])
def suggest():
    city = request.form['city']
    weather = fetch_weather(city)

    if not weather:
        return render_template('crop.html', suggestion=" Weather data not found.")
    
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']

    # Simple suggestion logic
    if temp > 30 and humidity < 50:
        crop = "Millets / Bajra"
    elif 20 < temp <= 30:
        crop = "Wheat / Barley"
    elif temp <= 20:
        crop = "Mustard / Peas"
    else:
        crop = "Rice / Sugarcane"

    return render_template('crop.html', suggestion=f"Suggested Crop: {crop}")

# Weather API Fetch
def fetch_weather(city):
    API_KEY = '70dd5539145ffcfbd5654debe98d90b6'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Price Graph Page
@app.route('/price-graph')
def price_graph():
    return render_template('price_graph.html')

# API Route for Price History Data (IMPORTANT ✅)
@app.route('/api/price-history')
def price_history():
    # Dummy data - Replace with DB or dynamic data if needed
    data = [
        {"date": "2024-03-01", "price": 2200},
        {"date": "2024-03-02", "price": 2250},
        {"date": "2024-03-03", "price": 2300},
        {"date": "2024-03-04", "price": 2280},
        {"date": "2024-03-05", "price": 2350},
        {"date": "2024-03-06", "price": 2400},
    ]
    return jsonify({"data": data})

# Index Page (optional)
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
