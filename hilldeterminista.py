'funciones de Hill'
n
#programa para graficar las diferentes funciones de Hill

# se importan las librerias
import numpy as np
import math 
import random as rnd
from matplotlib import pyplot

def prod(x, n): # x!/(x-n)!
    prod=x-n+1
    xprod= x-n+1
    if n!=0 and prod-1>=0:
        for i in range(1,n):
            xprod= xprod * (prod+i)
        return xprod
    elif prod-1<0:
        return 0
    else:
        return 1

def H_d(x,n,K,j): #funcion de hill determinista
    return (x/j)**n/(K + (x/j)**n)

def H_sd(x,n,K,j):# funcion de Hill semideterminista
    if x<n:
        return 0
    if x>=n and x<j/2:
        return prod(x,n)/(K*(j**n) + prod(x,n))
    if x>=n and x>=25:
        return prod(x+n,n)/(K*(j**n) + prod(x+n,n))

def H_ss(x,n,K,j):# funcion de Hill semiestocastica
    if x<n:
        return 0
    if x>=n and x<j/2:
        return prod(x,n)/(K*(j**n)*np.exp((n-1)/j) + prod(x,n))
    if x>=n and x>=j/2:
        return prod(x+n,n)/(K*(j**n)*np.exp((n-1)/j) + prod(x+n,n))

def H_ap(x,n,K,j): # funcion de hill con aproximaciones
    return ((x/j)**n + (n/(2*j))*(n-1)*(x/j)**(n-1) )/(K + (x/j)**n + (n/(2*j))*(n-1)*(x/j)**(n-1))

# Valores del eje X que toma el gráfico.
#x = np.arange(0, 1, 0.0001)
x=range(0,60)

# Graficar ambas funciones.
pyplot.plot(x, [H_d(i,2,.01,50) for i in x], label='H_d')
pyplot.plot(x, [H_ap(i,2,.01,50) for i in x], label='H_ap')
#pyplot.plot(x, [f3(i,20,.01) for i in x], label='H_ss')
#pyplot.plot(x, [f1(i,1,.01) for i in x], label='n=1')

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(0, 30)
pyplot.ylim(0, 1.05)
pyplot.title("Hill n=10")
pyplot.xlabel("e (número de enzimas)")
pyplot.ylabel("H")
pyplot.legend()

# Guardar gráfico como imágen PNG.
pyplot.savefig("han10.png")

# Mostrarlo.
pyplot.show()
