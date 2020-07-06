#!/usr/bin/env python3

'''
Función para calcular función que se ajustará a los datos, de forma exponencial.

Se ajusta mediante los valores "fea" y "feb", posteriormente se calculará el
error R2, devolviendo este valor y los parametros ajustados.
'''

try:

    import numpy as np

    from scipy.optimize import curve_fit

    from sklearn.metrics import r2_score

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios! \
Ejecute dependencies_covid.py en /project')

def func_exp(__x__, __fea__, __feb__):

    '''Función para realizar ajuste de los datos'''

    return __fea__*np.exp(__feb__/__x__)

def curvefit(__c_f__):
    '''
    Función para calcular función que se ajustará a los datos, de forma exponencial.
    '''
    __csv__ = __c_f__

    __csv__['Día'] = range(1, len(__csv__)+1)

    x_curve = __csv__[['Día']]

    x_curve = np.ravel(x_curve)

    __y__ = __csv__[['Cantidad acumulada']]

    __y__ = np.ravel(__y__)

    __popt__, _ = curve_fit(func_exp, x_curve, __y__)

    __a__ = __popt__[0]

    __b__ = __popt__[1]

    __y_pred__ = func_exp(x_curve, __a__, __b__)

    __r2__ = r2_score(__y__, __y_pred__)

    return x_curve, __y__, __y_pred__, __r2__, __a__, __b__
