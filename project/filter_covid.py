#!/usr/bin/env python3

'''
Script para filtrar datos de la base de datos.
Primero se filtra para descargar datos que no se han utilizado.
Segundo se filtra por provincia, tambien con la posibilidad de utilizar
los datos de Argentina en su totalidad.
'''

try:

    import pandas as pd

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios! \
Ejecute dependencies_covid.py en /project')

def datos_filtrados():

    '''Función para filtrar datos, eliminando columnas no utilizadas'''

    __url_base_covid__ = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    __filename__ = __url_base_covid__.split('/')[-1]

    __covid_archivo_crudo__ = pd.read_csv('docs/'+__filename__, encoding="utf-16", sep=',',
                                          low_memory=False)

    # __filename_test__ = "covid_19_casos.csv"   #Eliminar postprueba
    #
    # __covid_archivo_crudo__ = pd.read_csv('docs/'+__filename_test__, sep=';',
    #                                       low_memory=False) #Eliminar postprueba

    __datos_interesantes__ = ['sexo', 'edad', 'carga_provincia_nombre',
                              'carga_provincia_id', 'fallecido', 'fecha_fallecimiento',
                              'clasificacion_resumen', 'fecha_diagnostico']

    return __covid_archivo_crudo__[__datos_interesantes__]

def datos_filtrados_provincias(__d_f_p__):

    '''Función para filtrar por provincia o para todo el país'''

    print('''
                Argentina 0
                Ciudad Autónoma de Buenos Aires 2
                Buenos Aires 6
                Catamarca 10
                Córdoba 14
                Corrientes 18
                Chaco 22
                Chubut 26
                Entre Ríos 30
                Formosa 34
                Jujuy 38
                La Pampa 42
                La Rioja 46
                Mendoza 50
                Misiones 54
                Neuquén 58
                Río Negro 62
                Salta 66
                San Juan 70
                San Luis 74
                Santa Cruz 78
                Santa Fe 82
                Santiago del Estero 86
                Tucumán 90
                Tierra del Fuego, Antártida e Islas del Atlántico Sur 94
                ''')

    while True:

        __dictionary_provincia_id__ = {'Ciudad Autónoma de Buenos Aires': 2,
                                       'Buenos Aires': 6, 'Catamarca': 10, 'Córdoba': 14,
                                       'Corrientes': 18, 'Chaco': 22, 'Chubut': 26,
                                       'Entre Ríos': 30, 'Formosa': 34, 'Jujuy': 38,
                                       'La Pampa': 42, 'La Rioja': 46, 'Mendoza': 50,
                                       'Misiones': 54, 'Neuquén': 58, 'Río Negro': 62,
                                       'Salta': 66, 'San Juan': 70, 'San Luis': 74,
                                       'Santa Cruz': 78, 'Santa Fe': 82, 'Santiago del Estero': 86,
                                       'Tucumán': 90, 'Tierra del Fuego, \
                                       Antártida e Islas del Atlántico Sur': 94}

        __input_provincia_f__ = int(input("Seleccione Argentina o la provincia según Nº INDEC: "))

        if  __input_provincia_f__ in __dictionary_provincia_id__.values():

            __covid_filtrado_prov__ = \
            __d_f_p__.loc[__d_f_p__['carga_provincia_id'] == __input_provincia_f__]

            if __covid_filtrado_prov__.empty:

                return 'No hay datos!'

            return __covid_filtrado_prov__, __input_provincia_f__

        if __input_provincia_f__ == 0:

            __covid_filtrado_prov__ = __d_f_p__

            return __covid_filtrado_prov__, __input_provincia_f__

        print('''
                ID de provincia, incorrecto.
                Por favor coloque el ID de la provincia, ó 0 para Argentina.
                ''')

def provincia_id(__p_id__):

    '''Función que devuelve el nombre de la provincia que se esta buscando'''

    __dictionary_provincia_id__ = {'Ciudad Autónoma de Buenos Aires': 2,
                                   'Buenos Aires': 6, 'Catamarca': 10, 'Córdoba': 14,
                                   'Corrientes': 18, 'Chaco': 22, 'Chubut': 26, 'Entre Ríos': 30,
                                   'Formosa': 34, 'Jujuy': 38, 'La Pampa': 42, 'La Rioja': 46,
                                   'Mendoza': 50, 'Misiones': 54, 'Neuquén': 58, 'Río Negro': 62,
                                   'Salta': 66, 'San Juan': 70, 'San Luis': 74, 'Santa Cruz': 78,
                                   'Santa Fe': 82, 'Santiago del Estero': 86, 'Tucumán': 90,
                                   'Tierra del Fuego, Antártida e Islas del Atlántico Sur': 94,
                                   'Argentina': 0}

    for __provincia__, __id_provincia__ in __dictionary_provincia_id__.items():

        if __p_id__ == __id_provincia__:

            return __provincia__

    return ''
