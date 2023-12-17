# Proyecto final - Casino.
# Esmeilin Batista (1200114) - Nathaly Berroa (1200297)

import random
import pygad

def generar_poblacion(num_jugadas):
    """
    Genera una población de números aleatorios de 3 a 4 dígitos.
    """
    return [random.randint(100, 9999) for _ in range(num_jugadas)]

def generar_montos_apostados(num_jugadas, monto_apuestas):
    """
    Genera los montos apostados de manera aleatoria como números enteros positivos,
    asegurándose de que la suma de los montos sea igual al monto total de apuestas.
    """
    montos = [random.randint(1, int(monto_apuestas) - num_jugadas + 1) for _ in range(num_jugadas - 1)]
    montos.append(int(monto_apuestas) - sum(montos))
    
    # Eliminar valores negativos y ceros
    montos = [monto for monto in montos if monto > 0]
    
    return montos

def calcular_montos(montos_apostados, monto_apuestas):
    """
    Calcula diferentes montos relacionados con las apuestas en el casino.
    """
    porcentaje_ganancia_casino = 0.2
    ganancia_casino = int(porcentaje_ganancia_casino * monto_apuestas)
    
    monto_proceso_jugada = int(monto_apuestas - ganancia_casino)
    
    porcentaje_margen_negativo = 0.02
    monto_margen_negativo = int(monto_proceso_jugada - (monto_proceso_jugada * porcentaje_margen_negativo))
    
    porcentaje_margen_positivo = 0.02
    monto_margen_positivo = int(monto_proceso_jugada + (monto_proceso_jugada * porcentaje_margen_positivo))
    
    return ganancia_casino, monto_proceso_jugada, monto_margen_negativo, monto_margen_positivo

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("Bienvenido a nuestro casino")
    
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

    # Mostrar resultados
    print("\nNúmeros de la población:", poblacion)
    print("Montos apostados:", montos_apostados)
    print(f"Suma de Montos apostados: {sum(montos_apostados)}")
    print(f"Ganancia del casino: {ganancia_casino}")
    print(f"Monto después de la ganancia del casino: {monto_proceso_jugada}")
    print(f"Monto con margen negativo: {monto_margen_negativo}")
    print(f"Monto con margen positivo: {monto_margen_positivo}")

if __name__ == "__main__":
    main()
