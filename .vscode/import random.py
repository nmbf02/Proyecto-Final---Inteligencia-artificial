import random
import pygad

def generar_poblacion(num_jugadas):
    return [random.randint(100, 9999) for _ in range(num_jugadas)]

def calcular_montos(poblacion, monto_apuestas):
    montos_apostados = [random.randint(1, int(monto_apuestas)) for _ in range(len(poblacion))]
    
    porcentaje_ganancia_casino = 0.2
    ganancia_casino = int(porcentaje_ganancia_casino * monto_apuestas)
    
    monto_proceso_jugada = int(monto_apuestas - ganancia_casino)
    
    porcentaje_margen_negativo = 0.02
    monto_margen_negativo = int(monto_proceso_jugada - (monto_proceso_jugada * porcentaje_margen_negativo))
    
    porcentaje_margen_positivo = 0.02
    monto_margen_positivo = int(monto_proceso_jugada + (monto_proceso_jugada * porcentaje_margen_positivo))
    
    return montos_apostados, ganancia_casino, monto_proceso_jugada, monto_margen_negativo, monto_margen_positivo

# Pantalla de bienvenida y preguntas de entrada
print("Bienvenido a nuestro casino")
num_jugadas = int(input("Ingrese la cantidad de jugadas a registrar: "))
monto_apuestas = float(input("Ingrese el monto total de apuestas: "))

# Generación de la población de números
poblacion = generar_poblacion(num_jugadas)

# Cálculo de montos con funciones
montos_apostados, ganancia_casino, monto_proceso_jugada, monto_margen_negativo, monto_margen_positivo = calcular_montos(poblacion, monto_apuestas)

# Ajuste para asegurar que la sumatoria de montos_apostados sea igual a monto_proceso_jugada
ajuste = monto_proceso_jugada - sum(montos_apostados)
if ajuste != 0:
    # Distribuir el ajuste de forma equitativa entre los montos
    ajuste_individual = ajuste // num_jugadas
    montos_apostados = [monto + ajuste_individual for monto in montos_apostados]

# Mostrar resultados
print(f"\nNúmeros de la población: {poblacion}")
print(f"Montos apostados: {montos_apostados}")
print(f"Ganancia del casino: {ganancia_casino}")
print(f"Monto después de la ganancia del casino: {monto_proceso_jugada}")
print(f"Monto con margen negativo: {monto_margen_negativo}")
print(f"Monto con margen positivo: {monto_margen_positivo}")





