import pygad
import random

# Configuraciones iniciales
monto_jugado = 595.00  # Monto jugado total en el ejemplo
comision_porcentaje = 0.2  # Porcentaje de comisión del casino
monto_repartir = monto_jugado - (monto_jugado * comision_porcentaje)  # Monto a repartir después de la comisión

# Definir la función de fitness
def fitness_func(solution, solution_idx):
    valor_A = sum(int(d) for d in str(solution[0]))  # Estimación simplificada de valor para A
    valor_B = sum(int(d) for d in str(solution[1]))  # Estimación simplificada de valor para B
    total_valor = (valor_A * 600) + (valor_B * 1200)  # Asumiendo un valor de ejemplo por dígito
    
    if total_valor <= monto_repartir:
        return 1.0 / (monto_repartir - total_valor + 1)  # Fitness más alto para valores más cercanos al monto a repartir
    else:
        return 0  # Penalización por exceder el monto a repartir

# Configuración de `pygad` para el algoritmo genético
num_genes = 2  # Dos genes: uno para jugada A y otro para B
sol_per_pop = 10  # Número de soluciones por población
num_parents_mating = 4  # Número de padres para el apareamiento

# Definición de espacios de genes para A y B con rangos simplificados
gene_space = [{'low': 100, 'high': 999},  # Rango para jugadas A
              {'low': 1000, 'high': 9999}]  # Rango para jugadas B

# Callback para monitorear la evolución
def on_generation(ga_instance):
    print(f"Generación: {ga_instance.generations_completed}")
    print(f"Mejor solución: {ga_instance.best_solution()[0]} Fitness: {ga_instance.best_solution()[1]}")

# Crear la instancia de GA
ga_instance = pygad.GA(num_generations=50,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_space=gene_space,
                       on_generation=on_generation)

# Ejecutar el GA
ga_instance.run()

# Obtener e imprimir la mejor solución
mejor_solucion = ga_instance.best_solution()
print(f"\nMejor Jugada A: {mejor_solucion[0][0]}, Mejor Jugada B: {mejor_solucion[0][1]}")
print(f"Fitness de la Mejor Solución: {mejor_solucion[1]}")
