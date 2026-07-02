"""
Aerospace Software Lab
test_aircraft.py
Análisis de vuelo
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.flight_loader import load_flight
from src.flight_analysis import analyze_flight

flight = load_flight("data/flight01.csv")

if flight is not None:
    print("\nDatos cargados correctamente:\n")
    print(flight)

    analyze_flight(flight)
