# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Define the data for countries, capitals, and currencies in a Python dictionary
# This data will be served by the backend
countries_data = [
    {"country": "United States", "capital": "Washington D.C.", "currency": "US Dollar"},
    {"country": "Canada", "capital": "Ottawa", "currency": "Canadian Dollar"},
    {"country": "Mexico", "capital": "Mexico City", "currency": "Mexican Peso"},
    {"country": "Brazil", "capital": "Brasília", "currency": "Brazilian Real"},
    {"country": "United Kingdom", "capital": "London", "currency": "Pound Sterling"},
    {"country": "France", "capital": "Paris", "currency": "Euro"},
    {"country": "Germany", "capital": "Berlin", "currency": "Euro"},
    {"country": "Italy", "capital": "Rome", "currency": "Euro"},
    {"country": "Spain", "capital": "Madrid", "currency": "Euro"},
    {"country": "China", "capital": "Beijing", "currency": "Chinese Yuan"},
    {"country": "India", "capital": "New Delhi", "currency": "Indian Rupee"},
    {"country": "Japan", "capital": "Tokyo", "currency": "Japanese Yen"},
    {"country": "Australia", "capital": "Canberra", "currency": "Australian Dollar"},
    {"country": "South Africa", "capital": "Pretoria", "currency": "South African Rand"},
    {"country": "Egypt", "capital": "Cairo", "currency": "Egyptian Pound"},
    {"country": "Saudi Arabia", "capital": "Riyadh", "currency": "Saudi Riyal"},
    {"country": "Russia", "capital": "Moscow", "currency": "Russian Ruble"},
    {"country": "Argentina", "capital": "Buenos Aires", "currency": "Argentine Peso"},
    {"country": "South Korea", "capital": "Seoul", "currency": "South Korean Won"},
    {"country": "Indonesia", "capital": "Jakarta", "currency": "Indonesian Rupiah"},
]

# Define a REST API endpoint to serve the countries data
@app.route('/api/countries', methods=['GET'])
def get_countries():
    """
    Returns a JSON list of countries, their capitals, and currencies.
    This endpoint can be accessed by the frontend to fetch the data.
    """
    return jsonify(countries_data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
