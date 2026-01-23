

sensors = {
    "S1": {"type": "Temperature", "value": 85, "status": "OK"},
    "S2": {"type": "Pressure", "value": 170, "status": "OK"},
    "S3": {"type": "CO2", "value": 400, "status": "OK"}
}


for name, data in sensors.items():
    sensor_type = data["type"]
    val = data["value"]
    if sensor_type == "Temperature" and val>80:
         data.update({'status':'Critical'})
    elif sensor_type == 'Pressure'and val>150:
        data.update({'status':'Critical'})
    elif sensor_type=="CO2" and val> 100 :
        data.update({"status":"Critical"})      
                 # Այստեղ գրիր if-else-ը...

        print (sensors)                 
    


    