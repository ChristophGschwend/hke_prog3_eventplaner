import requests 

API_KEY = "364188dc375eccd10b10de6804023c5c"

lat = "47.5492"
lon = "10.6305"

request_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Fehler")