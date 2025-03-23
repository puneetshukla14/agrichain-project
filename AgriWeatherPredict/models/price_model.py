def predict_crop_price(crop, temperature, humidity):
    base_prices = {
        'wheat': 2000,
        'rice': 2500,
        'cotton': 6000,
        'soybean': 3500
    }

    price = base_prices.get(crop.lower(), 3000)  # Default if crop not found

    if temperature > 35:
        price -= 200
    elif temperature < 20:
        price += 150

    if humidity > 70:
        price -= 100

    return price
