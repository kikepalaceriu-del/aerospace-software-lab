"""
Módulo Main - Programa principal de Aerospace Software Lab

Este es el programa principal que integra todos los componentes del sistema:
Aircraft, Sensores, Cálculos aerodinámicos y Reportes.

Implementa validaciones, pruebas de diagnóstico y menú interactivo.

Autor: Enrique
Fecha: 2026
"""
def run_x1_system():
    print("\n🛩️ SISTEMA X-1 EJECUTÁNDOSE\n")
    
    # aquí va tu lógica actual del main
    print("Reporte Experimental Aircraft X-1 generado")
from typing import List, Tuple
from aircraft import Aircraft
from sensor import Sensor
from reports import AircraftReport

def run_system_checks(aircraft: Aircraft) -> List[Tuple[str, bool]]:
    """
    Ejecuta pruebas de diagnóstico del sistema.
    
    Args:
        aircraft: Instancia de Aircraft a verificar
        
    Returns:
        List[Tuple[str, bool]]: Lista de (descripción, estado) de cada prueba
    """
    results = []
    
    # Verificación 1: Existencia de aeronave
    try:
        aircraft_exists = isinstance(aircraft, Aircraft) and aircraft.name != ""
        results.append(("Aeronave inicializada", aircraft_exists))
    except Exception as e:
        results.append(("Aeronave inicializada", False))
    
    # Verificación 2: Sensores operacionales
    try:
        sensors_operational = bool(aircraft.sensors) and all(
            sensor.is_operational for sensor in aircraft.sensors
        )
        results.append(("Sensores operacionales", sensors_operational))
    except Exception as e:
        results.append(("Sensores operacionales", False))
    
    # Verificación 3: Cálculo de sustentación válido
    try:
        lift_value = aircraft.calculate_lift()
        lift_valid = isinstance(lift_value, (int, float)) and lift_value >= 0
        results.append(("Cálculo de sustentación", lift_valid))
    except Exception as e:
        results.append(("Cálculo de sustentación", False))
    
    # Verificación 4: Cálculo de carga alar válido
    try:
        wing_loading = aircraft.calculate_wing_loading()
        wing_loading_valid = isinstance(wing_loading, (int, float)) and wing_loading > 0
        results.append(("Cálculo de carga alar", wing_loading_valid))
    except Exception as e:
        results.append(("Cálculo de carga alar", False))
    
    # Verificación 5: Viabilidad de vuelo
    try:
        lift = aircraft.calculate_lift()
        flight_viable = lift > aircraft.weight
        results.append(("Viabilidad de vuelo", flight_viable))
    except Exception as e:
        results.append(("Viabilidad de vuelo", False))
    
    return results


def display_aircraft_report(aircraft: Aircraft) -> None:
    """
    Muestra un reporte visual del estado de la aeronave.
    
    Args:
        aircraft: Instancia de Aircraft
    """
    lift = aircraft.calculate_lift()
    status = "OPERACIONAL" if lift > aircraft.weight else "RESTRICCIÓN DE VUELO"
    sensor_names = ", ".join(sensor.name for sensor in aircraft.sensors)
    
    print("\n" + "=" * 70)
    print("REPORTE OPERACIONAL DE AERONAVE".center(70))
    print("=" * 70)
    print(f"Nombre       : {aircraft.name}")
    print(f"Masa         : {aircraft.mass:.2f} kg")
    print(f"Peso         : {aircraft.weight:.2f} N")
    print(f"Sustentación : {lift:.2f} N")
    print(f"Estado       : {status}")
    print(f"Sensores     : {sensor_names if sensor_names else 'Ninguno'}")
    print("=" * 70)


def display_test_results(results: List[Tuple[str, bool]]) -> None:
    """
    Muestra los resultados de las pruebas de diagnóstico.
    
    Args:
        results: Lista de resultados de pruebas
    """
    print("\n" + "-" * 70)
    print("RESULTADOS DE DIAGNÓSTICO DEL SISTEMA".center(70, "-"))
    print("-" * 70)
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    for label, passed in results:
        icon = "✓" if passed else "✗"
        status_text = "PASÓ" if passed else "FALLÓ"
        print(f"  {icon} {label:<40} [{status_text:^6}]")
    
    print("-" * 70)
    print(f"Resultado Final: {passed_count}/{total_count} pruebas completadas")
    
    if passed_count == total_count:
        print("🟢 SISTEMA LISTO - Todas las pruebas exitosas")
    else:
        print("🟡 SISTEMA CON RESTRICCIONES - Revisar fallos")
    
    print("-" * 70 + "\n")


def main() -> None:
    """
    Función principal del programa.
    
    Realiza:
    1. Inicialización de aeronave con parámetros predefinidos
    2. Creación y conexión de sensores
    3. Ejecución de pruebas de diagnóstico
    4. Generación de reportes
    """
    
    print("\n" + "=" * 70)
    print("AEROSPACE SOFTWARE LAB - SISTEMA PRINCIPAL".center(70))
    print("Versión 1.0 - Autor: Enrique".center(70))
    print("=" * 70)
    
    # ==================== INICIALIZACIÓN ====================
    print("\n[1/4] Inicializando aeronave...")
    
    plane = Aircraft(
        name="Experimental Aircraft X-1",
        mass=1500,
        weight=1500 * 9.81,
        wing_area=20,
        velocity=100,
        cl=0.8,
    )
    print("✓ Aeronave inicializada correctamente")
    
    # ==================== SENSORES ====================
    print("\n[2/4] Configurando sensores...")
    
    imu = Sensor("IMU (Acelerómetro)", 9.81, "IMU")
    gps = Sensor("GPS (Posición)", 120.5, "GPS")
    altimeter = Sensor("Altímetro", 1500.0, "ALTIMETER")
    temperature = Sensor("Termómetro", 15.5, "TEMPERATURE")
    
    plane.add_sensor(imu)
    plane.add_sensor(gps)
    plane.add_sensor(altimeter)
    plane.add_sensor(temperature)
    
    print(f"✓ {len(plane.sensors)} sensores conectados exitosamente")
    
    # ==================== VISUALIZACIÓN ====================
    print("\n[3/4] Generando reportes...")
    
    display_aircraft_report(plane)
    
    # ==================== DIAGNÓSTICO ====================
    print("\n[4/4] Ejecutando diagnóstico del sistema...")
    
    check_results = run_system_checks(plane)
    display_test_results(check_results)
    
    # ==================== REPORTE DETALLADO ====================
    print("Generando reporte técnico detallado...\n")
    
    report = AircraftReport(plane)
    print(report.generate_report())
    
    # Exportar reporte a archivo
    report.export_to_file()
    
    print("✓ Programa ejecutado exitosamente\n")


if __name__ == "__main__":
    main()
