def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio = ((8 + 9 + 7) / 3)
    maxima = max(8, 7, 9)
    minima = min(8, 9, 7)
    faltante = (10 - promedio)

    print(round(promedio, 2))
    print(maxima)
    print(minima)
    print(round(faltante, 2))
