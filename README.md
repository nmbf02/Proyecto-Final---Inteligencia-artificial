# Casino Play Optimization with PyGAD

Este proyecto utiliza el algoritmo genético implementado por `pygad` para optimizar las jugadas en un casino, específicamente enfocado en las jugadas de tipo A y B. Se busca maximizar el valor de las jugadas sin exceder un monto límite determinado por el total jugado y la comisión del casino.

## Descripción

El casino busca optimizar las jugadas de los tipos A y B para asegurar que el premio a repartir se maximice sin superar el monto disponible después de deducir la comisión del casino. Este script implementa un algoritmo genético con `pygad` para encontrar las combinaciones óptimas de jugadas.

## Instalación

Para utilizar este script, necesitarás Python 3.x y `pygad`. Sigue estos pasos para configurar tu entorno:

1. **Instala Python 3.x** desde [python.org](https://www.python.org/downloads/) si aún no lo tienes.

2. **Instala `pygad`** usando pip. Abre tu terminal o línea de comandos y ejecuta el siguiente comando:

   ```bash
   pip install pygad

## Uso

1. Para ejecutar el script de optimización, sigue estos pasos:

2. Descarga el script casino_optimization.py a tu computadora.

3. Abre una terminal en el directorio donde descargaste el script.

4. Ejecuta el script con el siguiente comando:

   ```bash
   python casino_optimization.py

El script iniciará el proceso de optimización y mostrará los resultados en la terminal, incluyendo las mejores jugadas encontradas para los tipos A y B y el valor de fitness correspondiente.

------------------------------------------------------------------------------------------------------------------------------------------------------

# Logica de Implementación de Casino

Este proyecto implementa la lógica base para un juego de casino, enfocándose en mantener un sistema equilibrado que permite al casino obtener beneficios manteniendo al mismo tiempo la equidad y la atracción para los jugadores. La implementación toma en cuenta un margen de error del 2% sobre el monto apostado, así como un porcentaje definido que el casino retiene como beneficio.

## Introducción

Este sistema está diseñado para ser utilizado en cualquier juego de casino, proporcionando una base sólida sobre la cual se pueden construir variaciones específicas de juegos. A través del cálculo de porcentajes y la gestión de apuestas, asegura que el casino pueda operar de manera rentable sin comprometer la justicia hacia los jugadores.

## Características

- **Cálculo de Margen de Error**: Implementa un sistema que permite un margen de error del 2% en el monto apostado, ajustando las probabilidades o pagos para asegurar la viabilidad a largo plazo del casino.

- **Retención de Beneficios**: Define un porcentaje específico de las apuestas que el casino retiene como beneficio, asegurando la sostenibilidad del negocio.

- **Flexibilidad**: Diseñado para adaptarse a una amplia variedad de juegos de casino, permitiendo modificaciones según las necesidades de cada juego específico.
