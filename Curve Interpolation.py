#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
pi = np.pi


# # Lagrange Interpolation

# In[13]:


X = [0.5, 1.5, 3.0, 5.0, 6.5, 8.0]
Y = [1.625, 5.875, 31.0, 131.0, 282.125, 521.0]
n = len(X)

x = 7
y = 0

for i in range(n):
    prod = 1
    for j in range(n):
        if(i != j):
            prod *= (x-X[j]) / (X[i] - X[j])
    y += Y[i] * prod
y


# # Nevilles Interpolation

# In[7]:


n = 20
X = np.linspace(-3*pi,3*pi,n)
Y = np.sin(X) + np.cos(X)

def P(i, j, x):
    if (i == j):
        return Y[i];
    value = ((X[j] - x) * P(i, j - 1, x) + (x - X[i]) * P(i + 1, j, x)) / (X[j] - X[i]);
    return value;

x = pi/3
P(0, n-1, x)


# In[15]:


def comp(n):
    X = np.linspace(-3*pi,3*pi,n)
    Y = np.sin(X) + np.cos(X)

    def P(i, j, x):
        if (i == j):
            return Y[i];
        value = ((X[j] - x) * P(i, j - 1, x) + (x - X[i]) * P(i + 1, j, x)) / (X[j] - X[i]);
        return value

    X1 = np.linspace(-3*pi,3*pi,100)
    Y1 = []
    for x in X1:
        Y1.append(P(0,n-1,x))
    return Y1


# In[16]:


X1 = np.linspace(-3*pi,3*pi,100)
fig, ax = plt.subplots(7)
i = 0
for n in range(1,20,3):
    Y1 = comp(n)
    ax[i].plot(X1,Y1, color = 'r')
    i += 1
plt.show()


# In[17]:


X1 = np.linspace(-3*pi,3*pi,100)
Y1 = np.sin(X1) + np.cos(X1)
plt.plot(X1,Y1, color = 'c')


# # Newton Interpolation

# In[19]:


n = 20
X = np.linspace(-3*pi,3*pi,n)
Y = np.sin(X) + np.cos(X)
dividedDiff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dividedDiff[i][i] = Y[i]

for k in range(1,n,1):
    i = 0
    while(i+k<n):
        dividedDiff[i][i+k] = (dividedDiff[i+1][i+k] - dividedDiff[i][i+k-1]) / (X[i+k] - X[i])
        i += 1
        
x = pi/12
y = dividedDiff[0][0]

for i in range(1,n,1):
    prod = 1
    for j in range(i):
        prod *= x - X[j]
    y += dividedDiff[0][i] * prod
y


# In[19]:


def comp(n):
    X = np.linspace(-4*pi,4*pi,n)
    Y = np.sin(X) + np.cos(X)
    dividedDiff = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dividedDiff[i][i] = Y[i]

    for k in range(1,n,1):
        i = 0
        while(i+k<n):
            dividedDiff[i][i+k] = (dividedDiff[i+1][i+k] - dividedDiff[i][i+k-1]) / (X[i+k] - X[i])
            i += 1
        
    def P(x):
        y = dividedDiff[0][0]

        for i in range(1,n,1):
            prod = 1
            for j in range(i):
                prod *= x - X[j]
            y += dividedDiff[0][i] * prod
        return y

    X1 = np.linspace(-4*pi,4*pi,100)
    Y1 = []
    for x in X1:
        Y1.append(P(x))
    return Y1


# In[20]:


X1 = np.linspace(-4*pi,4*pi,100)
fig, ax = plt.subplots(10)
i = 0
for n in range(1,30,3):
    Y1 = comp(n)
    ax[i].plot(X1,Y1, color = 'r')
    i += 1
plt.show()


# In[21]:


X1 = np.linspace(-3*pi,3*pi,100)
Y1 = np.sin(X1) + np.cos(X1)
plt.plot(X1,Y1, color = 'c')


# # Gregory Newton

# In[22]:


n = 20
X = []
val = 0

for i in range(n):
    X.append(val)
    val += 10 * (pi/180)
    
Y = np.sin(X)
Diff = [[0 for _ in range(n)] for _ in range(n)]

def fact(n):
    if(n == 0): return 1
    return n * fact(n-1)

for i in range(n):
    Diff[i][i] = Y[i]

for k in range(1,n,1):
    i = 0
    while(i+k<n):
        Diff[i][i+k] = (Diff[i+1][i+k] - Diff[i][i+k-1])
        i += 1
        
x = 35 * (pi/180)
y = Diff[0][0]
h = X[1] - X[0]
s = (x - X[0]) / h

for i in range(1,n,1):
    prod = 1
    for j in range(i):
        prod *= s - j
    y += (Diff[0][i] * prod) / fact(i)
y


# # Rational Interpolation

# In[23]:


n = 6
X = np.linspace(0.01,pi-0.01,n)
Y = [1/np.tan(_) for _ in X]
inverseDividedDiff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
    inverseDividedDiff[0][i] = (X[i] - X[0]) / (Y[i] - Y[0])

for i in range(1,n,1):
    for j in range(i+1,n,1):
        inverseDividedDiff[i][j] = (X[j] - X[i]) / (inverseDividedDiff[i-1][j] - inverseDividedDiff[i-1][i])

x = 0.75
y = inverseDividedDiff[n-2][n-1]

for i in range(n-2,0,-1):
    y = (x-X[i])/y + inverseDividedDiff[i-1][i]
y = Y[0] + (x-X[0])/y

y

