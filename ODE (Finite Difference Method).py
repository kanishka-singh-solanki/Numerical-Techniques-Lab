#!/usr/bin/env python
# coding: utf-8

# # ODE (Finite Difference Method)

# In[22]:


import numpy as np
import math
n = 4


# In[27]:


# f(x) = exp(x)

x = np.linspace(0,1,n+2)
h = abs(x[1]-x[0])
y = [h*h*(math.exp(t)) for t in x]
M = np.zeros((n,n+1))
for i in range(n):
    for j in range(n):
        if i==j:
            M[i][j] = -2
        if ((i==j+1)or (i+1==j)):
            M[i][j] = 1
b = y[1:-1]
for i in range(n):
    M[i][n]=b[i]
M[n-1][n] -= math.exp(1)
M[0][n] -= math.exp(0)
M


# In[31]:


def gaussian_elimination(a):
    n = len(a)

    for k in range(n):
        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k, n + 1):
                a[i][j] -= factor * a[k][j]

    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        x[k] = a[k][n] / a[k][k]
        for i in range(k - 1, -1, -1):
            a[i][n] -= a[i][k] * x[k]

    return x
gaussian_elimination(M)

