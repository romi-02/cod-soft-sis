#!/usr/bin/env python
# coding: utf-8

# In[7]:


nombre = str(input(" < romina > /n")) 
ciudad = int(input(" < 15 > /n"))
comida favorita = int(input(" < pozole >
edad =

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


# In[ ]:




