measurements = [
    {"city": "Yerevan", "pm25": 45},
    {"city": "Sevan", "pm25": 12},
    {"city": "Yerevan", "pm25": 60},
    {"city": "Gyumri", "pm25": 55},
    {"city": "Sevan", "pm25": 8},
    {"city": "Gyumri", "pm25": 30}
]



den_m=filter( lambda x : x['pm25']>35,measurements)
# print(list(den_m))

den_c=map(lambda x : x["city"], den_m)
print(list(den_c))

counts={}
for city in den_c:
    counts[city]= counts.get(city,0)+1
    print(counts)
