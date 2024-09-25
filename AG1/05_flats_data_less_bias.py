import os
import numpy as np
from astropy.io import fits
import glob
from constants import BIAS_FOLDER, FLAT_FOLDER, DATA_FOLDER

# Cargar el Master Bias
with fits.open(BIAS_FOLDER + 'master_bias.fits') as hdul:
    master_bias = hdul[0].data

# Ruta donde se almacenan los archivos flat (en formato FITS)
flat_files = glob.glob(FLAT_FOLDER + "*.fits")  # Cargar todos los archivos FITS en la carpeta

# Leer las imágenes flat y corregirlas con el master bias
for file in flat_files:
    with fits.open(file) as hdul:
        flat_corrected = hdul[0].data - master_bias  # Restar el Master Bias
        # Guardar cada imagen corregida en archivos FITS
        hdu = fits.PrimaryHDU(flat_corrected)
        hdu.writeto(FLAT_FOLDER + os.path.basename(file).split(".")[0] + '_bias.fits', overwrite=True)
        
        if np.any(np.isinf(flat_corrected)) or np.any(np.isnan(flat_corrected)):
            print(f"La imagen calibrada de {file} contiene valores infinitos o NaN. Revisa la calibración.")
        continue

print("Flats corregidos y guardados.")

data_files = glob.glob(DATA_FOLDER + "*_cm.fits")  # Cargar todos los archivos FITS en la carpeta

# Leer las imágenes de ciencia (data) y corregirlas con el master bias
for file in data_files:
    with fits.open(file) as hdul:
        data_corrected = hdul[0].data - master_bias  # Restar el Master Bias
        # Guardar cada imagen corregida en archivos FITS
        hdu = fits.PrimaryHDU(data_corrected)
        hdu.writeto(DATA_FOLDER + os.path.basename(file).split(".")[0] + '_bias.fits', overwrite=True)
        
        if np.any(np.isinf(data_corrected)) or np.any(np.isnan(data_corrected)):
            print(f"La imagen calibrada de {file} contiene valores infinitos o NaN. Revisa la calibración.")
        continue
        
print("Datos de ciencia corregidos y guardados.")