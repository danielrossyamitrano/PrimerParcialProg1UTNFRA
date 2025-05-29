def mejor_promedio(matriz: list) -> None:
    # 3 – Función mejor_promedio(): Calcula el promedio de cada alumno y
    # determina cuál tiene el mejor promedio. Retorna el índice del alumno y
    # el valor del promedio.

    notas_ordenadas = []  # lista vacía con las notas de los alumnos que serán ordenadas
    alumnos = []  # lista de alumnos, en princio vacía, que contendrá indices de alumnos ordenados.
    for i in range(len(matriz)):
        suma = 0  # el acumulador se inicia en 0 por alumno.
        alumnos.append(i)  # agregamos el índice del alumno a la lista de alumnos
        notas_alumno = matriz[i]  # cada fila de la matriz es el conjunto de notas del alumno
        for nota in notas_alumno:
            if type(nota) is not int:  # una validación adicional por las dudas.
                print(f"Nota {nota} inválida")  # no podemos hacer la suma si la nota no es un integer.
                break
            else:
                suma += int(nota)  # sumamos 1 por cada nota aprobada.
        promedio = round(suma / len(notas_alumno))
        # calculamos el porcentaje de las notas; round() es solo para prolijidad.
        notas_ordenadas.append(promedio)

    # bubble sort mejorado
    # ordena los alumnos pero por nota
    n = len(notas_ordenadas)
    for i in range(len(notas_ordenadas)):
        ordenado = False
        j = 0
        while j < n - 1 - i:
            if notas_ordenadas[j] > notas_ordenadas[j + 1]:
                aux2 = alumnos[j]
                alumnos[j] = alumnos[j + 1]
                alumnos[j + 1] = aux2
                ordenado = True
            j += 1
        if not ordenado:
            break

    print(f"El alumno con mejor promedio es el #{alumnos[-1]}")