def escribe_fichero(mensaje):
    with open('fichero_comunicación.txt', 'w') as fichero:
        fichero.write(mensaje)

def lee_fichero():
    mensaje = ""
    with open('fichero_comunicación.txt', 'r') as fichero:
        mensaje = fichero.read()
    return mensaje

nombre = input('Escribe tu nombre')
ciudad = input('Escribe una ciudad')
comida = input('Tu comida favorita')
edad = input('Escribe cuantos anos tienes')

escribe_fichero("De acuerdo")
print(lee_fichero())