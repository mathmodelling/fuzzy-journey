# -*- coding: utf-8 -*-
import pandas as pd

__author__ = 'Profesor Efraín. Domínguez Calle, PhD.'
__copyright__ = "Copyright 20015, Mathmodelling"
__credits__ = ["None"]
__license__ = "Uso académico estudiantes de la Pontificia Universidad Javeriana"
__version__ = "1.0"
__maintainer__ = "Efraín Antonio Domínguez Calle"
__email__ = 'e.dominguez@javeriana.edu.co, edoc@marthmodelling.org'
__status__ = "En desarrollo"


# Curso de Hidroclimatología
# Versión del curso: Segundo semestre del 2015
# Los scripts están orientados a los datos de la CAR Resolución Mensual
# Pontificia Universidad Javeriana - Facultad de Estudios Ambientales y Rurales
# Departamento de Ecología y Territorio
# El script es sólo para uso académico de los estudiantes del curso

# Primer paso: Definición de rutas para lectura y guardado de archivos de Excel
excel_entrada = 'IDEAM_M_QL_GRUPOS_Selectas.xlsx'
excel_salida =  'IDEAM_M_QL_GRUPOS_Complementadas.xlsx'
libro = pd.ExcelFile(excel_entrada)
pestanas = libro.sheet_names
print pestanas

# Se prepara un libro de Excel NUEVO en el que se guardaran los datos complementados con la media de cada mes
libro_excel = pd.ExcelWriter(excel_salida)

# Segundo paso Leer datos, por pestañas
for p in pestanas:
    datos = pd.read_excel(excel_entrada, sheetname=p,index_col=0)

    # Tercer paso calcular promedios de columnas del dataframe
    promedios = datos.mean()
    print promedios
    # Cuarto paso rellenamos con los promedios de cada mes
    print datos.to_string()
    datos = datos.fillna(promedios)
    datos['13'] = datos.mean(axis=1)
    print datos.to_string()

    # Quinto guardar datos complementados en el libro de Excel que se guardará al final
    datos.to_excel(libro_excel, sheet_name=p, merge_cells=False)

libro_excel.save()

