

def extract_weather_info(weather_data):
    extracted_info = {}
    extracted_info["city_name"] = weather_data["city"]["name"]
    extracted_info["city_country"] = weather_data["city"]["country"]
    extracted_info["Date_time"] = weather_data["list"][0]["dt_txt"]
    extracted_info["temperature"] = weather_data["list"][0]["main"]["temp"]
    extracted_info["weather"] = weather_data["list"][0]["weather"][0]["main"]

    return extracted_info

def check_weather_condition(weather_info):

    if weather_info["weather"] in ["Rain" , "Thunderstorm" , "Drizzle"]:
        weather_info["weather_condition"] = "Its going to rain. Don't forget to take an umbrella!"
    elif weather_info["weather"] in ["Clear", "Clouds"]:
        if weather_info["temperature"] > 293.15:
            weather_info["weather_condition"] = "The weather is clear and Sunny. Enjoy your day with a good amount of sun screen!"
        else:
            weather_info["weather_condition"] = "The weather is clear but a bit chilly. You might want to wear a light jacket."
    else:
        weather_info["weather_condition"] = "The weather is a bit unpredictable. It's a good idea to check the forecast again later."

    return weather_info


def display_weather_info(weather_info):
    print(f"City: {weather_info['city_name']}, {weather_info['city_country']}")
    print(f"Date and Time: {weather_info['Date_time']}")
    print(f"Temperature: {weather_info['temperature']- 273.15:,.2f} °C)")
    print(f"Weather: {weather_info['weather']}")
    print(weather_info["weather_condition"])