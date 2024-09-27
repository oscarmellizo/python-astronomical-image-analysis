from astropy.io import fits
import numpy as np
from photutils.detection import DAOStarFinder
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.stats import sigma_clipped_stats
from constants import DATA_FOLDER
from astropy.wcs import WCS

def find_star_comparation_simbad(filter):
    # Cargar la imagen de ciencia
    image_data = fits.getdata(DATA_FOLDER + '2S0114-0001_' + filter + '_cm_bias_corrected.fits')

    mean, median, std = sigma_clipped_stats(image_data, sigma=3.0) 

    mean = np.mean(image_data)
    median = np.median(image_data)
    std = np.std(image_data)

    # Detectar estrellas en la imagen
    daofind = DAOStarFinder(fwhm=4.9, threshold=5.*std)
    sources = daofind(image_data - median)
    
    # Cargar la cabecera de la imagen FITS (asegurarse que contiene información WCS)
    hdu = fits.open(DATA_FOLDER + '2S0114-0001_' + filter + '_cm.fits')[0]
    #wcs = WCS(hdu.header)
    image_header = hdu.header
    
    # Convertir las coordenadas de píxeles a RA/DEC (ejemplo con las primeras estrellas)
    x = sources['xcentroid']
    y = sources['ycentroid']

    # Convertir coordenadas de píxeles a RA/DEC
    #ra_dec = wcs.all_pix2world(x, y, 1)

    # Asegurarse de que sea un array de NumPy
    #ra_dec = np.array(ra_dec)

    # Extraer las coordenadas RA y DEC
    #ra, dec = ra_dec[:, 0], ra_dec[:, 1]

    ra = image_header.get('OBJCTRA', 'No disponible') 
    dec = image_header.get('OBJCTDEC', 'No disponible') 

    # Mostrar las coordenadas RA/DEC
    for i in range(len(sources)):
        print(f"Estrella {i+1}: RA = {ra:.6f}, DEC = {dec:.6f}")

    # Configurar para obtener las magnitudes en los filtros B, V, R, I
    Simbad.add_votable_fields('flux(B)', 'flux(V)', 'flux(R)', 'flux(I)')
    
    # Consultar SIMBAD para cada estrella detectada (usando RA/DEC)
    for i in range(len(ra)):  
        coord = SkyCoord(ra[i], dec[i], unit=(u.deg, u.deg), frame='icrs')
        result = Simbad.query_region(coord, radius='5s')  # Buscar en un radio de 5 arcosegundos

        if result is not None:
            print(f"Resultados para la estrella {i+1}:")
            print(result)
        else:
            print(f"No se encontraron resultados para la estrella {i+1} en SIMBAD.")

find_star_comparation_simbad('B') 
find_star_comparation_simbad('V') 
find_star_comparation_simbad('I') 
find_star_comparation_simbad('R') 
