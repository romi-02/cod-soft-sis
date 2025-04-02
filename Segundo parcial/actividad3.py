#!/usr/bin/env python
# coding: utf-8

# In[3]:


nombre = str(input(" ¿cual es tu nombre? ")) 
ciudad = str(input(" ¿de que ciudad eres? "))
comida = str(input(" ¿cual es tu comida favorita? "))
edad = str(input(" ¿cual es tu edad? "))

def escibe_fichero(mensaje):
    with open('fichero_comunicacion.txt' ,'w') as fichero:
        fichero.write(mensaje)

def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    return mensaje
    escribe_fichero("Esto es un mensaje")
    print(lee_fichero())

