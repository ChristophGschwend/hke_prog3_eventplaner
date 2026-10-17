RESTAURANTS = [
    {"ort": "Kempten", "lokalitaet": "Hotel Post", "breite": 47.73, "laenge": 10.31, "uhrzeit": "19:30", "datum": "2024-06-15", "bewertung": 3.2},
    {"ort": "Memmingen", "lokalitaet": "Hotel Stadt", "breite": 47.99, "laenge": 10.18, "uhrzeit": "20:00", "datum": "2024-06-15", "bewertung": 4.0},
    {"ort": "Füssen", "lokalitaet": "Hotel Füssen", "breite": 47.57, "laenge": 10.70, "uhrzeit": "18:00", "datum": "2024-06-15", "bewertung": 5.0},
    {"ort": "Vils", "lokalitaet": "Schwarzer Adler", "breite": 47.67, "laenge": 10.62, "uhrzeit": "19:00", "datum": "2024-06-15", "bewertung": 4.5},
]

if __name__ == "__main__":
    for eintrag in RESTAURANTS:
        print(f"{eintrag['ort']:<12} {eintrag['lokalitaet']:<18} {eintrag['uhrzeit']:<8} {eintrag['datum']:<10} {eintrag['bewertung']:<5}")
              
       