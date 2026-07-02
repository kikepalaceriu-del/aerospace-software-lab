from flight_loader import load_flight  # Importamos la función para cargar y validar los datos del vuelo
from flight_analysis import analyze_flight  # Importamos la función que analiza los datos del vuelo

flight = load_flight("data/flight01.csv")  # Cargamos el archivo CSV con los datos del vuelo

if flight is not None:  # Verificamos que los datos se hayan cargado correctamente
    print("\nDatos cargados correctamente:\n")  # Mensaje de confirmación en consola
    print(flight)  # Mostramos el DataFrame con los datos del vuelo

    analyze_flight(flight)  # Ejecutamos el análisis del vuelo