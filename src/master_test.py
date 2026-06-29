import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("\n🧪 INICIANDO PRUEBA COMPLETA DEL SISTEMA AERONÁUTICO\n")

# SISTEMA DE VUELO
print("\n==============================")
print("✈️ SISTEMA DE VUELO (CSV)")
print("==============================\n")

subprocess.run(["python", os.path.join(BASE_DIR, "src", "run_test.py")])

# SISTEMA X-1 (DESACTIVADO TEMPORALMENTE)
print("\n==============================")
print("🛩️ SISTEMA X-1")
print("==============================\n")

print("⚠️ X-1 desactivado temporalmente (archivo main.py no integrado)\n")

print("\n✔ PRUEBA COMPLETA FINALIZADA\n")