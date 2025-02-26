#!/usr/bin/env python
# coding: utf-8

# In[1]:


monumentos={
    "Delhi":"Red fort",
    "Paris":"Torre Eifel",
    "Nueva York":"Estatua de la libertad",
    "Rio de janeiro":"Cristo redentor"
}
ciudad=input("Ingresa el nombre de la ciudad")
print("El monumento es ", monumentos[ciudad])


# In[7]:


edad = float(input("Ingresa la edad que deseas sabersi es posible votar"))
if edad >= 18:
    print("es posible votar")
else:
    print("Eres menor de edad, no puedes votar")


# In[13]:


numero1=input("Ingresa el primer numero")
numero2=input("Ingresa el segundo numero")
if numero1>numero2:
    print(numero1," es mayorque ",numero2)
elif numero2>numero1:
    print(numero2," es mayor que ",numero1)


# In[ ]:




