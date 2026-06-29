import pandas as pd


def load_flight(file_path):
    try:
        flight = pd.read_csv(file_path)

        required_columns = ["time", "altitude", "speed", "pitch", "roll", "yaw"]

        for col in required_columns:
            if col not in flight.columns:
                raise ValueError(f"Falta la columna: {col}")

        print("✓ Archivo de vuelo cargado correctamente")
        return flight

    except FileNotFoundError:
        print("❌ No se encontró el archivo")
        return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    

