import numpy as np
def Euler_method(t0, d0, dt, n):
    """
    Input:    initial value d0, time setp dt, and total computational steps n
    Output:   array d(n+1) with d[0] = d0, d[1] = d(0.01), d[2]=d(0.01) ... d[100] = d(1.00)
    """
    d = np.zeros(n + 1)
    d[0] = d0

    t = np.zeros(n + 1)
    for i in range(n + 1):
        t[i] = t0 + i * dt

    """
    Add a loop to compute d[1] to d[100] using Euler's method
    """

    return t, d
    # The right-hand side function of the differential equation
def f(t, d):
    return t * t - 3.0 * t + d


# The exact solution of the differential equation
def d_exact(t):
    return -t * t + t + 1.0


t0 = float(0.0)
d0 = float(1.0)
dt = float(0.01)
n = int(100)

t, d = Euler_method(t0, d0, dt, n)

de = np.zeros(n + 1)
for i in range(n + 1):
    de[i] = d_exact(t[i])


import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(t, d, "-r", label="Euler method")
plt.plot(t, de, "-b", label="Exact solution")
plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("d")
plt.grid()
plt.show()