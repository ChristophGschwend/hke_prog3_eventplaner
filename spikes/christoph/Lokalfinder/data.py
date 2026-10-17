import requests


lat = "47.5492"
lon = "10.6305"
radius = "3000"  # Radius in Metern


API_KEY = "acf90c6908f3442a9d85400e1abedc70"

request_url = f"https://api.geoapify.com/v2/places?categories=catering.restaurant&filter=circle:{lon},{lat},{radius}&apiKey={API_KEY}"

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    
# Eine leere Liste für deine Lokale
    lokale_liste = []
    
    # Durch die Ergebnisse loopen
    for place in data.get("features", []):
        # 1. Namen herausfiltern
        name = place.get("properties", {}).get("name", "Unbekanntes Lokal")
        
        # 2. GPS-Koordinaten herausfiltern
        coords = place.get("geometry", {}).get("coordinates", [])
        
        if len(coords) >= 2:
            laenge = coords[0]  # Longitude
            breite = coords[1]  # Latitude
            
            # In ein Dictionary speichern (perfekt für deine App/Streamlit)
            lokal_eintrag = {
                "name": name,
                "breite": breite,
                "laenge": laenge
            }
            lokale_liste.append(lokal_eintrag)

    # Test-Ausgabe im Terminal
    for lokal in lokale_liste:
        print(f"Lokal: {lokal['name']} | Lat: {lokal['breite']} | Lon: {lokal['laenge']}")

else:
    print("Fehler")