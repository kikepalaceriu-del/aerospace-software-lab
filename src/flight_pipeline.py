from flight_loader import load_flight  # Importamos la función que carga y valida los datos del vuelo
from flight_analysis import analyze_flight  # Importamos la función que analiza el vuelo


def run_flight_system(file_path):
    # Función principal que ejecuta todo el sistema de análisis de vuelo

    print("\n🛫 INICIANDO SISTEMA DE ANÁLISIS DE VUELO\n")  # Mensaje de inicio del sistema

    flight = load_flight(file_path)  # Cargamos el archivo de vuelo usando el loader

    if flight is None:  # Verificamos si hubo error al cargar los datos
        print("❌ Error: no se pudo cargar el vuelo")  # Mensaje de error
        return  # Terminamos la ejecución si no hay datos válidos

    result = analyze_flight(flight)  # Ejecutamos el análisis del vuelo

    print("\n📊 RESULTADOS DEL VUELO:\n")  # Encabezado de resultados

    for key, value in result.items():  # Recorremos los resultados del análisis
        print(f"{key}: {value}")  # Mostramos cada métrica o resultado

    print("\n✔ SISTEMA TERMINADO CORRECTAMENTE\n")  # Mensaje final de éxito