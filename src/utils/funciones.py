
# FUNCIONES PERSONALIZADAS:


# 1.FUNCIÓN: Crea una columna anual con la media de todos los trimestres.

def calcular_columna_anual(nombre_archivo):
    # Se extrae de la columna 'TRIMESTRE' el año '(\d\d\d\d)' y llamamos a esa nueva columna 'PERIODO'.
    nombre_archivo['PERIODO'] = nombre_archivo['TRIMESTRE'].str.extract('(\d\d\d\d)', expand=False)
    # Se borra la columna 'TRIMESTRE', porque no la vamos a necesitar.
    nombre_archivo = nombre_archivo.drop(['TRIMESTRE'], axis=1)
    # Se agrupa las columnas, se hace la media y se reinicia el id.
    try:
        nombre_archivo = nombre_archivo.groupby([nombre_archivo.iloc[:, 0],'PERIODO']).mean()
        # Redondeamos los valores de la columna 'DESEMPLEO' tenga dos decimales.
        nombre_archivo = nombre_archivo.round(decimals=2)
        nombre_archivo = nombre_archivo.reset_index()
        return nombre_archivo
    except:
        nombre_archivo = nombre_archivo.groupby('PERIODO').mean()
        nombre_archivo = nombre_archivo.round(decimals=2)
        # Redondeamos los valores de la columna 'DESEMPLEO' tenga dos decimales.
        nombre_archivo = nombre_archivo.reset_index()
        return nombre_archivo





# 2.FUNCIÓN: Quita el número de las comunidades autónomas.

def quitar_ca(nombre_archivo):
    # Se extrae de la columna 'CA' el año '(\d\d\d\d)' y llamamos a esa nueva columna 'CCAA'.
    nombre_archivo['CCAA'] = nombre_archivo['CA'].str.extract('((?<=(\d\s)).$)', expand=True)
    # Se borra la columna 'CA', porque no la vamos a necesitar.
    nombre_archivo = nombre_archivo.drop(['CA'], axis=1)
    return nombre_archivo