import os

from constants import DATA_FOLDER

def listar_archivos_y_split(carpeta, indice_elemento=0):
    archivos_procesados = []

    # Recorrer todos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        # Verificar que es un archivo y no un directorio
        if os.path.isfile(os.path.join(carpeta, archivo)):
            # Hacer split del nombre del archivo en base a '-'
            partes = archivo.split('-')

            # Verificar que el índice sea válido
            if len(partes) > indice_elemento:
                # Guardar el elemento seleccionado del split
                archivos_procesados.append(partes[indice_elemento])

    return archivos_procesados

# Ruta de la carpeta que deseas leer
ruta_carpeta = './carpeta_con_archivos'

# Llamar a la función para procesar los archivos
archivos_resultantes = listar_archivos_y_split(DATA_FOLDER)

# Eliminar duplicados usando un conjunto (set)
archivos_unicos = list(set(archivos_resultantes))

# Imprimir la lista de archivos sin duplicados
print(archivos_unicos)

