import pandas as pd
import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.worldometers.info/population/largest-cities-in-the-world/")

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

tbody = table.find("tbody")

rows = tbody.find_all("tr")

city_data = []

for row in rows:

    cols = row.find_all("td")

    if len(cols) >= 4:

        rank = cols[0].text.strip()
        city = cols[1].text.strip()
        country = cols[2].text.strip()
        population = cols[3].text.strip()

        population = (
            population
            .replace(",", "")
            .replace(" ", "")
        )

        city_data.append({
            "rank": rank,
            "city": city,
            "country": country,
            "population": population
        })

df = pd.DataFrame(city_data)
df["city"] = df["city"].str.extract(r"\((.*?)\)", expand=False).fillna(df["city"])
df.to_csv("data/raw/city_population.csv",index=False)
print(df.head())
print(df.shape)