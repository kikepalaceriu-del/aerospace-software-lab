from flight_pipeline import run_flight_system  # Importamos el sistema principal de análisis de vuelos
import os  # Importamos os para manejo de rutas del sistema operativo

# IMPORTAMOS X-1
from main import run_x1_system  # Importamos el segundo sistema (X-1) desde el archivo main


# Obtenemos la ruta base del proyecto de forma dinámica (dos niveles arriba del archivo actual)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_all_systems():
    # Función que ejecuta todos los sistemas del proyecto aeronáutico

    print("\n🧪 SISTEMA AERONÁUTICO UNIFICADO\n")  # Mensaje de inicio general

    # SISTEMA FLIGHT
    run_flight_system(os.path.join(BASE_DIR, "data", "flight01.csv"))  
    # Ejecutamos el sistema de vuelo usando la ruta completa del archivo CSV

    # SISTEMA X-1
    print("\n==============================")  # Separador visual
    print("🛩️ SISTEMA X-1")  # Título del sistema X-1
    print("==============================\n")  # Separador visual

    run_x1_system()  # Ejecutamos el sistema X-1

    print("\n✔ SISTEMA COMPLETO FINALIZADO\n")  # Mensaje final de éxito


# Punto de entrada principal del script
if __name__ == "__main__":
    run_all_systems()  # Ejecutamos la función principal solo si el archivo se ejecuta directamente