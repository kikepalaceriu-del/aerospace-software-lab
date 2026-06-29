"""
Módulo Aircraft - Clase principal para modelado de aeronaves

Este módulo contiene la clase Aircraft que simula una aeronave con
capacidades de cálculo de sustentación y carga alar.

Autor: Enrique
Fecha: 2026
"""

from typing import List, Optional


class Aircraft:
    """
    Clase que representa una aeronave con propiedades aerodinámicas.
    
    Atributos:
        name (str): Nombre identificador de la aeronave
        mass (float): Masa total en kilogramos
        weight (float): Peso calculado en Newtons (masa * gravedad)
        wing_area (float): Área alar en metros cuadrados
        velocity (float): Velocidad de vuelo en m/s
        cl (float): Coeficiente de sustentación adimensional
        air_density (float): Densidad del aire en kg/m³ (default: 1.225 a nivel del mar)
        sensors (List): Lista de sensores montados en la aeronave
    """
    
    # Constante de aceleración gravitatoria
    GRAVITY = 9.81
    
    def __init__(
        self,
        name: str,
        mass: float,
        weight: Optional[float] = None,
        wing_area: float = 0,
        velocity: float = 0,
        cl: float = 0.0,
        air_density: float = 1.225
    ) -> None:
        """
        Inicializa una instancia de Aircraft.
        
        Args:
            name: Nombre de la aeronave
            mass: Masa en kg
            weight: Peso en N (si no se proporciona se calcula automáticamente)
            wing_area: Área alar en m²
            velocity: Velocidad en m/s
            cl: Coeficiente de sustentación
            air_density: Densidad del aire en kg/m³
        """
        self.name = name
        self.mass = mass
        self.weight = weight if weight is not None else mass * self.GRAVITY
        self.wing_area = wing_area
        self.velocity = velocity
        self.cl = cl
        self.air_density = air_density
        self.sensors: List = []

    def add_sensor(self, sensor) -> None:
        """
        Añade un sensor a la aeronave.
        
        Args:
            sensor: Objeto Sensor a añadir
        """
        if sensor is None:
            raise ValueError("El sensor no puede ser None")
        self.sensors.append(sensor)

    def add_flight_data(
        self,
        wing_area: Optional[float] = None,
        velocity: Optional[float] = None,
        cl: Optional[float] = None,
        weight: Optional[float] = None,
        air_density: Optional[float] = None
    ) -> None:
        """
        Actualiza datos de vuelo de la aeronave.
        
        Args:
            wing_area: Área alar (opcional)
            velocity: Velocidad (opcional)
            cl: Coeficiente de sustentación (opcional)
            weight: Peso (opcional)
            air_density: Densidad del aire (opcional)
        """
        if wing_area is not None:
            if wing_area <= 0:
                raise ValueError("El área alar debe ser positiva")
            self.wing_area = wing_area
        if velocity is not None:
            if velocity < 0:
                raise ValueError("La velocidad no puede ser negativa")
            self.velocity = velocity
        if cl is not None:
            self.cl = cl
        if weight is not None:
            if weight < 0:
                raise ValueError("El peso no puede ser negativo")
            self.weight = weight
        if air_density is not None:
            if air_density <= 0:
                raise ValueError("La densidad del aire debe ser positiva")
            self.air_density = air_density

    def calculate_lift(self) -> float:
        """
        Calcula la fuerza de sustentación usando la ecuación aerodinámica.
        
        Fórmula: L = 0.5 × ρ × V² × S × Cl
        
        Donde:
            L = Sustentación (N)
            ρ = Densidad del aire (kg/m³)
            V = Velocidad (m/s)
            S = Área alar (m²)
            Cl = Coeficiente de sustentación
        
        Returns:
            float: Fuerza de sustentación en Newtons
        """
        return 0.5 * self.air_density * (self.velocity ** 2) * self.wing_area * self.cl

    def calculate_wing_loading(self) -> float:
        """
        Calcula la carga alar (wing loading).
        
        Fórmula: Wing Loading = Peso Total / Área Alar
        
        Returns:
            float: Carga alar en N/m²
            
        Raises:
            ValueError: Si el área alar es menor o igual a cero
        """
        if self.wing_area <= 0:
            raise ValueError("El área alar debe ser mayor que cero")
        return self.weight / self.wing_area

    def input_flight_data(self) -> None:
        """
        Captura datos de vuelo desde la entrada del usuario de forma interactiva.
        Los valores vacíos mantienen los valores actuales.
        """
        print("\n--- Ingreso de Datos de Vuelo ---")
        try:
            self.name = input(f"Nombre del avión [{self.name}]: ") or self.name
            
            mass_input = input(f"Masa (kg) [{self.mass}]: ")
            if mass_input:
                self.mass = float(mass_input)
            
            wing_area_input = input(f"Área alar (m²) [{self.wing_area}]: ")
            if wing_area_input:
                self.wing_area = float(wing_area_input)
            
            velocity_input = input(f"Velocidad (m/s) [{self.velocity}]: ")
            if velocity_input:
                self.velocity = float(velocity_input)
            
            cl_input = input(f"Coeficiente Cl [{self.cl}]: ")
            if cl_input:
                self.cl = float(cl_input)
            
            air_density_input = input(f"Densidad del aire (kg/m³) [{self.air_density}]: ")
            if air_density_input:
                self.air_density = float(air_density_input)
            
            self.weight = self.mass * self.GRAVITY
            print("✓ Datos actualizados exitosamente\n")
            
        except ValueError as e:
            print(f"✘ Error: Entrada inválida - {e}\n")

    def show_data(self) -> None:
        """
        Imprime los datos actuales de la aeronave en formato legible.
        """
        print("\n" + "=" * 50)
        print(f"DATOS DE LA AERONAVE: {self.name}")
        print("=" * 50)
        print(f"Masa                 : {self.mass:.2f} kg")
        print(f"Peso                 : {self.weight:.2f} N")
        print(f"Área alar            : {self.wing_area:.2f} m²")
        print(f"Velocidad            : {self.velocity:.2f} m/s")
        print(f"Coeficiente Cl       : {self.cl:.2f}")
        print(f"Densidad del aire    : {self.air_density:.3f} kg/m³")
        print(f"Sensores             : {len(self.sensors)} conectados")
        print("=" * 50 + "\n")

    def __str__(self) -> str:
        """Representación en string del objeto Aircraft."""
        return f"Aircraft(name={self.name}, mass={self.mass}kg, lift={self.calculate_lift():.2f}N)"

    def __repr__(self) -> str:
        """Representación formal del objeto Aircraft."""
        return f"Aircraft({self.name!r}, {self.mass}, {self.wing_area}, {self.velocity}, {self.cl})"
