import pandas as pd

weather_df = pd.read_csv("data/raw/weather_data.csv")
city_df = pd.read_csv("data/raw/city_population.csv")

merged_df = weather_df.merge(city_df,on="city",how="left")

print("Merged Shape:")
print(merged_df.shape)

print("\nPreview:")
print(merged_df.head())

merged_df.to_csv("data/processed/weather_population.csv",index=False)
