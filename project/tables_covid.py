#!/usr/bin/env python3

'''
Script que contiene funcione para crear y modificar tablas que se utilizarán
para estimaciones.
Se incluye tambien, funciones para graficar datos, segun corresponda.
'''

try:

    import pandas as pd

    import matplotlib.pyplot as plt

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios! \
Ejecute dependencies_covid.py en /project')

def tabla_regresion(__t_r_l_1__, __t_r_l_2__):

    ''' Función para transformar tabla para regresión de casos seleccionados,
       siempre y cuando esten clasificados como "Confirmado"'''

    __covid_fecha__ = __t_r_l_1__.loc[__t_r_l_1__[
        'clasificacion_resumen'] == 'Confirmado']

    __covid_fecha__ = __covid_fecha__[['fecha_diagnostico']]

    __covid_fecha__ = __covid_fecha__.groupby('fecha_diagnostico')['fecha_diagnostico'].count()

    __covid_fecha__ = pd.DataFrame({'Fecha':__covid_fecha__.index,
                                    'Cantidad':__covid_fecha__.values})

    __covid_fecha__ = __covid_fecha__.set_index('Fecha')

    idx = pd.date_range(__covid_fecha__.index.min(), __covid_fecha__.index.max())

    __covid_fecha__.index = pd.DatetimeIndex(__covid_fecha__.index)

    __covid_fecha__ = __covid_fecha__.reindex(idx, fill_value=0)

    __covid_fecha__['Cantidad acumulada'] = __covid_fecha__.Cantidad.cumsum()

    plt.figure(figsize=(11, 6))

    plt.subplot(2, 1, 1)
    plt.plot(__covid_fecha__.index, __covid_fecha__['Cantidad'], 'o-')
    plt.title('Confirmados en '+str(__t_r_l_2__))
    plt.ylabel('Confirmados diarios')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(__covid_fecha__.index, __covid_fecha__['Cantidad acumulada'], '-')
    plt.xlabel('Fecha')
    plt.ylabel('Confirmados acumulados')
    plt.grid(True)

    plt.show()

    return __covid_fecha__, __t_r_l_2__

def fecha_inicial(__t_r_l_1__):

    ''' Función para conseguir la fecha minina del primer confirmado de COVID '''

    __covid_fecha__ = __t_r_l_1__.loc[__t_r_l_1__[
        'clasificacion_resumen'] == 'Confirmado']

    __covid_fecha__ = __covid_fecha__['fecha_diagnostico']

    return min(__covid_fecha__)
