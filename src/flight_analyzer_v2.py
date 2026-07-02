import pandas as pd

# Cargamos el archivo CSV con los datos del vuelo
data = pd.read_csv("data/flight01.csv")

# Límites de seguridad definidos para el sistema
MAX_SPEED = 180
MAX_ALTITUDE = 500

# Título del sistema de monitoreo en consola
print("=== FLIGHT SAFETY MONITOR ===")

# Recorremos cada registro del vuelo fila por fila
for _, row in data.iterrows():

    # Lista donde almacenamos las alertas detectadas en cada instante
    alerts = []

    # Verificamos si la velocidad supera el límite máximo permitido
    if row["speed"] > MAX_SPEED:
        alerts.append("WARNING: Overspeed detected")
    
    # Verificamos si la velocidad supera el 120% del límite (condición crítica)
    if row["speed"] > MAX_SPEED * 1.2:
        alerts.append("WARNING: Critical overspeed detected")

    # Verificamos si la altitud supera el límite establecido
    if row["altitude"] > MAX_ALTITUDE:
        alerts.append("WARNING: Altitude limit exceeded")

    # Si se detectaron alertas, mostramos el tiempo y los mensajes
    if alerts:
        print(f"Time {row['time']}s")

        # Imprimimos cada alerta detectada en ese instante
        for alert in alerts:
            print("-", alert)



