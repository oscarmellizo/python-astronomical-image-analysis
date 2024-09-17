from astropy.io import fits
import numpy as np
from photutils.detection import DAOStarFinder
from astropy.stats import mad_std
from astropy.stats import sigma_clipped_stats
from constants import DATA_FOLDER

# Cargar la imagen de ciencia
image_data = fits.getdata(DATA_FOLDER + '2S0114-0001_B_cm_bias_corrected.fits')

mean, median, std = sigma_clipped_stats(image_data, sigma=3.0) 

mean = np.mean(image_data)
median = np.median(image_data)
std = np.std(image_data)

print("mean",  mean, "median", median, "std", std)

# Calcular el ruido (desviación estándar robusta)
bkg_sigma = mad_std(image_data - median)

# Detectar estrellas en la imagen
daofind = DAOStarFinder(fwhm=4.9, threshold=5.*std)
sources = daofind(image_data - median)
sources.sort('peak')

# Seleccionar las 5 estrellas más brillantes
brightest_stars = sources[:5]  # Seleccionamos las 5 más brillantes
print(brightest_stars)

