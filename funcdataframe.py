import pandas as pd

def check_pollution(data_list):
    df=pd.DataFrame(data_list)

    df['Heality_Risk']='Heality'

    df.loc[df['AQI'] > 150, 'Heality_Risk']= 'Unheality'
    unheality=df[df['Heality_Risk']!= "Heality"]
    return unheality

data=[{"city": "Yerevan", "AQI": 155}]
check_pollution(data)
print (check_pollution(data))
