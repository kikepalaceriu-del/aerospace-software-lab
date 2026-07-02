import pandas as pd  # Importamos pandas para manejo de datos en formato tabla (CSV)

def load_flight(file_path):
    # Función que carga un archivo de vuelo y valida su estructura
    try:
        flight = pd.read_csv(file_path)  # Leemos el archivo CSV desde la ruta indicada

        required_columns = ["time", "altitude", "speed", "pitch", "roll", "yaw"]  
        # Definimos las columnas obligatorias que debe tener el dataset

        for col in required_columns:  # Recorremos cada columna requerida
            if col not in flight.columns:  # Verificamos si la columna existe en el archivo
                raise ValueError(f"Falta la columna: {col}")  # Lanzamos error si falta alguna columna

        print("✓ Archivo de vuelo cargado correctamente")  # Mensaje de éxito si todo está bien
        return flight  # Devolvemos el DataFrame cargado

    except FileNotFoundError:  # Error si el archivo no existe en la ruta
        print("❌ No se encontró el archivo")  # Mensaje de error específico
        return None  # Retornamos None para indicar fallo

    except Exception as e:  # Capturamos cualquier otro error inesperado
        print(f"❌ Error: {e}")  # Mostramos el error
        return None  # Retornamos None para manejar fallos de forma segura    

