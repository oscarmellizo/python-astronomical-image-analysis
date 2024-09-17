from astropy.io import fits
from constants import DATA_FOLDER

# Cargar la imagen
filename = DATA_FOLDER + '4U0115-0001_B_cm.fits'
hdu_list = fits.open(filename)

# Leer el encabezado (header)
header = hdu_list[0].header

# Mostrar todo el encabezado
print(repr(header))

# Buscar las claves de metadatos más comunes
focal_length = header.get('FOCALLEN', 'No disponible')
pixel_size = header.get('PIXSCALE', 'No disponible')

# Mostrar los resultados
print(f"Distancia Focal: {focal_length}")
print(f"Tamaño de Píxel (escala de placa): {pixel_size}")

hdu_list.close()