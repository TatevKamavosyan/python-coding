import pandas as pd

data = [
    {"city": "Yerevan", "AQI": 155},
    {"city": "Gyumri", "AQI": 45},
    {"city": "Vanadzor", "AQI": 90},
    {"city": "Abovyan", "AQI": 210},
    {"city": "Hrazdan", "AQI": 60}
]

df = pd.DataFrame(data)
df.loc[df['AQI']> 105, 'Heality_Risk']= "Unheality"
df.loc[df["AQI"] < 105, "Heality_Risk"] = "Heality"

Unheality= df[df["Heality_Risk"]!= "Heality"]
mean=df['AQI'].mean()

print(df)
print(Unheality)
print(mean)
