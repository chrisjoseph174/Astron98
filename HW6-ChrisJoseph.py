import numpy as np
import matplotlib.pylab as plt

#HW 6
#Problem 1: Random Plots

list1 = np.random.randint(0,101,size=40)
list2 = np.random.randint(0,101,size=40)
list3 = np.random.randint(0,101,size=40)

plt.figure(1)
plt.subplot(211)
plt.plot(range(len(list1)), list1, linewidth=10, color='orange')
plt.plot(range(len(list2)), list2, color='red', linestyle='--')
plt.title("Line Graph")
plt.legend(list1, list2)

plt.figure(2)
plt.subplot(212)
plt.scatter(range(len(list3)), list3, color='magenta', marker='D')

plt.show()

#Problem 2: van der Waals Gas

pressure = np.linspace(1,10,100)
volume = np.linspace(1,30,100)
R = 0.083144
a = 16.02
b = 0.1124

P, V = np.meshgrid(pressure, volume)
T = ((P + a / V**2) * (V - b)) / (1 * R)

plt.imshow(T, cmap='plasma', vmin=T.min(), vmax=T.max())
plt.colorbar(label='Temperature (K)')
plt.xlabel('Pressure (bar)')
plt.ylabel('Volume (L)')
plt.title('Temperature of Acetone (1 mole)')
plt.show()

#Problem #3: Monte Carlo
def estimatingPi(N):
    points = np.random.rand(int(N), 2)
    distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
    points_inside = distances[distances <= 1]
    pi_estimate = 4 * len(points_inside) / N
    return pi_estimate

N_values = [1e3, 1e4, 1e5, 1e6]

pi_estimates = [estimatingPi(N) for N in N_values]

N = 1e4
points = np.random.rand(int(N), 2)
distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)
points_inside = points[distances <= 1]
points_outside = points[distances > 1]

plt.scatter(points_inside[:, 0], points_inside[:, 1], color='blue')
plt.scatter(points_outside[:, 0], points_outside[:, 1], color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monte Carlo Estimate of π')
plt.legend()
plt.show()