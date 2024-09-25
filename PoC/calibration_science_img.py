import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from constants import BIAS_FOLDER, FLAT_FOLDER, DATA_FOLDER

# Cargar el Master Bias y Master Flat
master_bias = fits.getdata(BIAS_FOLDER + 'master_bias.fits')
master_flat_V = fits.getdata(FLAT_FOLDER + 'master_flat_normalized_V.fits')

# Función para calibrar una imagen de ciencia
def calibrar_imagen_ciencia(ciencia_fits, master_bias, master_flat):
    # Cargar la imagen de ciencia
    ciencia = fits.getdata(ciencia_fits)
    
    # Restar el Master Bias
    ciencia_bias_corregida = ciencia - master_bias
    
    # Dividir por el Master Flat
    ciencia_calibrada = ciencia_bias_corregida / master_flat
    
    return ciencia_calibrada

# Ejemplo de calibración para una imagen en filtro V
imagen_ciencia_calibrada_V = calibrar_imagen_ciencia(DATA_FOLDER + '2S0114-0001_V_cm.fits', master_bias, master_flat_V)

# Guardar la imagen calibrada si es necesario
hdu = fits.PrimaryHDU(imagen_ciencia_calibrada_V)
hdu.writeto(DATA_FOLDER + 'ciencia_calibrada_V.fits', overwrite=True)

# Visualizar la imagen calibrada
plt.figure(figsize=(8, 8))
plt.imshow(imagen_ciencia_calibrada_V, cmap='gray', origin='lower', 
           vmin=np.percentile(imagen_ciencia_calibrada_V, 5), 
           vmax=np.percentile(imagen_ciencia_calibrada_V, 95))
plt.colorbar(label='Nivel de Señal (ADU)')
plt.title("Imagen Calibrada - Filtro V")
plt.show()
