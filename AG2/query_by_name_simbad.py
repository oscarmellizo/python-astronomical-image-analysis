from astroquery.simbad import Simbad
import pandas as pd

# Configurar SIMBAD para obtener magnitudes en diferentes filtros y sus errores
Simbad.add_votable_fields('flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'flux_error(B)', 'flux_error(V)', 'flux_error(R)', 'flux_error(I)')

# Consultar SIMBAD para una estrella específica
result = Simbad.query_object("PG1633+099")

# Convertir el resultado a un DataFrame de pandas
df = result.to_pandas()

# Mostrar todas las columnas sin truncar
pd.set_option('display.max_columns', None)
print(df)
