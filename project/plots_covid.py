#!/usr/bin/env python3

'''
Funciones para graficar casos, segun corresponda.
'''

try:

    import matplotlib.pyplot as plt

    import seaborn as sns

    import pandas as pd

except ImportError:

    raise ImportError('No se pudieron importar los modulos necesarios!')

def plot_curve_fit_low(x_curve, __y__, __y_pred__, __n_p__):

    '''
    Plot para días vs casos confirmados acumulados con R2 menor que 95%.
    '''

    fig_1 = plt.figure(1, figsize=(11, 6))
    fig_1.suptitle('Casos confirmados acumulados en ' + __n_p__, fontsize=14,
                   fontweight='bold')
    ax_1 = fig_1.add_subplot(111)

    plt.plot(x_curve, __y__, '*', label='Valores originales')

    plt.plot(x_curve, __y_pred__, 'r', label='Predicción')

    ax_1.set_xlabel('Días')
    ax_1.set_ylabel('Casos confirmados acumulados')
    ax_1.text(10, 0.5, 'R2 (Calidad) del modelo baja', style='italic', fontsize=10,
              verticalalignment='bottom', horizontalalignment='left',
              bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

    ax_1.text(0.95, 0.01, 'Autor: Sebastian San Blas - sebastiansanblas@gmail.com',
              verticalalignment='bottom', horizontalalignment='right',
              transform=ax_1.transAxes, color='green', fontsize=8)
    plt.grid(True)
    plt.legend(loc='best')

    plt.show()

def plot_curve_fit_high(x_curve, __y__, __y_pred__, __r2__, __n_p__):

    '''
    Plot para días vs casos confirmados acumulados con R2 mayor o igual que 95%.
    '''

    fig = plt.figure(1, figsize=(11, 6))
    fig.suptitle('Casos confirmados acumulados en ' + __n_p__, fontsize=14, fontweight='bold')
    ax_2 = fig.add_subplot(111)

    plt.plot(x_curve, __y__, '*', label='Valores originales')

    plt.plot(x_curve, __y_pred__, 'r', label='Predicción')

    ax_2.set_xlabel('Días')
    ax_2.set_ylabel('Casos confirmados acumulados')
    ax_2.text(10, 0.5, 'R2: ' + str("{:.2f}".format(__r2__)), style='italic', fontsize=10,
              verticalalignment='bottom', horizontalalignment='left',
              bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})

    ax_2.text(0.95, 0.01, 'Autor: Sebastian San Blas - sebastiansanblas@gmail.com',
              verticalalignment='bottom', horizontalalignment='right',
              transform=ax_2.transAxes, color='green', fontsize=8)
    plt.grid(True)
    plt.legend(loc='best')

    plt.show()

def histograma(x_hist, name_hist):
    '''
    Histograma de fallecidos según edades.
    '''
    x_1 = x_hist.loc[x_hist['fallecido'] == 1]
    hombre = x_1.loc[x_1['sexo'] == 1]
    mujer = x_1.loc[x_1['sexo'] == 0]

    plt.figure(1, figsize=(11, 6))

    sns.kdeplot(hombre['edad'], label="Masculino", color='red')
    sns.kdeplot(mujer['edad'], label="Femenino")
    plt.title('Histograma: Edad vs Fallecidos - ' + str(name_hist))
    plt.ylabel('Densidad')
    plt.xlabel('Edad')
    plt.xlim(0, 120)
    plt.legend(loc="upper right", fontsize='small')
    plt.text(80, -0.0025, 'Autor: Sebastian San Blas - sebastiansanblas@gmail.com',
             color='green', fontsize=8, bbox=dict(facecolor='green', alpha=0.2))
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def plot_proba(clf, name_hist):

    '''Grafica de probabilidad de fallecimiento en función de las edades y sexo.'''

    sexo_f = [0]*101
    sexo_m = [1]*101
    edad = range(101)

    df_f = pd.DataFrame({'sexo': sexo_f, 'edad': edad})
    df_m = pd.DataFrame({'sexo': sexo_m, 'edad': edad})

    x_m = df_m.iloc[:, :2]
    x_f = df_f.iloc[:, :2]

    x_m = x_m.values.reshape(-1, 2)
    x_f = x_f.values.reshape(-1, 2)

    plt.figure(2, figsize=(11, 6))
    plt.plot(x_m[:, 1], clf.predict_proba(x_m)[:, 1], label="Masculino", color='red', linewidth=1)
    plt.plot(x_f[:, 1], clf.predict_proba(x_f)[:, 1], label="Femenino", color='blue', linewidth=1)
    plt.axhline(y=0.5, color='black', linestyle='-')
    plt.title('Probabilidad de fallecimiento en ' + str(name_hist))
    plt.ylabel('Probabilidad')
    plt.xlabel('Edad')
    plt.xlim(0, 100)
    plt.ylim(0, 1)
    plt.grid(True)
    plt.legend(loc="center right", fontsize='small')
    plt.text(65, 0.025, 'Autor: Sebastian San Blas - sebastiansanblas@gmail.com',
             color='green', fontsize=8, bbox=dict(facecolor='green', alpha=0.2))
    plt.tight_layout()
    plt.show()
