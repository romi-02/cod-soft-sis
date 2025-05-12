#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Ingles(Humano):
    humano = "Idioma"
    def hablar(self):
        print("Whats up!!")

class Español(Humano):
    humano = "Idioma"
    def hablar(self):
        print("Que onda!!")

class Frances(Humano):
    humano = "Idioma"
    def hablar(self):
        print("Salut, ça va!!")


# In[8]:


class Vehiculo:
    
class Camión(Vehiculo):
    __Marca = "Mercedes Benz"
    def rodar(self):
        print("Esta transportando a la gente")

class Carro(Vehiculo):
    __Modelo = "Nissan"
    def  manejar(self):
        print("Va muy rápido")

class Trailer_de_carga(Vehiculo):
    __peso = "carga apróx. 2 toneladas"
    def tarnsportar(self):
        print("Esta llevando mucho granito")

