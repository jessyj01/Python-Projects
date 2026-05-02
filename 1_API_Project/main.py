from datetime import datetime
import api_handler
import data_processor


if __name__ == "__main__":
    
    city, num_days = api_handler.get_user_input()
    print(f"City: {city}, Number of Days: {num_days}")

    weather_info = api_handler.get_weather_data(city, num_days)

    if weather_info:
        extracted_info = data_processor.extract_weather_info(weather_info)
        extracted_info = data_processor.check_weather_condition(extracted_info)
        data_processor.display_weather_info(extracted_info)

    else:
        print("Failed to retrieve weather data. Please check the city name and try again.")
    

