import matplotlib.pyplot as plt

# Datos del eje X (Tamaño de apertura)
aperturas = [8, 9, 10, 11, 12, 13, 14, 15]

# Datos del eje Y (Magnitudes)
magnitudes = [
    [11.836, 11.826, 11.819, 11.815, 11.811, 11.809, 11.807, 11.805],
    [12.473, 12.458, 12.449, 12.443, 12.440, 12.437, 12.436, 12.435],
    [10.851, 10.838, 10.831, 10.826, 10.823, 10.821, 10.819, 10.818],
    [11.491, 11.481, 11.474, 11.469, 11.466, 11.464, 11.462, 11.460],
    [10.377, 10.352, 10.338, 10.331, 10.326, 10.322, 10.320, 10.319],
]

# Etiquetas para cada conjunto de datos (opcional)
etiquetas = [
    'Estrella 1',
    'Estrella 2',
    'Estrella 3',
    'Estrella 4',
    'Estrella 5',
]

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar cada conjunto de datos
for i, magnitud in enumerate(magnitudes):
    plt.plot(aperturas, magnitud, marker='o', label=etiquetas[i])

# Añadir títulos y etiquetas
plt.title('Magnitud vs Tamaño de Apertura')
plt.xlabel('Tamaño de Apertura')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
