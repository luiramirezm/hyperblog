"""2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de la lista está
el mayor número par leído."""

try:

    lista = []
    mayor = 0
    pos = 0

    for i in range(10):
        num = int(input("Digite un número entero:"))
        lista.append(num)
    print(lista)

    for i in range(len(lista)):
        if lista[i] > mayor:
            if lista[i] % 2 == 0:
                mayor = lista[i]
                pos = i
    print("La posición del número par mayor es: ", pos)
        

except ValueError:
    print("No es un número entero")