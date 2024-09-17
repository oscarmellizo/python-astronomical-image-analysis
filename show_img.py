from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from constants import DATA_FOLDER, BIAS_FOLDER, FLAT_FOLDER
from astropy.visualization import ZScaleInterval

def show_image(image_data):
    print(type(image_data))
    print(image_data.shape)

    # Calcular el número de cuentas máximo y mínimo
    max_counts = np.max(image_data)
    min_counts = np.min(image_data)
    std_counts = np.std(image_data)
    mean_counts = np.mean(image_data)
    median_counts = np.median(image_data)

    # Imprimir los resultados
    print(f"Máximo número de cuentas: {max_counts}")
    print(f"Mínimo número de cuentas: {min_counts}")
    print(f"Std cuentas: {std_counts}")
    print(f"Mean de cuentas: {mean_counts}")
    print(f"Median de cuentas: {median_counts}")

    interval = ZScaleInterval()
    z1, z2 = interval.get_limits(image_data)

    print(f"límite inferior: {z1}")
    print(f"límite superior: {z2}")

    # Mostrar la imagen
    plt.figure(figsize=(10, 10))  # Tamaño de la figura (ajustar según necesidades)
    plt.imshow(image_data, cmap='Blues', origin='lower', vmin=z1, vmax=z2)  # Mapa de colores y origen
    plt.colorbar()  # Mostrar barra de color si es necesario
    plt.title('Imagen de Astronomía')  # Título de la imagen
    plt.xlabel('Coordenada X')  # Etiqueta del eje X
    plt.ylabel('Coordenada Y')  # Etiqueta del eje Y
    plt.grid(False)  # Opcional: mostrar cuadrícula (False para desactivar)
    plt.show()
    

def show_image_by_path(file_path):
    with fits.open(file_path) as hdul:
        image_data = hdul[0].data
        show_image(image_data)

show_image_by_path(DATA_FOLDER + '2S0114-0001_B_cm_bias_corrected.fits')