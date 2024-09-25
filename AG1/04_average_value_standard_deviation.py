import numpy as np
from astropy.io import fits
from constants import BIAS_FOLDER

# Cargar el Master Bias
with fits.open(BIAS_FOLDER + 'master_bias.fits') as hdul:
    master_bias = hdul[0].data

# Calcular el número de cuentas (valor promedio)
cuentas_promedio = np.mean(master_bias)

# Calcular la desviación estándar
desviacion_estandar = np.std(master_bias)

# Imprimir los resultados
print(f"Número de cuentas (valor promedio) del Master Bias: {cuentas_promedio:.2f}")
print(f"Desviación estándar del Master Bias: {desviacion_estandar:.2f}")
