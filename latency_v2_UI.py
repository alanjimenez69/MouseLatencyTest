import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pynput import mouse

# 🎨 CONFIGURACIÓN DE ESTILO
FONDO_COLOR = "#1E1E1E"
TEXTO_COLOR = "#FFD700"
LINEA_COLOR = "#00FF00"
LEYENDA_COLOR = "#FFFFFF"

# Lista para almacenar mediciones
latencies = []
timestamps = []
start_time = None

# Configurar la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor(FONDO_COLOR)
ax.set_facecolor(FONDO_COLOR)

ax.set_title("customicemx - Latencia de Clicks", fontsize=14, fontweight="bold", color=TEXTO_COLOR)
ax.set_xlabel("Número de Clicks", fontsize=12, color=TEXTO_COLOR)
ax.set_ylabel("Latencia (s)", fontsize=12, color=TEXTO_COLOR)
ax.tick_params(axis='x', colors=TEXTO_COLOR)
ax.tick_params(axis='y', colors=TEXTO_COLOR)

line, = ax.plot([], [], 'o-', color=LINEA_COLOR, markersize=8, label="Latencia")

legend = ax.legend(facecolor=FONDO_COLOR, edgecolor="white")
for text in legend.get_texts():
    text.set_color(LEYENDA_COLOR)

def on_click(x, y, button, pressed):
    global start_time
    if pressed:
        start_time = time.time()
    else:
        if start_time is not None:
            latency = time.time() - start_time
            latencies.append(latency)
            timestamps.append(len(latencies))
            print(f"Latencia del click: {latency:.4f} segundos")

def update_plot(frame):
    """Función para actualizar el gráfico en tiempo real."""
    if latencies:
        line.set_data(timestamps, latencies)
        ax.set_xlim(0, len(latencies) + 1)
        ax.set_ylim(0, max(latencies) + 0.01)
    return line,

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

ani = animation.FuncAnimation(fig, update_plot, interval=500)

plt.show()

mouse_listener.stop()
mouse_listener.join()
