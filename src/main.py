from datetime import date, timedelta
from pathlib import Path
import json


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

OUTPUT_DIR = Path("resultado")
OUTPUT_FILE = OUTPUT_DIR / "travel_hacker_report.json"


# ======================================
# GENERADOR DE FECHAS
# ======================================

def generate_dates():
    dates = []

    current_date = EARLIEST_DEPARTURE

    while current_date < LATEST_RETURN:
        dates.append(current_date)
        current_date += timedelta(days=1)

    return dates


# ======================================
# CONSTRUCCIÓN DEL INFORME
# ======================================

def build_report():

    search_dates = generate_dates()

    report = {
        "project": "TravelHackerAI",
        "status": "ready",
        "generated_at": date.today().isoformat(),

        "travel": {
            "travelers": TRAVELERS,
            "departure_airports": DEPARTURE_AIRPORTS,
            "destination": "ANYWHERE",
            "earliest_departure": EARLIEST_DEPARTURE.isoformat(),
            "latest_return": LATEST_RETURN.isoformat(),
            "maximum_budget": MAX_TOTAL_BUDGET,
        },

        "search": {
            "possible_departure_days": len(search_dates),
            "possible_departure_dates": [
                d.isoformat() for d in search_dates
            ],
            "flight_search": {
                "status": "pending",
                "source": None,
            },
            "hotel_search": {
                "status": "pending",
                "source": None,
            },
        },

        "deal_engine": {
            "status": "ready",
            "maximum_total_price": MAX_TOTAL_BUDGET,
            "ranking": "price_quality",
        },

        "next_steps": [
            "Connect flight data source",
            "Connect hotel data source",
            "Calculate total trip price",
            "Rank best deals",
            "Generate summer deal recommendation",
        ],
    }

    return report


# ======================================
# GUARDAR INFORME
# ======================================

def save_report(report):

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
        )


# ======================================
# CONSOLA
# ======================================

def print_summary(report):

    travel = report["travel"]
    search = report["search"]

    print()
    print("======================================")
    print("🚀 TravelHackerAI")
    print("======================================")

    print(f"👨‍👩‍👧‍👦 Viajeros: {travel['travelers']}")

    print(
        f"✈️ Aeropuertos: "
        f"{', '.join(travel['departure_airports'])}"
    )

    print(f"🌍 Destino: {travel['destination']}")

    print(
        f"📅 Fechas: "
        f"{travel['earliest_departure']} → "
        f"{travel['latest_return']}"
    )

    print(
        f"💰 Presupuesto máximo: "
        f"{travel['maximum_budget']} €"
    )

    print("--------------------------------------")

    print(
        f"📆 Días de salida posibles: "
        f"{search['possible_departure_days']}"
    )

    print("✈️ Búsqueda de vuelos: PENDIENTE")
    print("🏨 Búsqueda de hoteles: PENDIENTE")
    print("🤖 Motor de chollos: PREPARADO")

    print("--------------------------------------")

    print(f"📄 Informe generado: {OUTPUT_FILE}")

    print("======================================")


# ======================================
# MAIN
# ======================================

def main():

    report = build_report()

    save_report(report)

    print_summary(report)

    print()
    print("✅ TravelHackerAI finalizado correctamente")


if __name__ == "__main__":
    main()
