"""
Módulo Reports - Generación de reportes de aeronaves

Este módulo genera reportes profesionales de aeronaves con información
detallada sobre características, desempeño y estado operacional.

Autor: Enrique
Fecha: 2026
"""

from datetime import datetime
from typing import Optional
from aircraft import Aircraft
from sensor import Sensor


class AircraftReport:
    """
    Clase para generar reportes profesionales de aeronaves.
    
    Genera reportes en formato texto con información completa de la aeronave,
    sensores, y estado de vuelo.
    
    Atributos:
        aircraft (Aircraft): Instancia de Aircraft a reportar
        timestamp (datetime): Fecha y hora de generación del reporte
    """

    def __init__(self, aircraft: Aircraft) -> None:
        """
        Inicializa el generador de reportes.
        
        Args:
            aircraft: Instancia de Aircraft
        """
        self.aircraft = aircraft
        self.timestamp = datetime.now()

    def _get_flight_status(self) -> str:
        """
        Determina el estado de vuelo basado en la sustentación.
        
        Returns:
            str: Estado descriptivo del vuelo
        """
        lift = self.aircraft.calculate_lift()
        
        if lift > self.aircraft.weight * 1.1:  # 10% de margen
            return "🟢 LISTO PARA VUELO (Margen seguro)"
        elif lift >= self.aircraft.weight:
            return "🟡 EQUILIBRIO ALCANZADO"
        else:
            return "🔴 NO APTO PARA VUELO"

    def _get_sensors_info(self) -> str:
        """
        Obtiene información de sensores conectados.
        
        Returns:
            str: Información formateada de sensores
        """
        if not self.aircraft.sensors:
            return "  • Sin sensores conectados"
        
        sensors_info = []
        for i, sensor in enumerate(self.aircraft.sensors, 1):
            status = "✓" if sensor.is_operational else "✗"
            sensors_info.append(
                f"  {i}. {status} {sensor.name}: {sensor.value} {sensor.unit}"
            )
        
        return "\n".join(sensors_info)

    def generate_report(self) -> str:
        """
        Genera un reporte completo de la aeronave.
        
        Returns:
            str: Reporte formateado en texto
        """
        lift = self.aircraft.calculate_lift()
        wing_loading = self.aircraft.calculate_wing_loading()
        flight_status = self._get_flight_status()
        sensors_info = self._get_sensors_info()
        
        report = (
            f"\n{'=' * 70}\n"
            f"{'REPORTE TÉCNICO DE AERONAVE'.center(70)}\n"
            f"{'=' * 70}\n"
            f"Generado: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"{'=' * 70}\n\n"
            
            f"📋 INFORMACIÓN GENERAL\n"
            f"{'-' * 70}\n"
            f"Nombre de Aeronave       : {self.aircraft.name}\n"
            f"Masa                     : {self.aircraft.mass:.2f} kg\n"
            f"Peso                     : {self.aircraft.weight:.2f} N\n"
            f"Densidad del aire        : {self.aircraft.air_density:.3f} kg/m³\n\n"
            
            f"✈️  PARÁMETROS AERODINÁMICOS\n"
            f"{'-' * 70}\n"
            f"Área alar                : {self.aircraft.wing_area:.2f} m²\n"
            f"Velocidad de vuelo       : {self.aircraft.velocity:.2f} m/s\n"
            f"Coeficiente de sustent.  : {self.aircraft.cl:.2f}\n"
            f"Sustentación             : {lift:.2f} N\n"
            f"Carga alar               : {wing_loading:.2f} N/m²\n\n"
            
            f"📡 SENSORES CONECTADOS ({len(self.aircraft.sensors)})\n"
            f"{'-' * 70}\n"
            f"{sensors_info}\n\n"
            
            f"✈️  ESTADO DE VUELO\n"
            f"{'-' * 70}\n"
            f"{flight_status}\n"
            f"Diferencia de fuerzas     : {(lift - self.aircraft.weight):.2f} N\n\n"
            
            f"{'=' * 70}\n"
        )
        
        return report

    def export_to_file(self, filename: Optional[str] = None) -> str:
        """
        Exporta el reporte a un archivo de texto.
        
        Args:
            filename: Nombre del archivo (default: genera nombre automático)
            
        Returns:
            str: Ruta del archivo generado
        """
        if filename is None:
            timestamp = self.timestamp.strftime("%Y%m%d_%H%M%S")
            filename = f"report_{self.aircraft.name.replace(' ', '_')}_{timestamp}.txt"
        
        report_content = self.generate_report()
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"✓ Reporte exportado a: {filename}\n")
            return filename
        except IOError as e:
            print(f"✘ Error al exportar reporte: {e}\n")
            return ""


def main() -> None:
    """
    Función principal que demuestra la generación de reportes.
    """
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN DE GENERACIÓN DE REPORTES".center(70))
    print("=" * 70)
    
    # Crear aeronave de ejemplo
    plane = Aircraft(
        name="Experimental Rotocraft",
        mass=1500,
        wing_area=20,
        velocity=100,
        cl=0.8
    )
    
    # Añadir sensores
    imu = Sensor("IMU (Acelerómetro)", 9.81, "IMU")
    gps = Sensor("GPS", 120.5, "GPS")
    altimeter = Sensor("Altímetro", 1500.0, "ALTIMETER")
    
    plane.add_sensor(imu)
    plane.add_sensor(gps)
    plane.add_sensor(altimeter)
    
    # Generar reporte
    report = AircraftReport(plane)
    print(report.generate_report())
    
    # Exportar a archivo
    report.export_to_file()


if __name__ == "__main__":
    main()
