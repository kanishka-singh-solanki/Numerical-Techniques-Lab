#!/usr/bin/env python
# coding: utf-8

# In[131]:


import numpy as np
import matplotlib.pyplot as plt
h = 0.001


# # Undamped Oscillation

# ### Euler's Method

# In[132]:


n = 10000

X = [0 for _ in range(n)]
V = [0 for _ in range(n)]
t = [i*h for i in range(n)]

#initial conditions
X[0] = 0
V[0] = 5

for i in range(1,n):                 # k/m = 1
    X[i] = X[i-1] + h*V[i-1]
    V[i] = V[i-1] + h*(-X[i-1])

fig,ax = plt.subplots(1,2,figsize = (12,4)) 

ax[0].plot(X,V)
ax[1].plot(t,X)
ax[1].plot(t,V)
ax[0].set_title("Phase Diagram")
ax[1].set_title("X - t")
ax[0].set_xlabel("position(X)")
ax[0].set_ylabel("velocity(V)")
ax[1].set_xlabel("time(t)")
ax[1].set_ylabel("position(X) / velocity(V)")


# ### Central Difference

# In[133]:


n = 10000

X = [0 for _ in range(n)]
t = [i*h for i in range(n)]

#initial conditions
X[0] = 0
X[1] = 0.005

for i in range(2,n):                                # k/m = 1
    X[i] = 2*X[i-1] - X[i-2] + (h**2)*(-X[i-1])

plt.plot(t,X)
plt.title("X - t")
plt.xlabel("time(t)")
plt.ylabel("position(X)")


# # Damped Oscillation

# ### Euler's Method

# In[134]:


n = 100000
γ = 0.2

X = [0 for _ in range(n)]
V = [0 for _ in range(n)]
t = [i*h for i in range(n)]

#initial conditions
X[0] = 0
V[0] = 5

for i in range(1,n):                 # k/m = 1
    X[i] = X[i-1] + h*V[i-1]
    V[i] = V[i-1] + h*(-X[i-1]-γ*V[i-1])       # m = 1

fig,ax = plt.subplots(1,2,figsize = (12,4)) 

ax[0].plot(X,V)
ax[1].plot(t,X)
ax[1].plot(t,V)
ax[0].set_title("Phase Diagram")
ax[1].set_title("X - t")
ax[0].set_xlabel("position(X)")
ax[0].set_ylabel("velocity(V)")
ax[1].set_xlabel("time(t)")
ax[1].set_ylabel("position(X) / velocity(V)")


# ### Central Difference

# In[135]:


n = 100000

X = [0 for _ in range(n)]
t = [i*h for i in range(n)]

#initial conditions
X[0] = 0
X[1] = 0.005

for i in range(2,n):                                                            # k/m = 1
    X[i] = 2*X[i-1] - X[i-2] + (h**2)*(-X[i-1]-0.3*(X[i-1]-X[i-2])/h)          # γ/m = 0.3

plt.plot(t,X)
plt.title("X - t")
plt.xlabel("time(t)")
plt.ylabel("position(X)")

