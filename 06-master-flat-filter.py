import numpy as np
from astropy.io import fits
import glob
from constants import FLAT_FOLDER

# Ruta donde se almacenan los archivos flat (en formato FITS)

def create_master_flat(filter):
    flat_files = glob.glob(FLAT_FOLDER + "FLAT*" + filter + "_bias.fits")  # Cargar todos los archivos FITS en la carpeta por filtro

    print("Filter:", filter)
    # Leer las imágenes flat y corregirlas con el master bias
    flat_images = []
    for file in flat_files:
        print("File:", file)
        with fits.open(file) as hdul:
            flat_images.append(hdul[0].data)
            
    # Convertir la lista a un array de NumPy para el cálculo
    flat_stack = np.array(flat_images)

    # Crear el Master Flat (usando la mediana para minimizar el ruido)
    master_flat = np.median(flat_stack, axis=0)

    # Guardar el Master Flat en un archivo FITS
    hdu = fits.PrimaryHDU(master_flat)
    hdu.writeto(FLAT_FOLDER + 'master_flat_' + filter + '.fits', overwrite=True)
    print("----------")
    
create_master_flat('B')
create_master_flat('V')
create_master_flat('R')
create_master_flat('I')