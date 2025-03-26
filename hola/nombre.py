with open('nombres.txt', 'r') as fichero:
    for linea in fichero.readlines():
        print(linea, end='')