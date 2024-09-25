from astropy.io import fits
from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad
import astropy.units as u
from constants import DATA_FOLDER

def find_ra_dec(filter):
    # Cargar el encabezado del archivo FITS
    image_header = fits.getheader(DATA_FOLDER + 'XTE1946-0001_' + filter + '_cm.fits')
    ra = image_header.get('OBJCTRA', 'No disponible') 
    dec = image_header.get('OBJCTDEC', 'No disponible') 

    print(f"RA: {ra}")
    print(f"DEC: {dec}")
    
    coord = SkyCoord(ra, dec, unit=(u.deg, u.deg), frame='icrs')
    result = Simbad.query_region(coord, radius='5s')  # Buscar en un radio de 5 arcosegundos

    if result is not None:
        print(f"Resultados para la estrella en filtro {filter}:")
        print(result)
    else:
        print(f"No se encontraron resultados para la estrella en filtro {filter} en SIMBAD.")

find_ra_dec('B')
find_ra_dec('I')
find_ra_dec('R')
find_ra_dec('V')