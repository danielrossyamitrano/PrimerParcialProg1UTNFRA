def cargar_matriz_notas() -> list:
    """Carga la cantidad de alumnos y las notas de los mismos"""
    while True:
        n = input('Ingrese la cantidad de alumnos: ')
        if not n.isdigit() or not 0 < int(n):  # verifica que el ingreso sea un número natural y que sea mayor que 0.
            print("ingrese un número natural")
        else:
            n = int(n)
            break  # salimos del bucle porque no hay más alumnos para ingresar.

    while True:
        x = input('Ingrese la cantidad de notas: ')
        if not x.isdigit() or not 0 < int(x):  # verifica que el ingreso sea un número natural y que sea mayor que 0.
            print("ingrese un número natural")
        else:
            x = int(x)
            break  # salimos del bucle porque no hay más notas para ingresar.

    matriz = [[0 for _ in range(n)] for _ in range(x)]  # creamos una matriz vacia de n * x
    for a in range(int(n)):  # hace que el prompt aparezca solo la cantidad de veces necesaria para los cada alumno.
        print(f"\nA continuación, ingrese las notas para el alumno #{a}.")
        i = 0
        while i < x:
            m = input(f'Ingrese la nota {i + 1}/{x} para el alumno #{a}: ')
            test_1 = m.isdigit()  # verifica que el input sea un número
            test_2 = test_1 and 1 <= int(m) <= 10  # verifica que el input sea un número entre 1 y 10.
            test_3 = not test_1 and m == ''  # verifica que el input este en blanco para pasar al siguiente alumno.
            if test_3:
                break  # si el usuario puso un espacio en blanco, salta al siguiente alumno.
            elif not test_1 or not test_2:  # valida y si no fuera correcto imprime error.
                print('Igrese un número natural entre 1 y 10')
            else:
                matriz[a][i] = int(m)  # agregamos la nota a la columna correspondiente al alumno.
                i += 1

    return matriz
