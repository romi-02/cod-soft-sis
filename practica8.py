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


# In[3]:


edad = float(input("Ingresa la edad que deseas sabersi es posible votar"))
if edad >= 18:
    print("es posible votar")
else:
    print("Eres menor de edad, no puedes votar")


# In[5]:


numero1=input("Ingresa el primer numero")
numero2=input("Ingresa el segundo numero")
if numero1>numero2:
    print(numero1," es mayorque ",numero2)
elif numero2>numero1:
    print(numero2," es mayor que ",numero1)


# In[13]:


edades=[]
edad1=int(input("ingresa tu edad"))
edades.append(edad1)
edad2=int(input("ingresa tu edad"))
edades.append(edad2)
edad3=int(input("ingresa tu edad"))
edades.append(edad3)
edad4=int(input("ingresa tu edad"))
edades.append(edad4)

print("la edad menor es",min(edades))


# In[21]:


mayus="QWERTYUIOPÑLKJHGFDSAZXCVBNM"
minus="qwertyuiopñlkjhgfdsazxcvbnm"
palabra=input("ingresa tu palabra")
letras=list(palabra)
for letra in letras:
    if letra in mayus:
        print("letra mayuscula",letra)
    elif letra in minus:
        print("letra minuscula",letra)
    else: 
        print("es un numero o iun simbolo",letra)


# In[ ]:




