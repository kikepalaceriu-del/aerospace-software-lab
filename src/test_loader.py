from flight_loader import load_flight
from flight_analysis import analyze_flight

flight = load_flight("data/flight01.csv")

if flight is not None:
    print("\nDatos cargados correctamente:\n")
    print(flight)

    analyze_flight(flight)
