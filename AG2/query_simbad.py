from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u

# Coordenadas de la estrella en formato h:m:s para RA y d:m:s para DEC
ra_hms = "23h33m44s"  # Ejemplo de RA en h:m:s
dec_dms = "+05d46m35s"  # Ejemplo de DEC en d:m:s

# Crear el objeto de coordenadas SkyCoord en el sistema ICRS
coord = SkyCoord(ra=ra_hms, dec=dec_dms, frame='icrs')

# Configurar SIMBAD para obtener magnitudes en diferentes filtros y sus errores
Simbad.add_votable_fields('flux(B)', 'flux_error(B)', 'flux(V)', 'flux_error(V)', 'flux(R)', 'flux_error(R)', 'flux(I)', 'flux_error(I)')

# Consultar SIMBAD para la estrella en las coordenadas especificadas con un radio de búsqueda de 2 segundos
result = Simbad.query_region(coord, radius='2s')

# Mostrar los resultados
print(result)
