import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

x_0, y_0 = 1.0e15, 0
vx_0, vy_0 = 0, 2e7
Mc, m = 9.945e39, 1.989e39
dt, N = 60*60*24, 1700

r, t = planet2D(x_0, y_0, vx_0, vy_0, Mc, m, dt, N)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(np.min(r[:, 0]) * 1.1, np.max(r[:, 0]) * 1.1)
ax.set_ylim(np.min(r[:, 1]) * 1.1, np.max(r[:, 1]) * 1.1)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.grid()
ax.scatter(0, 0, color='#000000', label='Black Hole 1', s=100)
planet, = ax.plot([], [], 'bo', markersize=5, color='#000000', label='Black Hole 2')
trail, = ax.plot([], [], 'b-', lw=0.5)

ax.legend()

def init():
    planet.set_data([], [])
    trail.set_data([], [])
    return planet, trail

def update(frame):
    planet.set_data([r[frame, 0]], [r[frame, 1]])
    trail.set_data(r[:frame+1, 0], r[:frame+1, 1])
    return planet, trail

ani = animation.FuncAnimation(fig, update, frames=N, init_func=init, blit=True, interval=1)
plt.show()
