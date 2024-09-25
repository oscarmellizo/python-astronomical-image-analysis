import numpy as np
from astropy.io import fits
from constants import FLAT_FOLDER

def normalized(filter):
    print("Filter:", filter)
    with fits.open(FLAT_FOLDER + 'master_flat_' + filter + '.fits') as hdul:
        master_flat = hdul[0].data
        # Calcular el número de cuentas (valor promedio)
        cuentas_promedio = np.mean(master_flat)
        print(f"Número de cuentas (valor promedio) del Master Flat: {cuentas_promedio:.2f} del filtro {filter}")
        
        master_flat_normalized = master_flat / cuentas_promedio
        
        cuentas_promedio = np.mean(master_flat_normalized)
        print(f"Número de cuentas (valor promedio) del Master Flat Normalizado: {cuentas_promedio:.2f} del filtro {filter}")
        
        # Guardar el Master Flat en un archivo FITS
        hdu = fits.PrimaryHDU(master_flat_normalized)
        hdu.writeto(FLAT_FOLDER + 'master_flat_normalized_' + filter + '.fits', overwrite=True)

normalized('B')
normalized('V')
normalized('R')
normalized('I')