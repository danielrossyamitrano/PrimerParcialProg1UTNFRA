from funciones import *


def menu():
    matriz = None
    opciones = [
        ["Cargar Matriz de notas", cargar_matriz_notas],
        ["Calcular el mejor porcentaje", porcentaje_aprobados],
        ["Calcular el mejor promedio", mejor_promedio],
        ["Buscar una nota en el registro", buscar_nota]
    ]
    while True:
        cargada = " (cargada)" if matriz is not None else ""
        opciones[0][0] += cargada

        print("\nSeleccione la operación que desea ejecutar")
        for i in range(len(opciones)):
            print(f"{i} - {opciones[i][0]}")

        opcion = input("> ")
        if opcion.isdigit() and 0 <= int(opcion) < len(opciones):
            opcion = int(opcion)
            if opcion == 0:
                matriz = opciones[opcion][1]()

            elif (1 <= opcion <= len(opciones)) and matriz is None:
                print("Ingrese primero las notas de los alumnos (opción #0)")

            elif 1 <= opcion <= 2 and matriz is not None:
                # esto discrimina porque las funciones 1 y 2 toman solo el parámetro "matriz"
                opciones[opcion][1](matriz)

            elif opcion == 3 and matriz is not None:
                # mientras que la función 3 toma los parámetros "matriz" y "nota_buscada"
                nota_buscada = input("Ingrese la nota buscada: ")
                if nota_buscada.isdigit() and 1 <= int(nota_buscada) <= 10:
                    posiciones = opciones[opcion][1](matriz, int(nota_buscada))
                    print(f'La nota "{nota_buscada}" aparece en las posiciones:')
                    if len(posiciones):
                        for i in range(len(posiciones)):
                            x, y = posiciones[i]
                            print(f'{i}: {x},{y}')
                    else:
                        f'La nota "{nota_buscada}" no aparece en la matriz de notas.'

        else:
            print("Por favor, ingrese un número entre 0 y 3 para seleccionar una opción")


menu()
