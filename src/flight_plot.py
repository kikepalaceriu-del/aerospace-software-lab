import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/flight01.csv")

print(data.head())

# Crear figura
plt.figure(figsize=(10,6))

# 1. Altitud
plt.subplot(3,1,1)
plt.plot(data["time"],data["altitude"])
plt.title("Altitude vs Time")
plt.ylabel("Altitude")

# 2. Velocidad
plt.subplot(3,1,2)
plt.plot(data["time"],data["speed"])
plt.title("Speed vs Time")
plt.ylabel("Speed")

# 3. Perfil combinado
plt.subplot(3,1,3)
plt.plot(data["time"],data["altitude"],
    label="Altitude")

plt.plot(data["time"],data["speed"],
    label="Speed")

plt.title("Flight Profile Overview")
plt.xlabel("Time")
plt.legend()

plt.tight_layout()
plt.savefig("documentation/images/flight_plot_day7.png")
plt.show()  
