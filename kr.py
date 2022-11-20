import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import quad
import numpy as np
speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
#Номер 1
time = np.arange(0, 12)
#Номер 2
print(time)
#Номер 3
plt.plot(time, speed)
plt.xlabel('Час')
plt.ylabel('Швидкість')
plt.axhline(0, 11)
plt.ylim(0, 130)
plt.grid()
plt.show()
#Номер 4
cubic = interp1d(time, speed, kind='cubic')
time_cubic = np.arange(0, 11, 0.0011)
speed_cubic = cubic(time_cubic)
plt.plot(time_cubic, speed_cubic)
plt.title('Кубічна інтерполяція')
plt.grid()
plt.show()
#Номер 5
print(quad(cubic, 0, 11))
#Номер 6
qua = interp1d(time, speed, kind='quadratic')
time_qua = np.arange(0, 11, 0.0011)
speed_qua = qua(time_qua)
plt.plot(time_qua, speed_qua)
plt.title('Квадратична інтерполяція')
plt.grid()
plt.show()
print(quad(qua, 0, 11))
plt.plot(time_qua, speed_qua)
plt.plot(time_cubic, speed_cubic, color='orange')
plt.scatter(time, speed, color='red')
plt.legend(['Квадратична','Кубічна','Оригінал'])
plt.grid()
plt.show()