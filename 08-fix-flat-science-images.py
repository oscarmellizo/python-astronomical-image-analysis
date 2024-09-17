import os
from astropy.io import fits
import numpy as np
from constants import FLAT_FOLDER, DATA_FOLDER

def correct_flat_science_images(filter):
    print("Filter:", filter)
    # Cargar el Master Flat correcto
    master_flat = fits.getdata(FLAT_FOLDER + 'master_flat_normalized_' + filter + '.fits')
    
    # Obtener la lista de archivos de science images
    science_images = [f for f in os.listdir(DATA_FOLDER) if f.endswith('_' + filter + '_cm_bias.fits')]
    
    for image in science_images:
        print("Correcting:", image)
        
        # Cargar la imagen de science
        hdu_list = fits.open(DATA_FOLDER + image)
        data = hdu_list[0].data

        epsilon = 1e-6
        safe_flat = np.where(master_flat > epsilon, master_flat, epsilon)

        # Aplicar la corrección del Master Flat
        corrected_data = data / safe_flat

        # Guardar la imagen corregida
        hdu = fits.PrimaryHDU(corrected_data)
        hdu.writeto(DATA_FOLDER + image.replace('_cm_bias.fits', '_cm_bias_corrected.fits'), overwrite=True)
        
        print("Corrected:", image)
        
        if np.any(np.isinf(corrected_data)) or np.any(np.isnan(corrected_data)):
            print(f"La imagen calibrada de {image} contiene valores infinitos o NaN. Revisa la calibración.")
        continue
        
correct_flat_science_images('B')
#correct_flat_science_images('V')
#correct_flat_science_images('R')
#correct_flat_science_images('I')