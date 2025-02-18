import numpy as np
import matplotlib.pyplot as plt

def planet2D(x_0, y_0, vx_0, vy_0, Mc, m, dt, N):
    G = 6.67430e-11
    M = Mc
    
    r = np.zeros((N+1, 2))
    v = np.zeros((N+1, 2))
    t = np.linspace(0, (N+1)*dt, N+1)

    r[0] = np.array([x_0, y_0])
    v[0] = np.array([vx_0, vy_0])

    r[1] = r[0] + v[0] * dt 

    for i in range(1, N):
        r_norm = np.linalg.norm(r[i])
        a = -G * M * r[i] / r_norm**3
        r[i+1] = 2 * r[i] - r[i-1] + a * dt**2
    
    return r, t

x_0, y_0 = 1.5e11, 0
vx_0, vy_0 = 0, 29780
Mc, m = 1.989e30, 5.972e24
dt, N = 60*60, 9000

r, t = planet2D(x_0, y_0, vx_0, vy_0, Mc, m, dt, N)

plt.figure(figsize=(8, 8))
plt.plot(r[:, 0], r[:, 1], color = '#0000FF', label = 'Planet')
plt.scatter(0, 0, color='#000000', label = 'Sun', s = 100)
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.legend()
plt.grid()
plt.show()
