#!/usr/bin/env python3

'''
Script para actualizar base de datos provistado por el gobierno nacional,
obtenida de su página oficial.
'''

try:

    from tqdm import tqdm

    import requests

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios! \
Ejecute dependencies_covid.py en /project')

def update():
    '''Función para decidir si actualizar la base de datos o no'''
    while True:
        __resp__ = input("¿Desea descargar/actualizar la base de datos?[y/n]:")
        if __resp__ == "y":
            update_datos() #cambiar por update_datos()
            break
        if  __resp__ == "n":
            break
        print("Opción invalida")

def update_datos():

    '''
    Función para descargar la base de datos si es necesario.
    '''

    __url_base_covid__ = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    __requests__ = requests.get(__url_base_covid__, stream=True)

    __total_size__ = int(__requests__.headers['content-length'])

    __filename__ = __url_base_covid__.split('/')[-1]

    with open("docs/"+__filename__, 'wb') as __f__:
        for data in tqdm(iterable=__requests__.iter_content(chunk_size=1024),
                         total=__total_size__/(1024), unit='kB',):
            __f__.write(data)

    print("Base de datos actualizada.")

def update_datos_prueba():

    '''
    Función para descargar la base de datos si es necesario.
    '''

    __url_base_covid__ = "http://ipv4.download.thinkbroadband.com/5MB.zip"

    __requests__ = requests.get(__url_base_covid__, stream=True)

    __total_size__ = int(__requests__.headers['content-length'])

    __filename__ = __url_base_covid__.split('/')[-1]

    with open('docs/'+__filename__, 'wb') as __f__:
        for data in tqdm(iterable=__requests__.iter_content(chunk_size=1024),
                         total=__total_size__/(1024), unit='kB',):
            __f__.write(data)

    print("Base de datos actualizada.(prueba)")

def check_update():
    '''
    Función para comprobar la descarga de la base de datos.
    '''

    __url_base_covid__ = "https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.csv"

    __filename__ = __url_base_covid__.split('/')[-1]

    with open("docs/"+__filename__) as __check__:
        __check__.close()
