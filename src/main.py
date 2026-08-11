from datetime import date

TRAVELERS = 4

DEPARTURE_AIRPORTS = [
    "MAD",
    "AGP",
    "ALC",
    "VLC",
    "SVQ",
    "BIO",
    "BCN",
]

LATEST_RETURN = date(2026, 9, 5)

print("======================================")
print("🚀 TravelHackerAI")
print("======================================")
print(f"👨‍👩‍👧‍👦 Viajeros: {TRAVELERS}")
print(f"✈️ Aeropuertos: {', '.join(DEPARTURE_AIRPORTS)}")
print("🌍 Destino: CUALQUIERA")
print(f"📅 Regreso máximo: {LATEST_RETURN.strftime('%d/%m/%Y')}")
print("======================================")
print("✅ Configuración cargada correctamente")
