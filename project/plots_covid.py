#!/usr/bin/env python3

'''
Funciones para graficar casos, segun corresponda.
'''

try:

    import matplotlib.pyplot as plt

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios!')

def plot_curve_fit_low(x_curve, __y__, __y_pred__, __n_p__):

    '''
    Plot para días vs casos confirmados acumulados con R2 menor que 90%.
    '''

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

def plot_curve_fit_high(x_curve, __y__, __y_pred__, __r2__, __n_p__):

    '''
    Plot para días vs casos confirmados acumulados con R2 mayor o igual que 90%.
    '''

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
