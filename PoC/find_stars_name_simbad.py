from astroquery.simbad import Simbad

# Agregar más campos a la consulta (magnitudes en diferentes filtros, tipo espectral, etc.)
Simbad.add_votable_fields('flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'sptype')

def find_star_comparation_simbad(star_name):
    # Consultar SIMBAD por nombre de estrella
    result = Simbad.query_object(star_name)

    # Ver los resultados
    if result is not None:
        print(result)
    else:
        print(f"No se encontró información para la estrella {star_name}")

find_star_comparation_simbad('M31')