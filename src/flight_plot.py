import pandas as pd  # Importamos pandas para manejar datos en formato tabla (CSV)
import matplotlib.pyplot as plt  # Importamos matplotlib para generar gráficas

data = pd.read_csv("data/flight01.csv")  # Cargamos el archivo CSV con los datos del vuelo

print(data.head())  # Mostramos las primeras filas del dataset para verificación rápida

# Crear figura principal para las gráficas con tamaño definido
plt.figure(figsize=(10,6))

# 1. Gráfica de altitud vs tiempo
plt.subplot(3,1,1)  # Primera de 3 subgráficas (posición 1)
plt.plot(data["time"], data["altitude"])  # Línea de altitud en función del tiempo
plt.title("Altitude vs Time")  # Título de la gráfica
plt.ylabel("Altitude")  # Etiqueta del eje Y

# 2. Gráfica de velocidad vs tiempo
plt.subplot(3,1,2)  # Segunda subgráfica (posición 2)
plt.plot(data["time"], data["speed"])  # Línea de velocidad en función del tiempo
plt.title("Speed vs Time")  # Título de la gráfica
plt.ylabel("Speed")  # Etiqueta del eje Y

# 3. Gráfica combinada de perfil de vuelo
plt.subplot(3,1,3)  # Tercera subgráfica (posición 3)

plt.plot(data["time"], data["altitude"], label="Altitude")  # Línea de altitud con etiqueta
plt.plot(data["time"], data["speed"], label="Speed")  # Línea de velocidad con etiqueta

plt.title("Flight Profile Overview")  # Título general del perfil de vuelo
plt.xlabel("Time")  # Etiqueta del eje X
plt.legend()  # Mostrar leyenda para diferenciar las curvas

plt.tight_layout()  # Ajusta automáticamente el espacio entre subgráficas
plt.savefig("documentation/images/flight_plot_day7.png")  # Guarda la imagen del gráfico en archivo
plt.show()  # Muestra la figura en pantalla
