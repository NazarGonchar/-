import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def model(x, t):
    beta, alpha = 0.3, 0.5
    xdot = [0, 0, 0]
    xdot[0] = -alpha * x[0]
    xdot[1] = alpha * x[0] - beta * x[1]
    xdot[2] = beta * x[1]
    return xdot
q1, q1dot, q2 = 990000, 7000,3000
t0, tf = 0, 25
t = np.linspace(t0, tf, 100)
y0 = [q1, q1dot, q2]
y = odeint(model, y0, t)
print(y)
plt.xlabel('Час')
plt.ylabel('Кількість')
plt.plot(t, y)
plt.legend(["Cприйнятливі", "Інфіковані", "Несприйнятливі"])
plt.show()