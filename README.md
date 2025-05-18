IP Geolocation Tracker
📌 Description
This Python-based tool fetches and displays detailed geolocation information of any given IP address — or your own IP if none is provided. It shows location details such as city, region, country, timezone, and ISP. It also fetches real-time weather data for that location using the OpenWeatherMap API. Finally, it generates an interactive map with all the information shown via popup markers.

🛠 Installation
Make sure Python 3.x is installed on your system. Download it from:
Python Official Website

Install required dependencies using pip:

bash
Copy
Edit
pip install requests folium
🚀 How to Run
Run the script from your terminal or command prompt:

bash
Copy
Edit
python geolocation_tracker.py
🎯 Features
Detect geolocation by IP address (or auto-detect your own IP).

Shows detailed location info: city, region, country, timezone, ISP.

Fetches current weather data for the location (temperature, humidity, wind speed).

Generates an interactive map with markers and weather/location details.

Opens the generated map automatically in your default web browser.

📝 Usage Example
plaintext
Copy
Edit
🌐 IP Geolocation Tracker

🔎 Enter IP address (or press Enter if you don't know your IP): 8.8.8.8

📍 Fetching location...
✅ Location found:
Ip: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Timezone: America/Los_Angeles
Isp: Google LLC

☁️ Getting current weather...
🌦️ Weather Info:
Description: Clear sky
Temperature: 20.5
Humidity: 60
Wind speed: 3.6

🗺️ Generating interactive map...
The browser will open a map showing the location with weather and IP details in a popup.

⚙ Configuration
OpenWeatherMap API key:
The script requires an OpenWeatherMap API key to fetch weather data. Get your free API key from OpenWeatherMap and replace the value of OPENWEATHER_API_KEY in the script:

python
Copy
Edit
OPENWEATHER_API_KEY = "your_valid_api_key_here"  # Replace with your key
🤝 Contributing
Contributions and improvements are welcome!

Fork the repository

Create your feature branch

Commit your changes

Submit a pull request

📄 License
This project is open-source and free to use.

