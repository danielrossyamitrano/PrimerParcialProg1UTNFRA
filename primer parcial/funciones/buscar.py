def buscar_nota(matriz: list, nota_buscada: int) -> list:
    # 4 – Función buscar_nota(): Recibe la matriz y una nota buscada, y
    # retorna una lista con todas las posiciones (fila, columna) donde aparece
    # esa nota exacta.

    posiciones = []  # creamos una lista de posiciones vacía.
    for y in range(len(matriz)):  # "y" representa las filas de la matriz
        for x in range(len(matriz[y])):  # "x" representa las columnas de la matriz
            if matriz[y][x] == nota_buscada:  # matriz[y][x] es la nota. Si coincide con nota_buscada
                posiciones.append((x, y))  # agregamos la posicion a la lista

    return posiciones  # devolvemos la lista de posiciones.
