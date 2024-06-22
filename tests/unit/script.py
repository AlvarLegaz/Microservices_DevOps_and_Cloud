import os

rutas = ['/ruta/a/mi/archivo.txt', '/ruta/a/mi/otro_archivo.txt']
sub_ruta_comun = os.path.commonpath(rutas)
print(f'Sub-ruta común: {sub_ruta_comun}')