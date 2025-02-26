#Danha Romina Marin Ventura
#practica 9
#2J
#26/02/25


#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
    print(1)


# In[5]:


for i in range(1,20,2):
    print(i)


# In[11]:


lista1=[0,1,2,3,4,5,6,7,8,9]
lista1.sort(reverse=True)
print (lista1)


# In[21]:


numero=int (input("Ingresa el numero que deseas multiplicar"))
for i in range(1,11):
    print(i ," x ",numero, " = ",i * numero)


# In[27]:


numero1="1234567890"
contador=1
numero=input("Ingresa el numero")
numero2=list(numero)
for numero3 in numero2:
    contador = int (numero3)*contador
    print("Producto ",contador)


# In[ ]:




