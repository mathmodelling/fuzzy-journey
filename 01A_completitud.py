# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

__author__ = 'Profesor Efraín. Domínguez Calle, PhD.'
__copyright__ = "Copyright 2015, Mathmodelling"
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

#Primer paso Lectura de archivo de Excel
excel_entrada = 'IDEAM_M_QL_GRUPOS_Sin_Anomalos.xlsx'
excel_salida = 'IDEAM_M_QL_GRUPOS_Selectas.xlsx'
libro = pd.ExcelFile(excel_entrada)
pestanas = libro.sheet_names
print pestanas

# Se prepara un libro de Excel NUEVO en el que se guardaran los datos con los anómalos retirados
libro_excel = pd.ExcelWriter(excel_salida)

for p in pestanas:
    print 'Leyendo pestaña:', p
    df = pd.read_excel(excel_entrada, index_col=0, columns=0, sheetname=p)
    #Número de meses con registro
    nm = df.count().sum()
    #Numero de años esperados
    ne = df.index.max() - df.index.min() + 1
    print nm, ne
    #Porcentaje de faltantes
    pfal = (1.0 - (nm/(ne*12.0)))*100
    print pfal, nm/12
    #Comprobación l'ogica de completitud y faltantes
    if (pfal <= 30) and ((nm/12) >= 30):
        df.to_excel(libro_excel, sheet_name=p, merge_cells=False)
    else:
        pass
libro_excel.save()
print np.size(pd.ExcelFile(excel_salida).sheet_names)
print np.size(pestanas)


