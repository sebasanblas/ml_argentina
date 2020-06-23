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

    raise ImportError('No se pudieron importar los modulos necesarios!')

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

    plt.figure(figsize=(8, 6))

    plt.subplot(2, 1, 1)
    plt.plot(__covid_fecha__.index, __covid_fecha__['Cantidad'], 'o-')
    plt.title('Confirmados diarios - Confirmados acumalativo - '+str(__t_r_l_2__))
    plt.xlabel('Fecha')
    plt.ylabel('Confirmados')

    plt.subplot(2, 1, 2)
    plt.plot(__covid_fecha__.index, __covid_fecha__['Cantidad acumulada'], '-')
    plt.xlabel('Fecha')
    plt.ylabel('Confirmados acumulados')

    plt.show()

    #__covid_fecha__.to_csv('{}.csv'.format(__t_r_l_2__), index=True, header=True)

    return __covid_fecha__, __t_r_l_2__
