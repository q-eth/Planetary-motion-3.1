import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def planet2D(x_0, y_0, vx_0, vy_0, Mc, m, dt, N):
    G = 6.67430e-11

    x = np.zeros(N)
    y = np.zeros(N)
    t = np.zeros(N)

    x[0], y[0] = x_0, y_0
    vx, vy = vx_0, vy_0

    r = np.sqrt(x[0]**2 + y[0]**2)
    ax = -G * Mc * x[0] / r**3
    ay = -G * Mc * y[0] / r**3
    
    x[1] = x[0] + vx * dt + 0.5 * ax * dt**2
    y[1] = y[0] + vy * dt + 0.5 * ay * dt**2
    
    for i in range(1, N - 1):
        r = np.sqrt(x[i]**2 + y[i]**2)
        ax = -G * Mc * x[i] / r**3
        ay = -G * Mc * y[i] / r**3
        
        x[i+1] = 2*x[i] - x[i-1] + ax * dt**2
        y[i+1] = 2*y[i] - y[i-1] + ay * dt**2
        
        t[i] = i * dt
    
    t[-1] = (N-1) * dt

    fig, ax = plt.subplots(figsize=(10, 10))

    max_range = 1.5 * max(abs(x_0), abs(y_0), 1e10)
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    
    ax.plot(0, 0, 'yo', markersize=10, label='Sun')
    line, = ax.plot([], [], color='gray', label='Planet Trajectory')
    point, = ax.plot([], [], 'bo', markersize=5, label='Planet', markerfacecolor='#000080')
    
    def update(frame):
        if frame >= len(x):
            return line, point
        line.set_data(x[:frame+1], y[:frame+1])
        point.set_data([x[frame]], [y[frame]])
        return line, point
    
    ani = animation.FuncAnimation(fig, update, frames=N, interval=2, blit=True)
    ax.legend()
    plt.show()
    
    return x, y, t

x0, y0 = 1.0e15, 0
v0x, v0y = 0, 2e7
Mc, m = 1e40, 2e39
dt = 60*60*24
N = 3000
x, y, t = planet2D(x0, y0, v0x, v0y, Mc, m, dt, N)
