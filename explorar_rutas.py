import os
import glob

# 1. Imprime el directorio de trabajo actual
print("CWD:", ...)   # completa con la función de os que devuelve el CWD

# 2. Construye la ruta al CSV declaraciones_dirty.csv usando os.path.join
ruta_csv = os.path.join("data", "inputs", "declaraciones_dirty.csv")
print("Ruta CSV:", ruta_csv)

# 3. Verifica si el archivo existe
print("¿Existe?", ...)

# 4. Imprime solo el nombre del archivo (sin carpetas)
print("Nombre:", ...)

# 5. Lista todos los archivos CSV en data/inputs/ (usa glob con el patrón *.csv)
csvs = ...
print("CSVs encontrados:", csvs)