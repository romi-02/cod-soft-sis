#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Planta:
    __tipo='cualquiera'
    def crecer(self):
        print("la flor crece junto al árbol")
    
class Flor(Planta):
    __tipo='gerbera'
    def crecer(self):
        print("la gerbera crece junto al árbol")

class Medicinal(Planta):
    __tipo='bugambilia'
    def crecer(self):
        print("la bugambilia crece junto al árbol")

una_planta=Planta()
print(una_planta.crecer())
una_flor=Flor()
print(una_flor.crecer())
una_medicinal=Medicinal()
print(una_medicinal.crecer())

