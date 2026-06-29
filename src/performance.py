"""
Módulo Performance - Análisis de desempeño de aeronaves

Este módulo calcula la carga alar (wing loading) y otros parámetros
de desempeño de la aeronave proporcionados por el usuario.

La carga alar es un indicador importante del desempeño aerodinámico.

Autor: Enrique
Fecha: 2026
"""

from aircraft import Aircraft


def calculate_performance(aircraft: Aircraft) -> dict:
    """
    Calcula métricas de desempeño de una aeronave.
    
    Args:
        aircraft: Instancia de Aircraft
        
    Returns:
        dict: Diccionario con métricas de desempeño
        
    Raises:
        ValueError: Si faltan datos requeridos
    """
    if aircraft.wing_area <= 0:
        raise ValueError("El área alar debe ser mayor a cero")
    
    wing_loading = aircraft.calculate_wing_loading()
    lift = aircraft.calculate_lift()
    
    # Categorizar desempeño basado en carga alar
    if wing_loading < 25:
        category = "Muy ligero (entrenamiento/acrobacias)"
    elif wing_loading < 100:
        category = "Ligero (aviación general)"
    elif wing_loading < 500:
        category = "Moderado (transporte regional)"
    else:
        category = "Pesado (transporte comercial)"
    
    return {
        "wing_loading": wing_loading,
        "lift": lift,
        "category": category,
        "status": "Viable" if lift > aircraft.weight else "Necesita más sustentación"
    }


def main() -> None:
    """
    Función principal que realiza análisis interactivo de desempeño.
    
    Captura datos del usuario y calcula métricas de desempeño de la aeronave.
    """
    print("\n" + "=" * 60)
    print("ANÁLISIS DE DESEMPEÑO DE AERONAVES".center(60))
    print("=" * 60 + "\n")
    
    try:
        # Captura de datos del usuario
        name = input("Ingrese el nombre del avión: ").strip() or "Avión sin nombre"
        mass = float(input("Ingrese la masa (kg): "))
        wing_area = float(input("Ingrese el área alar (m²): "))
        
        if mass <= 0 or wing_area <= 0:
            print("✘ Error: La masa y el área alar deben ser positivas")
            return
        
        # Crear instancia de Aircraft
        plane = Aircraft(name, mass, wing_area=wing_area)
        plane.weight = plane.mass * Aircraft.GRAVITY
        
        # Calcular desempeño
        performance = calculate_performance(plane)
        
        # Mostrar resultados
        print("\n" + "-" * 60)
        print("RESULTADOS".center(60, "-"))
        print("-" * 60)
        print(f"Nombre del avión     : {plane.name}")
        print(f"Masa                 : {plane.mass:.2f} kg")
        print(f"Peso                 : {plane.weight:.2f} N")
        print(f"Área alar            : {plane.wing_area:.2f} m²")
        print(f"Carga alar           : {performance['wing_loading']:.2f} N/m²")
        print(f"Categoría            : {performance['category']}")
        print(f"Estado               : {performance['status']}")
        print("-" * 60 + "\n")
        
    except ValueError as e:
        print(f"✘ Error: Entrada inválida - {e}\n")
    except Exception as e:
        print(f"✘ Error inesperado: {e}\n")


if __name__ == "__main__":
    main()
