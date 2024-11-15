import numpy as np
def f(t):
    return t**2
t = np.linspace(0,1,11)
print(t)
y = f(t)
print(y)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(t, y, "-r", label="Euler method")
#plt.plot(t, de, "-b", label="Exact solution")
plt.legend(loc="upper left")
plt.xlabel("t")
plt.ylabel("d")
plt.grid()
plt.show()