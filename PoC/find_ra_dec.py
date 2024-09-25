from astropy.io import fits
from constants import DATA_FOLDER

def find_ra_dec(filter):
    # Cargar el encabezado del archivo FITS
    image_header = fits.getheader(DATA_FOLDER + '4U0115-0001_' + filter + '_cm.fits')
    ra = image_header.get('OBJCTRA', 'No disponible') 
    dec = image_header.get('OBJCTDEC', 'No disponible') 

    print(f"RA: {ra}")
    print(f"DEC: {dec}")

find_ra_dec('B')
find_ra_dec('I')
find_ra_dec('R')
find_ra_dec('V')