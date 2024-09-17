import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

from constants import DATA_FOLDER

# Cargar la imagen FITS
image_data = fits.getdata(DATA_FOLDER + '2S0114-0001_B_cm_bias_corrected.fits')

# Aplanar la imagen para convertirla en un array 1D
flattened_image = image_data.flatten()

# Graficar el histograma de la imagen
plt.figure(figsize=(10, 6))
plt.hist(flattened_image, bins=100, histtype='step', color='black')  # Puedes ajustar el número de bins
plt.title('Histograma de la imagen FITS')
plt.xlabel('Valor de cuentas (intensidad de píxeles)')
plt.ylabel('Frecuencia')
plt.show()