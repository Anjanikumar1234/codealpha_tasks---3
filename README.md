# IP Geolocation Tracker

📌 **Description**  
This is a Python-based IP Geolocation Tracker that retrieves and displays detailed location information for any IP address you enter — or automatically detects your own IP if left blank. It shows city, region, country, timezone, and ISP details. Additionally, it fetches current weather data for the detected location using the OpenWeatherMap API and generates an interactive map showing the location with weather info markers.

🛠 **Installation**  
To run this project, ensure you have Python installed. You can download it from:  
🔗 [Python Official Website](https://www.python.org/downloads/)

Install required dependencies using pip:

```bash
pip install requests folium
```

🚀 **How to Run**  
Run the tracker using the command:

```bash
python geolocation_tracker.py
```

You will be prompted to enter an IP address or press Enter to detect your own IP automatically.

📊 **Example Runs**

**Example 1 - Providing an IP address**

```yaml
🌐 IP Geolocation Tracker

Enter IP address (or press Enter to detect your IP): 8.8.8.8

Fetching location...
Location found:
Ip: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Timezone: America/Los_Angeles
Isp: Google LLC

Fetching weather data...
Weather Description: Clear sky
Temperature: 20.5 °C
Humidity: 60%
Wind Speed: 3.6 m/s

Generating map...
Map has been saved and opened in your default browser.
```

**Example 2 - Auto-detecting your own IP**

```vbnet
Enter IP address (or press Enter to detect your IP): 

Detecting your IP...
Your IP: 123.45.67.89

Fetching location...
Location found:
Ip: 123.45.67.89
City: New York
Region: New York
Country: United States
Timezone: America/New_York
Isp: ISP Name

Fetching weather data...
Weather Description: Light rain
Temperature: 18.0 °C
Humidity: 72%
Wind Speed: 4.1 m/s

Generating map...
Map has been saved and opened in your default browser.
```

⏳ **Key Features**  
✅ Detects geolocation for any IP or auto-detects your own IP  
✅ Shows detailed info: city, region, country, timezone, ISP  
✅ Retrieves current weather data from OpenWeatherMap API  
✅ Generates an interactive map with location and weather popups  
✅ Opens the map automatically in your default browser

⚙️ **Configuration**  
You must replace the placeholder in the script with your valid OpenWeatherMap API key:

```python
OPENWEATHER_API_KEY = "your_valid_api_key_here"  # Replace with your key
```

🤝 **Contributing**  
Want to improve this project? Feel free to:  
🔹 Fork the repository  
🔹 Create a new branch  
🔹 Submit a pull request

Your contributions are always welcome! 😊
