
#5/3/25
#Danha Romina Marin Ventura
#2J
#Practica 1


#!/usr/bin/env python
# coding: utf-8

# In[23]:


from datetime import datetime
fecha_nacimiento = datetime(2009, 12, 2)
fecha_actual = datetime.now()
dias_vividos = (fecha_actual - fecha_nacimiento).days
print(f"Has vivido {dias_vividos} días.")

