from flight_pipeline import run_flight_system
import os

# IMPORTAMOS X-1
from main import run_x1_system


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_all_systems():
    print("\n🧪 SISTEMA AERONÁUTICO UNIFICADO\n")

    # SISTEMA FLIGHT
    run_flight_system(os.path.join(BASE_DIR, "data", "flight01.csv"))

    # SISTEMA X-1
    print("\n==============================")
    print("🛩️ SISTEMA X-1")
    print("==============================\n")

    run_x1_system()

    print("\n✔ SISTEMA COMPLETO FINALIZADO\n")


if __name__ == "__main__":
    run_all_systems()
    