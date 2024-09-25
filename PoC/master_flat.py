import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import glob

# Cargar el Master Bias
with fits.open('../bias/master_bias.fits') as hdul:
    master_bias = hdul[0].data

# Ruta donde se almacenan los archivos flat (en formato FITS)
flat_folder = "../flats/"
flat_files = glob.glob(flat_folder + "*.fits")  # Cargar todos los archivos FITS en la carpeta

# Leer las imágenes flat y corregirlas con el master bias
flat_images = []
for file in flat_files:
    with fits.open(file) as hdul:
        flat_corrected = hdul[0].data - master_bias  # Restar el Master Bias
        flat_images.append(flat_corrected)

# Convertir la lista a un array de NumPy para el cálculo
flat_stack = np.array(flat_images)

# Crear el Master Flat (usando la mediana para minimizar el ruido)
master_flat = np.median(flat_stack, axis=0)

# Normalizar el Master Flat para que el valor medio sea 1
master_flat /= np.median(master_flat)

# Guardar el Master Flat en un archivo FITS
hdu = fits.PrimaryHDU(master_flat)
hdu.writeto('../flats/master_flat.fits', overwrite=True)

# Visualizar el Master Flat
plt.figure(figsize=(10, 10))
plt.imshow(master_flat, cmap='gray', origin='lower', vmin=0.8, vmax=1.2)
plt.colorbar(label='Nivel de Señal Normalizado')
plt.title("Master Flat")
plt.show()

print("Master Flat creado, guardado y visualizado.")
