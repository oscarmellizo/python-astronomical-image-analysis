from astropy.io import fits
import matplotlib.pyplot as plt

from constants import DATA_FOLDER

# Cargar la imagen calibrada
imagen_calibrada = fits.getdata(DATA_FOLDER + '2S0114-0001_V_cm_bias_corrected.fits')

# Histograma de intensidades
plt.figure(figsize=(8, 6))
plt.hist(imagen_calibrada.flatten(), bins=100, histtype='step', color='black')
plt.xlabel('Nivel de Señal (ADU)')
plt.ylabel('Número de Píxeles')
plt.title('Histograma de Intensidades - Imagen Calibrada B')
plt.show()