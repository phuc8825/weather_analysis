import requests
import pandas as pd
from sqlalchemy import create_engine

API_KEY = "e66826eb7698e2f5b9391e2d1e8cb88a"
url = "https://api.openweathermap.org/data/2.5/weather"



cities = ["Hanoi","Ho Chi Minh City","Bangkok","Singapore","Jakarta","Kuala Lumpur","Tokyo","Seoul","Beijing","Shanghai",
    "Delhi","Mumbai","London","Paris","Berlin","Madrid","Rome","New York","Los Angeles","Toronto","Mexico City","Sao Paulo",
    "Cairo","Dubai","Sydney","Melbourne"]
weather_data = []

for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            weather_record = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "weather": data["weather"][0]["main"]
            }
            weather_data.append(weather_record)
        else:

            print(
                f"FAILED: {city} "
                f"(Status Code: {response.status_code})"
            )

    except Exception as e:
        print(f"ERROR: {city}")
        print(e)

df = pd.DataFrame(weather_data)
csv_path = "data/raw/weather_data.csv"

df.to_csv(csv_path,index=False)
print(f"Data saved to {csv_path}")

engine = create_engine("sqlite://../data/database/weather_data.db")
df.to_sql("weather_data", con=engine, if_exists="replace", index=False)