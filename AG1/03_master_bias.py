import numpy as np
from astropy.io import fits
import glob
from constants import BIAS_FOLDER
import show_img as si 

bias_files = glob.glob(BIAS_FOLDER + "*.fits")  # Cargar todos los archivos FITS en la carpeta

# Leer las imágenes bias
bias_images = []
for file in bias_files:
    with fits.open(file) as hdul:
        bias_images.append(hdul[0].data)

# Convertir a un array de NumPy para el cálculo
bias_stack = np.array(bias_images)

# Crear el Master Bias (usando la mediana para minimizar el ruido)
master_bias = np.median(bias_stack, axis=0)

# Guardar el Master Bias en un archivo FITS
hdu = fits.PrimaryHDU(master_bias)
hdu.writeto(BIAS_FOLDER + 'master_bias.fits', overwrite=True)

# Visualizar el Master Bias
si.show_image(master_bias)

print("Master Bias creado, guardado y visualizado.")
