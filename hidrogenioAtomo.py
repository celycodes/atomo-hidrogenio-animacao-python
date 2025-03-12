import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')


nucleo, = ax.plot(0, 0, 'ro', markersize=15, label='Núcleo (Próton)')

eletron, = ax.plot([], [], 'bo', markersize=10, label='Elétron')

trajetoria, = ax.plot([], [], 'b--', lw=0.5)

def init():
    eletron.set_data([], [])
    trajetoria.set_data([], [])
    return eletron, trajetoria

def animate(frame):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1  

    eletron_x = r * np.cos(2 * np.pi * frame / 100)
    eletron_y = r * np.sin(2 * np.pi * frame / 100)
    eletron.set_data(eletron_x, eletron_y)
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    trajetoria.set_data(x, y)
    
    return eletron, trajetoria

# Duração da animação = 20 segundos
total_frames = 200  # N° de frames
intervalo = 100  # Intervalo entre frames  (100 ms = 0.1 s)


ani = FuncAnimation(fig, animate, frames=total_frames, init_func=init, blit=True, interval=intervalo)


ax.legend()

plt.title("Átomo de Hidrogênio")


plt.show()