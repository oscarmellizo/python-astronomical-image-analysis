from astropy.io import fits
import numpy as np
from photutils.detection import DAOStarFinder
from astropy.stats import mad_std
from astropy.stats import sigma_clipped_stats
from photutils.psf import IntegratedGaussianPRF
from astropy.modeling import fitting
import matplotlib.pyplot as plt
from constants import DATA_FOLDER

def calculate_plate_scale_fwhm_seeing(filter):
    # Cargar la imagen de ciencia
    image_data = fits.getdata(DATA_FOLDER + '4U0115-0001_' + filter + '_cm_bias_corrected.fits')

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

    # Ordenar las estrellas por la columna 'flux' (brillo), de mayor a menor
    sources.sort('flux', reverse=True)

    print(sources)

    image_header = fits.getheader(DATA_FOLDER + '4U0115-0001_' + filter + '_cm.fits')
    focal_length = image_header.get('FOCALLEN', 'No disponible') # Retorna la distancia focal en mm
    pixel_size_x = image_header.get('XPIXSZ', 'No disponible')  # Tamaño del píxel en micrómetros (eje X)
    pixel_size_y = image_header.get('YPIXSZ', 'No disponible') # Tamaño del píxel en micrómetros (eje Y)
    print(f"Distancia Focal del telescopio: {focal_length} mm")
    print(f"Tamaño del píxel (X): {pixel_size_x} micrómetros")
    print(f"Tamaño del píxel (Y): {pixel_size_y} micrómetros")

    # Convertir el tamaño del píxel a milímetros
    pixel_size_mm = pixel_size_x / 1000  # Convertir a milímetros

    # Calcular la escala de placa en arcosegundos por píxel
    plate_scale = (206265 / focal_length) * pixel_size_mm
    print(f"Escala de placa del filtro {filter}: {plate_scale:.4f} arcosegundos/píxel")

    # Ajustar un perfil gaussiano para calcular el FWHM
    fitter = fitting.LevMarLSQFitter()
    psf_model = IntegratedGaussianPRF(sigma=2.0)  

    # Lista para almacenar los valores de FWHM
    fwhm_list = []

    # Ajustar un perfil gaussiano a las 10 estrellas más brillantes
    for star in sources[:15]:  
        x = star['xcentroid']
        y = star['ycentroid']
        
        # Extraer una subimagen alrededor de la estrella
        size = 15
        x_min = int(x) - size
        x_max = int(x) + size
        y_min = int(y) - size
        y_max = int(y) + size
        
        # Verificar si la estrella está cerca del borde
        if (x_min < 0 or y_min < 0 or x_max >= image_data.shape[1] or y_max >= image_data.shape[0]):
            print(f"Estrella en ({x:.2f}, {y:.2f}) está muy cerca del borde, saltando.")
            continue  # Saltar esta estrella si está muy cerca del borde
        
        subimage = image_data[y_min:y_max, x_min:x_max]
        
        # Verificar si la subimagen es válida antes de ajustarla
        print(f"Tamaño de la subimagen: {subimage.shape}")
        
        # Mostrar la subimagen
        plt.imshow(subimage, cmap='gray', origin='lower')
        plt.title(f"Subimagen de la estrella en ({x:.2f}, {y:.2f})")
        plt.colorbar()
        plt.show()
        
        # Crear una cuadrícula de coordenadas para el ajuste
        y_grid, x_grid = np.mgrid[:subimage.shape[0], :subimage.shape[1]]
        
        # Ajustar el modelo gaussiano a la estrella
        try:
            fit = fitter(psf_model, x_grid, y_grid, subimage)
            # Calcular el FWHM a partir de sigma
            fwhm = 2.355 * fit.sigma.value
            fwhm_list.append(fwhm)
            print(f"FWHM de la estrella en ({x:.2f}, {y:.2f}) es: {fwhm:.2f} píxeles")
        except Exception as e:
            print(f"Error ajustando la estrella en ({x:.2f}, {y:.2f}): {e}")

    # FWHM de las 10 estrellas más brillantes
    print("FWHMs calculados:", fwhm_list)

    fwhm_mean = np.mean(fwhm_list)

    print("FWHMs media " + filter + ":", fwhm_mean)

    seeing = fwhm_mean * plate_scale
    print(f"Seeing estimado para filtro {filter}: {seeing:.2f} arcosegundos")
    
calculate_plate_scale_fwhm_seeing('B')
calculate_plate_scale_fwhm_seeing('V')
calculate_plate_scale_fwhm_seeing('R')
calculate_plate_scale_fwhm_seeing('I')