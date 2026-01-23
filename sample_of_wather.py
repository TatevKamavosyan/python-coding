water_samples = [
    {"id": "Sample_1", "pH": 7.2, "O2": 8.5},
    {"id": "Sample_2", "pH": 4.5, "O2": 9.0},
    {"id": "Sample_3", "pH": 8.1, "O2": 3.2},
    {"id": "Sample_4", "pH": 6.8, "O2": 7.8},
    {"id": "Sample_5", "pH": 5.2, "O2": 4.0}
]


# wather_samples={}
for key in range(len(water_samples)):
    if water_samples[key]['pH'] < 6.0:
        water_samples[key]['status'] = 'acidenic'
    elif water_samples[key]['O2'] < 5.0:
        water_samples[key]['status'] = 'hipoxia'
    else:
        water_samples[key]['status']='heality'
list_of_not_heality=filter(lambda x : x['status']!='heality', water_samples)        


print(water_samples)
print(list(list_of_not_heality))