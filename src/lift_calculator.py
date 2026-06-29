"""
Módulo Lift Calculator - Cálculo de sustentación aerodinámica

Este módulo demostra cómo calcular la fuerza de sustentación de una aeronave
usando los parámetros aerodinámicos implementados en la clase Aircraft.

Fórmula: L = 0.5 × ρ × V² × S × Cl

Autor: Enrique
Fecha: 2026
"""

from aircraft import Aircraft


def main() -> None:
    """
    Función principal que realiza un cálculo de sustentación de ejemplo.
    
    Crea una aeronave experimental y calcula su fuerza de sustentación
    con parámetros predefinidos.
    """
    print("\n" + "=" * 60)
    print("CALCULADORA DE SUSTENTACIÓN AERODINÁMICA".center(60))
    print("=" * 60)
    
    # Crear aeronave con parámetros de ejemplo
    plane = Aircraft(
        name="Experimental Rotocraft",
        mass=1500,                      # kg
        weight=1500 * 9.81,            # N
        wing_area=20,                   # m²
        velocity=100,                   # m/s
        cl=0.8,                         # coeficiente de sustentación
    )
    
    # Mostrar datos de la aeronave
    plane.show_data()
    
    # Calcular y mostrar sustentación
    lift = plane.calculate_lift()
    wing_loading = plane.calculate_wing_loading()
    
    print("\n--- RESULTADOS DE CÁLCULO ---")
    print(f"Sustentación (L)     : {lift:>15.2f} N")
    print(f"Carga Alar           : {wing_loading:>15.2f} N/m²")
    print(f"Peso (W)             : {plane.weight:>15.2f} N")
    
    # Análisis de viabilidad de vuelo
    print("\n--- ANÁLISIS DE VIABILIDAD ---")
    if lift > plane.weight:
        diferencia = lift - plane.weight
        print(f"✓ VUELO POSIBLE")
        print(f"  Sustentación excesiva: {diferencia:.2f} N")
    elif lift == plane.weight:
        print(f"✓ EQUILIBRIO PERFECTO")
        print(f"  La sustentación iguala al peso")
    else:
        diferencia = plane.weight - lift
        print(f"✗ VUELO IMPOSIBLE")
        print(f"  Sustentación insuficiente: {diferencia:.2f} N")
        print(f"  Se requieren {diferencia:.2f} N adicionales")
    
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
