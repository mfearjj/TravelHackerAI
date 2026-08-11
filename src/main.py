from datetime import date, timedelta

# ======================================
# CONFIGURACIÓN TRAVELHACKERAI
# ======================================

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

EARLIEST_DEPARTURE = date(2026, 8, 21)
LATEST_RETURN = date(2026, 9, 5)

MAX_TOTAL_BUDGET = 2000


# ======================================
# INFORMACIÓN DE LA BÚSQUEDA
# ======================================

def print_header():
    print("======================================")
    print("🚀 TravelHackerAI")
    print("======================================")
    print(f"👨‍👩‍👧‍👦 Viajeros: {TRAVELERS}")
    print(f"✈️ Aeropuertos: {', '.join(DEPARTURE_AIRPORTS)}")
    print("🌍 Destino: CUALQUIERA")
    print(
        f"📅 Fechas: "
        f"{EARLIEST_DEPARTURE.strftime('%d/%m/%Y')} → "
        f"{LATEST_RETURN.strftime('%d/%m/%Y')}"
    )
    print(f"💰 Presupuesto máximo: {MAX_TOTAL_BUDGET} €")
    print("======================================")


def generate_search_dates():
    """Genera todas las fechas posibles de salida."""

    current_date = EARLIEST_DEPARTURE
    dates = []

    while current_date < LATEST_RETURN:
        dates.append(current_date)
        current_date += timedelta(days=1)

    return dates


def main():
    print_header()

    search_dates = generate_search_dates()

    print()
    print("🔎 CONFIGURACIÓN DE BÚSQUEDA")
    print("--------------------------------------")
    print(f"📆 Días de salida posibles: {len(search_dates)}")
    print(
        f"📆 Primera salida: "
        f"{search_dates[0].strftime('%d/%m/%Y')}"
    )
    print(
        f"📆 Última salida: "
        f"{search_dates[-1].strftime('%d/%m/%Y')}"
    )

    print()
    print("🛫 Aeropuertos a analizar:")
    for airport in DEPARTURE_AIRPORTS:
        print(f"   • {airport}")

    print()
    print("🎯 Estado:")
    print("   ✅ Configuración cargada")
    print("   ✅ Fechas generadas")
    print("   ⏳ Búsqueda de vuelos: siguiente fase")
    print("   ⏳ Búsqueda de hoteles: siguiente fase")
    print("   ⏳ Cálculo del chollo: siguiente fase")


if __name__ == "__main__":
    main()
