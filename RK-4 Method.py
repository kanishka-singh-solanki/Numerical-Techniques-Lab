#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import matplotlib.pyplot as plt
h = 0.01 
L = 5
n = 500
# ℏ/m = 1


# In[63]:


Ψ = [0 for _ in range(n+1)]
Φ = [0 for _ in range(n+1)]
x = [i*h for i in range(n+1)]
    
def solve(E):
    
    def f1(x,Φ): return Φ
    def f2(x,Ψ): return -2*E*Ψ

    #initial conditions
    Ψ[0] = 0
    Φ[0] = 1

    for i in range(1,n+1):    

        m1 = f1(x[i-1],Φ[i-1])
        m2 = f1(x[i-1]+h/2,Φ[i-1]+m1*h/2)
        m3 = f1(x[i-1]+h/2,Φ[i-1]+m2*h/2)
        m4 = f1(x[i-1]+h,Φ[i-1]+m3*h)
        
        M1 = f2(x[i-1],Ψ[i-1])
        M2 = f2(x[i-1]+h/2,Ψ[i-1]+m1*h/2)
        M3 = f2(x[i-1]+h/2,Ψ[i-1]+m2*h/2)
        M4 = f2(x[i-1]+h,Ψ[i-1]+m3*h)
        
        Ψ[i] = Ψ[i-1] + h/6 * (m1+2*m2+2*m3+m4)
        Φ[i] = Φ[i-1] + h/6 * (M1+2*M2+2*M3+M4)
   

#fig,ax = plt.subplots(15,figsize = (8,14)) 

i = 0
ran = np.linspace(0,10,100)

for E in ran:
    if(i > 14): break
    solve(E)
    if(abs(Ψ[n]) < 0.1):
        ax[i].plot(x,Ψ)
        if(i == 0 or i == 1 or i == 3 or i == 5 or i == 9 or i == 14): 
            plt.plot(x,Ψ)
            print(E)
        i += 1

