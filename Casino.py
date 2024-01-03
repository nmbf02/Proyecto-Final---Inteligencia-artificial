import random
import pygad
import time

# Funciones del primer programa
def generar_poblacion(num_jugadas):
    return [random.randint(100, 9999) for _ in range(num_jugadas)]

def generar_montos_apostados(num_jugadas, monto_apuestas):
    montos = [random.randint(1, int(monto_apuestas) - num_jugadas + 1) for _ in range(num_jugadas - 1)]
    montos.append(int(monto_apuestas) - sum(montos))
    montos = [monto for monto in montos if monto > 0]
    return montos

def calcular_montos(montos_apostados, monto_apuestas):
    porcentaje_ganancia_casino = 0.2
    ganancia_casino = int(porcentaje_ganancia_casino * monto_apuestas)
    monto_proceso_jugada = int(monto_apuestas - ganancia_casino)
    porcentaje_margen_negativo = 0.02
    monto_margen_negativo = int(monto_proceso_jugada - (monto_proceso_jugada * porcentaje_margen_negativo))
    porcentaje_margen_positivo = 0.02
    monto_margen_positivo = int(monto_proceso_jugada + (monto_proceso_jugada * porcentaje_margen_positivo))
    return ganancia_casino, monto_proceso_jugada, monto_margen_negativo, monto_margen_positivo

comision_porcentaje = 0.2
num_jugadas_A = 3
num_jugadas_B = 4
limite_monto_repartir = 1200000000
margen_error = 0.02

def generar_jugada(tipo, longitud):
    return ''.join(str(random.randint(0, 9)) for _ in range(longitud))

def evaluar_jugada(jugada, tipo):
    return random.randint(0, 1000)

def calcular_premio_total(jugadas_A, jugadas_B):
    premio_total = 0
    for jugada_A, jugada_B in zip(jugadas_A, jugadas_B):
        premio_total += evaluar_jugada(jugada_A, 'A') + evaluar_jugada(jugada_B, 'B')
    return premio_total

def generar_poblacion_inicial(tamano_poblacion):
    poblacion_A = [generar_jugada('A', num_jugadas_A) for _ in range(tamano_poblacion)]
    poblacion_B = [generar_jugada('B', num_jugadas_B) for _ in range(tamano_poblacion)]
    return poblacion_A, poblacion_B

def seleccionar_mejores(poblacion_A, poblacion_B, monto_repartir):
    mejores_A = []
    mejores_B = []
    premios = []

    for jugada_A, jugada_B in zip(poblacion_A, poblacion_B):
        premio_total = calcular_premio_total([jugada_A] * num_jugadas_A, [jugada_B] * num_jugadas_B)
        if premio_total <= monto_repartir * (1 + margen_error):
            mejores_A.append(jugada_A)
            mejores_B.append(jugada_B)
            premios.append(premio_total)

    # Devolver  las dos mejores jugadas A y B
    indices_mejores = sorted(range(len(premios)), key=lambda k: premios[k], reverse=True)[:2]
    mejores_A = [mejores_A[i] for i in indices_mejores]
    mejores_B = [mejores_B[i] for i in indices_mejores]

    return mejores_A, mejores_B  # Devolver  dos valores

def algoritmo_genetico(num_generaciones, tamano_poblacion):
    poblacion_A, poblacion_B = generar_poblacion_inicial(tamano_poblacion)

    mejores_A, mejores_B = [], []

    for generacion in range(num_generaciones):
        nuevas_mejores_A, nuevas_mejores_B = seleccionar_mejores(poblacion_A, poblacion_B, limite_monto_repartir)

        if generacion < 2:  # Solo las dos primeras generaciones se imprimen como "Mejores jugadas A" y "Mejores jugadas B"
            if nuevas_mejores_A:
                print(f"Generación {generacion + 1}: Mejores jugadas A: {nuevas_mejores_A}, Mejores jugadas B: {nuevas_mejores_B}")
        else:
            # Actualizar si se encuentran nuevas jugadas ganadoras
            mejores_A = nuevas_mejores_A
            mejores_B = nuevas_mejores_B

            # se implementar lógica adicional, como cruzamiento y mutación, para generar la próxima población

    # Imprimir solo las jugadas ganadoras después de todas las generaciones
    if mejores_A and mejores_B:
        print("\nJugada Ganadora A:", mejores_A[0])
        print("Jugada Ganadora B:", mejores_B[0])


# Función principal que ejecuta ambos programas
def main():
    start_time = time.time()

    print("Bienvenido a nuestro casino y al algoritmo genético")
    
    try:
        num_jugadas = int(input("Ingrese la cantidad de jugadas a registrar: "))
        monto_apuestas = float(input("Ingrese el monto total de apuestas: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return
    
    poblacion = generar_poblacion(num_jugadas)
    montos_apostados = generar_montos_apostados(num_jugadas, monto_apuestas)
    
    while sum(montos_apostados) != monto_apuestas:
        montos_apostados = generar_montos_apostados(num_jugadas, monto_apuestas)

    ganancia_casino, monto_proceso_jugada, monto_margen_negativo, monto_margen_positivo = calcular_montos(montos_apostados, monto_apuestas)

    print("\nNúmeros de la población:", poblacion)
    print("Montos apostados:", montos_apostados)
    print(f"Ganancia del casino: {ganancia_casino}")
    print(f"Monto después de la ganancia del casino: {monto_proceso_jugada}")
    print(f"Monto con margen negativo: {monto_margen_negativo}")
    print(f"Monto con margen positivo: {monto_margen_positivo}")

    # Llamada al algoritmo genético
    algoritmo_genetico(num_generaciones=10, tamano_poblacion=20)

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

if __name__ == "__main__":
    main()