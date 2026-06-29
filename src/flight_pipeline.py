from flight_loader import load_flight
from flight_analysis import analyze_flight


def run_flight_system(file_path):
    print("\n🛫 INICIANDO SISTEMA DE ANÁLISIS DE VUELO\n")

    flight = load_flight(file_path)

    if flight is None:
        print("❌ Error: no se pudo cargar el vuelo")
        return

    result = analyze_flight(flight)

    print("\n📊 RESULTADOS DEL VUELO:\n")

    for key, value in result.items():
        print(f"{key}: {value}")

    print("\n✔ SISTEMA TERMINADO CORRECTAMENTE\n")
    