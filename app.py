import requests
import streamlit as st

st.title("Weather Report ☁️")

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_wind_direction(degrees):
    directions = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
    index = int((degrees + 22.5) / 45) % 8
    return directions[index]

def main():
    try:
        city = st.text_input("Enter Your City")
        if st.button("Check"):
            api_key = "b1d2ededf0d77faf89a0c7e0a3acc4d1"
            final_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

            result = requests.get(final_url)
            data = result.json()

            if data['cod'] == '404':
                st.error("City not found.")
                return

            temperature_kelvin = data['main']['temp']
            temperature_celsius = round(kelvin_to_celsius(temperature_kelvin))
            temperature_fahrenheit = round(kelvin_to_fahrenheit(temperature_kelvin))
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['wind']['speed']
            wind_direction_degrees = data['wind']['deg']
            wind_direction_cardinal = get_wind_direction(wind_direction_degrees)
            cordinatelon = data['coord']['lon']
            cordinatelat = data['coord']['lat']
            visibility = data.get('visibility')
            wind_speed = data['wind']['speed']
            weather_condition = data['weather'][0]['description']

            st.subheader(f"Weather in {city}:")
            st.text(f"Temperature: {temperature_celsius} °C ({temperature_fahrenheit:.2f} °F)")
            st.text(f"Humidity: {humidity}%")
            st.text(f"Wind Speed: {wind_speed*3.6:.2f} km/h")
            st.text(f"Wind Direction: {wind_direction_cardinal}")
            st.text(f"Weather Condition: {weather_condition.capitalize()}")
            st.text(f"Latitude: {cordinatelat}")
            st.text(f"Longitude: {cordinatelon}")
            st.text(f"Pressure: {pressure} mb")
            if visibility:
                st.text(f"Visibility: {visibility / 1000:.2f} km")
            else:
                st.text("Visibility data not available.")
    except(KeyError):
        st.error("Please Enter the City Name")

if __name__ == "__main__":
    main()