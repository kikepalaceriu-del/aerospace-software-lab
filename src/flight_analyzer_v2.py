import pandas as pd

data = pd.read_csv("data/flight01.csv")

MAX_SPEED = 180
MAX_ALTITUDE = 500

print("=== FLIGHT SAFETY MONITOR ===")

for _, row in data.iterrows():

    alerts = []

    if row["speed"] > MAX_SPEED:
        alerts.append("WARNING: Overspeed detected")
    
    if row["speed"] > MAX_SPEED*1.2:
        alerts.append("WARNING: Critical overspeed detected")


    if row["altitude"] > MAX_ALTITUDE:
        alerts.append("WARNING: Altitude limit exceeded")

    if alerts:
        print(f"Time {row['time']}s")

        for alert in alerts:
            print("-", alert)




