#Danha Romina Marin Ventura
#Practica 10
#2J
#5/3/25


#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Introduce un número para calcular su factorial: "))
if num < 0:
    print("El factorial no está definido para números negativos.")
else:
    result = factorial(num)
    print(f"El factorial de {num} es {result}.")


# In[3]:


def suma_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10  
        numero //= 10 
    return suma
num = int(input("Introduce un número para calcular la suma de sus dígitos: "))
resultado = suma_digitos(num)
print(f"La suma de los dígitos de {num} es {resultado}.")


# In[7]:


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
print(f"Los números primos entre {num1} y {num2} son:")
for num in range(num1, num2 + 1):
    if es_primo(num):
        print(num)


# In[9]:


n = int(input("Introduce un número: "))
for i in range(1, n + 1):
    linea = ''.join(str(x) for x in range(1, i + 1))
    print(f"#{linea}")

