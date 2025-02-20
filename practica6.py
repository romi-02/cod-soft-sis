#Materia: CodSofSisIn
#Fecha: 20/02/25
#Alumno: Danha Romina Marín Ventura
#Grupo: 2J
#Nombre de la practica: Listas y tuplas

#!/usr/bin/env python
# coding: utf-8

# In[3]:


tupla_1 =(1,2,3,4,5)
print(tupla_1)


# In[5]:


tupla_2 = (6,7,8,9,10)
print(tupla_2[2])


# In[7]:


tupla_1 = (1,2,3,4,5)
tupla_2 = (6,7,8,9,10)
tupla_nueva= tupla_1 + tupla_2
print(tupla_nueva)


# In[9]:


tupla = ('a','b','c')
print(tupla[0],tupla[1],tupla[2])


# In[15]:


tupla = (1,3,5,7,9)
print(7 in tupla)


# In[17]:


tupla = (0,1,2,3,4,5)
print(tupla[2:4])


# In[19]:


tupla =  (10,20,30,40,50)
print(len(tupla))


# In[21]:


tupla = (3,6,9,12,15)
tupla_repetido = tupla*3
print(tupla_repetido)


# In[23]:


lista = [1,2,3]
tupla = tuple(lista)
print(tupla)


# In[39]:


tupla = (5,12,3,8,15)
print(min (tupla))


# In[41]:


tupla = (5,12,3,8,15)
print(max (tupla))

