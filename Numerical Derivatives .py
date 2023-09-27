#!/usr/bin/env python
# coding: utf-8

# In[201]:


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / np.tan(x)

def df(x):
    return -1 / (np.sin(x) ** 2)

h = 0.001
pi = np.pi


# # Forward Difference

# In[202]:


def f1(x):
    return (f(x+h) - f(x)) / h

print("f'(x) =",f1(0.01))
print("Error:",abs(f1(0.01)-df(0.01)))


# # Central difference

# In[203]:


def f2(x):
    return (f(x+h) - f(x-h)) / (2*h)

print("f'(x) =",f2(0.01))
print("Error:",abs(f2(0.01)-df(0.01)))


# # Interpolating polynomial

# In[204]:


n = 12
X = np.linspace(0.001,pi-0.001,n)
Y = [1/np.tan(_) for _ in X]
dividedDiff = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dividedDiff[i][i] = Y[i]

for k in range(1,n,1):
    i = 0
    while(i+k<n):
        dividedDiff[i][i+k] = (dividedDiff[i+1][i+k] - dividedDiff[i][i+k-1]) / (X[i+k] - X[i])
        i += 1
        
def f3(x):
    ans = dividedDiff[0][1]
    for i in range(2,n):
        s = 0
        for j in range(i):
            p = 1
            for k in range(i):
                if(k != j): p *= (x-X[k])
            s += p
        ans += dividedDiff[0][i] * s
    return ans
    
print("f'(x) =",f3(0.01))
print("Error:",abs(f3(0.01)-df(0.01)))


# # Richardson extrapolation

# In[205]:


def f4(x):
    return (8*f(x+h)-8*f(x-h)-f(x+2*h)+f(x-2*h)) / (12*h)

print("f'(x) =",f4(0.01))
print("Error:",abs(f4(0.01)-df(0.01)))


# # Comparison of Derivative Curves

# In[206]:


n = 1000

fig,ax = plt.subplots(1,2,figsize = (12,4)) 

#plot of derivative of Cot(x)

X = np.linspace(0.1,pi-0.1,n)
Y = [df(_) for _ in X]

X1 = np.linspace(pi+0.1,2*pi-0.1,n)
Y1 = [df(_) for _ in X1]

X2 = np.linspace(2*pi+0.1,3*pi-0.1,n)
Y2 = [df(_) for _ in X2]

ax[0].plot(X,Y,'c')
ax[0].plot(X1,Y1,'c')
ax[0].plot(X2,Y2,'c')

ax[0].set_title("Actual Derivative")

#plot of numerical derivative of Cot(x)

X = np.linspace(0.1,pi-0.1,n)
Y = [f1(_) for _ in X]

X1 = np.linspace(pi+0.1,2*pi-0.1,n)
Y1 = [f1(_) for _ in X1]

X2 = np.linspace(2*pi+0.1,3*pi-0.1,n)
Y2 = [f1(_) for _ in X2]

ax[1].plot(X,Y,'b')
ax[1].plot(X1,Y1,'b')
ax[1].plot(X2,Y2,'b')

ax[1].set_title("Numerical Derivative by Forward difference")


# In[207]:


n = 1000

fig,ax = plt.subplots(1,2,figsize = (12,4)) 

#plot of derivative of Cot(x)

X = np.linspace(0.1,pi-0.1,n)
Y = [df(_) for _ in X]

X1 = np.linspace(pi+0.1,2*pi-0.1,n)
Y1 = [df(_) for _ in X1]

X2 = np.linspace(2*pi+0.1,3*pi-0.1,n)
Y2 = [df(_) for _ in X2]

ax[0].plot(X,Y,'c')
ax[0].plot(X1,Y1,'c')
ax[0].plot(X2,Y2,'c')

ax[0].set_title("Actual Derivative")

#plot of numerical derivative of Cot(x)

X = np.linspace(0.1,pi-0.1,n)
Y = [f2(_) for _ in X]

X1 = np.linspace(pi+0.1,2*pi-0.1,n)
Y1 = [f2(_) for _ in X1]

X2 = np.linspace(2*pi+0.1,3*pi-0.1,n)
Y2 = [f2(_) for _ in X2]

ax[1].plot(X,Y,'b')
ax[1].plot(X1,Y1,'b')
ax[1].plot(X2,Y2,'b')

ax[1].set_title("Numerical Derivative by Central difference")


# In[218]:


n = 8

X = np.linspace(0.01,pi-0.01,n)
Y = [df(_) for _ in X]

plt.plot(X,Y,'c')

X = np.linspace(0.01,pi-0.01,n)
Y = [f1(_) for _ in X]

plt.plot(X,Y,'b')

