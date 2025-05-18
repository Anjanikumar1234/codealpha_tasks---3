import requests
import folium
import webbrowser
import os
from datetime import datetime

# -------------- CONFIG --------------
OPENWEATHER_API_KEY = "your_valid_api_key_here"  # Replace with your key
# ------------------------------------

def get_geolocation(ip=None):
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
    try:
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            return {
                "ip": data.get("query"),
                "city": data.get("city"),
                "region": data.get("regionName"),
                "country": data.get("country"),
                "latitude": data.get("lat"),
                "longitude": data.get("lon"),
                "timezone": data.get("timezone"),
                "isp": data.get("isp"),
            }
        else:
            print("Geolocation error:", data.get("message"))
            return None
    except requests.RequestException as e:
        print("Network error:", e)
        return None

def get_weather(lat, lon):
    if not OPENWEATHER_API_KEY or len(OPENWEATHER_API_KEY) < 20:
        return {"error": "Invalid or missing OpenWeatherMap API key."}
    
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "description": data["weather"][0]["description"].capitalize(),
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            return {"error": data.get("message", "Could not fetch weather")}
    except Exception as e:
        return {"error": str(e)}

def display_map(location_data, weather_info):
    lat = location_data["latitude"]
    lon = location_data["longitude"]

    m = folium.Map(location=[lat, lon], zoom_start=12, tiles="OpenStreetMap")

    # Add terrain layer with proper attribution
    folium.TileLayer(
        tiles='Stamen Terrain',
        attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors'
    ).add_to(m)

    popup_text = f"""
    <b>IP:</b> {location_data['ip']}<br>
    <b>City:</b> {location_data['city']}<br>
    <b>Region:</b> {location_data['region']}<br>
    <b>Country:</b> {location_data['country']}<br>
    <b>Timezone:</b> {location_data['timezone']}<br>
    <b>ISP:</b> {location_data['isp']}<br><br>
    <b>Weather:</b> {weather_info.get('description', 'N/A')}<br>
    <b>Temperature:</b> {weather_info.get('temperature', 'N/A')}°C<br>
    <b>Humidity:</b> {weather_info.get('humidity', 'N/A')}%<br>
    <b>Wind Speed:</b> {weather_info.get('wind_speed', 'N/A')} m/s
    """

    folium.Marker([lat, lon], popup=folium.Popup(popup_text, max_width=300)).add_to(m)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    map_filename = f"user_geolocation_map_{timestamp}.html"
    m.save(map_filename)
    webbrowser.open('file://' + os.path.realpath(map_filename))

def main():
    print("🌐 IP Geolocation Tracker\n")
    user_ip = input("🔎 Enter IP address (or press Enter if you don't know your IP): ").strip()

    # If user doesn't enter IP or types common phrases meaning "don't know"
    if user_ip == "" or user_ip.lower() in ["don't know", "dont know", "unknown", "no"]:
        print("ℹ️ Automatically detecting your current IP address...")
        user_ip = None  # get_geolocation with None fetches current IP info

    print("\n📍 Fetching location...")
    location = get_geolocation(user_ip)
    if location:
        print("✅ Location found:")
        for key, value in location.items():
            print(f"{key.capitalize()}: {value}")
        
        print("\n☁️ Getting current weather...")
        weather = get_weather(location['latitude'], location['longitude'])

        if "error" in weather:
            print("⚠️ Weather error:", weather["error"])
        else:
            print("\n🌦️ Weather Info:")
            for key, value in weather.items():
                print(f"{key.replace('_', ' ').capitalize()}: {value}")

        print("\n🗺️ Generating interactive map...")
        display_map(location, weather)
    else:
        print("❌ Could not retrieve geolocation.")

if __name__ == "__main__":
    main()
