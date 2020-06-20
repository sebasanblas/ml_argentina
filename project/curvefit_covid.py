#!/usr/bin/env python3

'''
Función para calcular función que se ajustará a los datos, de forma exponencial.

Se ajusta mediante los valores "fea" y "feb", posteriormente se calculará el
error R2, devolviendo este valor y los parametros ajustados.
'''

try:

    import matplotlib.pyplot as plt

    import numpy as np

    from scipy.optimize import curve_fit

    from sklearn.metrics import r2_score

    print("Importado modulos necesarios para curvefit_covid.py")

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios!')

def curvefit(__c_f__, __n_p__):

    '''
    Función para calcular función que se ajustará a los datos, de forma exponencial.
    '''
    __csv__ = __c_f__

    __csv__['Día'] = range(1, len(__csv__)+1)

    x_curve = __csv__[['Día']]

    x_curve = np.ravel(x_curve)

    __y__ = __csv__[['Cantidad acumulada']]

    __y__ = np.ravel(__y__)

    def func_exp(__x__, __fea__, __feb__):

        '''Función para realizar ajuste de los datos'''

        return __fea__*np.exp(__feb__/__x__)

    #__popt__, __pcov__ = curve_fit(func_exp, x_curve, __y__)
    __popt__, _ = curve_fit(func_exp, x_curve, __y__)

    __a__ = __popt__[0]

    __b__ = __popt__[1]

    __y_pred__ = func_exp(x_curve, __a__, __b__)

    __r2__ = r2_score(__y__, __y_pred__)

    if __r2__ < 0.90:

        print('''
-----------------------------------------------------------

Calidad del modelo por debajo del 90 %

Se recomienda no continuar la estimación ya que el modelo no será representativo.

¿Desea continuar?
''')

        __resp__ = input("[\"y\" para continuar]:")

        if __resp__ == "y":

            fig_1 = plt.figure()
            fig_1.suptitle('Casos confirmados acumulados ' + __n_p__, fontsize=14,
                           fontweight='bold')
            ax_1 = fig_1.add_subplot(111)

            plt.plot(x_curve, __y__, '*', label='Valores originales')

            plt.plot(x_curve, __y_pred__, 'r', label='Predicción')

            ax_1.set_xlabel('Días')
            ax_1.set_ylabel('Casos confirmados acumulados')
            ax_1.text(10, 0.5, 'R2 (Calidad) del modelo baja', style='italic', fontsize=10,
                      verticalalignment='bottom', horizontalalignment='left',
                      bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

            ax_1.text(0.95, 0.01, 'Sebastian San Blas - sebastiansanblas@gmail.com',
                      verticalalignment='bottom', horizontalalignment='right',
                      transform=ax_1.transAxes, color='green', fontsize=8)

            plt.legend(loc='best')

            plt.show()

            print('''
-----------------------------------------------------------
''')

            print("R cuadrado: {:.2f}".format(__r2__))

    if __r2__ >= 0.90:

        fig = plt.figure()
        fig.suptitle('Casos confirmados acumulados ' + __n_p__, fontsize=14, fontweight='bold')
        ax_2 = fig.add_subplot(111)

        plt.plot(x_curve, __y__, '*', label='Valores originales')

        plt.plot(x_curve, __y_pred__, 'r', label='Predicción')

        ax_2.set_xlabel('Días')
        ax_2.set_ylabel('Casos confirmados acumulados')
        ax_2.text(10, 0.5, 'R2: ' + str("{:.2f}".format(__r2__)), style='italic', fontsize=10,
                  verticalalignment='bottom', horizontalalignment='left',
                  bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})

        ax_2.text(0.95, 0.01, 'Sebastian San Blas - sebastiansanblas@gmail.com',
                  verticalalignment='bottom', horizontalalignment='right',
                  transform=ax_2.transAxes, color='green', fontsize=8)

        plt.legend(loc='best')

        plt.show()

        print('''
-----------------------------------------------------------
''')

        print("R cuadrado: {:.2f}".format(__r2__))
