import pandas as pd
import streamlit as st
import folium
from daten import RESTAURANTS
from funktionen import mittelwert
from streamlit_folium import st_folium

st.title("Spike: Eventplaner - Christoph")
st.text(f"Durchschnittsbewertung: {mittelwert(RESTAURANTS, [eintrag['bewertung'] for eintrag in RESTAURANTS]):.1f}")

# 1. Karte erstellen (zentriert z. B. auf Kempten/Allgäu)
karte = folium.Map(location=[47.73, 10.31], zoom_start=1)

# 2. Schleife durch alle Restaurants in deiner Liste
for restaurant in RESTAURANTS:
    # Koordinaten aus dem Dictionary lesen
    lat = restaurant["breite"]
    lon = restaurant["laenge"]
    
    # Text für das Popup (wird beim Klicken angezeigt)
    popup_text = f"<b>{restaurant['lokalitaet']}</b><br>{restaurant['ort']}<br>Uhrzeit: {restaurant['uhrzeit']} Uhr<br>Bewertung: ⭐ {restaurant['bewertung']}"
    
    # Marker zur Karte hinzufügen
    folium.Marker(
        location=[lat, lon],
        popup=popup_text,
        tooltip=restaurant["lokalitaet"],  # Zeigt den Namen beim Drüberfahren mit der Maus
        icon=folium.Icon(color="red", icon="cutlery", prefix="fa")  # Rotes Bestecksymbol
    ).add_to(karte)

# 3. Karte in Streamlit anzeigen
st_folium(karte, width=700, height=500)