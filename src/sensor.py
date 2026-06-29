"""
Módulo Sensor - Sistema de sensores para aeronaves

Este módulo contiene la clase Sensor para simular sensores
de navegación y control en aeronaves (IMU, GPS, Altímetro, etc.).

Autor: Enrique
Fecha: 2026
"""

from typing import Any, Optional
from datetime import datetime


class Sensor:
    """
    Clase que representa un sensor en la aeronave.
    
    Soporta diferentes tipos de sensores: IMU, GPS, Altímetro, etc.
    Incluye validación de lecturas y timestamps de medición.
    
    Atributos:
        name (str): Nombre identificador del sensor
        value (Any): Valor actual leído por el sensor
        sensor_type (str): Tipo de sensor (IMU, GPS, Altimeter, etc.)
        unit (str): Unidad de medida del sensor
        timestamp (datetime): Marca de tiempo de la última lectura
        is_operational (bool): Estado operacional del sensor
    """
    
    # Tipos de sensores soportados
    SUPPORTED_TYPES = {"IMU", "GPS", "ALTIMETER", "TEMPERATURE", "PRESSURE", "CUSTOM"}
    
    # Unidades por tipo de sensor
    UNITS_MAP = {
        "IMU": "m/s²",
        "GPS": "m",
        "ALTIMETER": "m",
        "TEMPERATURE": "°C",
        "PRESSURE": "Pa"
    }

    def __init__(
        self,
        name: str,
        value: Any,
        sensor_type: str = "CUSTOM",
        unit: Optional[str] = None
    ) -> None:
        """
        Inicializa una instancia de Sensor.
        
        Args:
            name: Nombre del sensor
            value: Valor inicial del sensor
            sensor_type: Tipo de sensor (default: "CUSTOM")
            unit: Unidad de medida (se asigna automáticamente si es tipo conocido)
            
        Raises:
            ValueError: Si el tipo de sensor no es válido
        """
        self.name = name
        self.value = value
        
        if sensor_type not in self.SUPPORTED_TYPES and sensor_type != "CUSTOM":
            raise ValueError(f"Tipo de sensor no soportado: {sensor_type}")
        
        self.sensor_type = sensor_type
        self.unit = unit or self.UNITS_MAP.get(sensor_type, "unidad")
        self.timestamp = datetime.now()
        self.is_operational = True

    def read(self) -> Any:
        """
        Lee el valor actual del sensor.
        
        Returns:
            Any: Valor actual del sensor
            
        Raises:
            RuntimeError: Si el sensor no está operacional
        """
        if not self.is_operational:
            raise RuntimeError(f"Sensor {self.name} no está operacional")
        
        self.timestamp = datetime.now()  # Actualiza timestamp en cada lectura
        return self.value

    def update_value(self, new_value: Any) -> None:
        """
        Actualiza el valor del sensor.
        
        Args:
            new_value: Nuevo valor para el sensor
            
        Raises:
            RuntimeError: Si el sensor no está operacional
        """
        if not self.is_operational:
            raise RuntimeError(f"Sensor {self.name} no está operacional")
        
        self.value = new_value
        self.timestamp = datetime.now()

    def set_status(self, operational: bool) -> None:
        """
        Cambia el estado operacional del sensor.
        
        Args:
            operational: True si está operacional, False en caso contrario
        """
        self.is_operational = operational
        status = "OPERACIONAL" if operational else "NO OPERACIONAL"
        print(f"[{self.name}] Estado: {status}")

    def get_info(self) -> dict:
        """
        Retorna información detallada del sensor.
        
        Returns:
            dict: Diccionario con información del sensor
        """
        return {
            "nombre": self.name,
            "tipo": self.sensor_type,
            "valor": self.value,
            "unidad": self.unit,
            "estado": "OPERACIONAL" if self.is_operational else "NO OPERACIONAL",
            "última_lectura": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self) -> str:
        """Representación en string del sensor."""
        status = "✓" if self.is_operational else "✗"
        return f"{status} {self.name}: {self.value} {self.unit}"

    def __repr__(self) -> str:
        """Representación formal del sensor."""
        return f"Sensor({self.name!r}, {self.value}, {self.sensor_type!r})"
